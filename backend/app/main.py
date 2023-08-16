from flask_restful import Api, Resource, reqparse
from app import create_app
from models import *
from flask_cors import CORS

app = create_app()
api = Api(app)

CORS(app)

class EducationsResource(Resource):
  def get(self):
    educations = Educations.query.all()
    return [{'id': e.id, 'education': e.education} for e in educations], 200

class MaritalsResource(Resource):
  def get(self):
    maritals = Maritals.query.all()
    return [{'id': m.id, 'marital': m.marital} for m in maritals], 200

class QuestionsResource(Resource):
  def get(self):
    questions = Questions.query.all()
    return [{'id': q.id, 'question': q.question, 'answer_type': q.answer_type} for q in questions], 200

class PersonResource(Resource):
  def post(self):
    json_args = reqparse.RequestParser()
    json_args.add_argument('age', type=int, required=True)
    json_args.add_argument('sex', type=str, required=True)
    json_args.add_argument('marital_id', type=int, required=True)
    json_args.add_argument('education_id', type=int, required=True)
    json_args.add_argument('roommates', type=int, required=True)
    json_args.add_argument('is_hired', type=bool, required=True)
    args = json_args.parse_args()

    person = Person(
      age=args['age'],
      sex=args['sex'],
      marital_id=args['marital_id'],
      education_id=args['education_id'],
      roommates=args['roommates'],
      is_hired=args['is_hired']
    )
    db.session.add(person)
    db.session.commit()
    return {'message': 'Person created successfully', 'id': person.id}, 201

class AnswersResource(Resource):
  def get(self):
    persons = db.session.query(
      Person.id,
      Person.age,
      Person.sex,
      Person.marital_id,
      Maritals.marital,
      Person.education_id,
      Educations.education,
      Person.roommates,
      Person.is_hired
    ).join(Maritals, Person.marital_id == Maritals.id).join(Educations, Person.education_id == Educations.id).all()

    results = []

    for person in persons:
      answers = db.session.query(
        Answers.question_id,
        Questions.question,
        Answers.answer
      ).join(Questions, Questions.id == Answers.question_id).filter(Answers.person_id == person.id).all()
      answers_list = [{
        'question_id': a.question_id,
        'question': a.question,
        'answer': a.answer
      } for a in answers]

      results.append({
        'id': person.id,
        'age': person.age,
        'sex': person.sex,
        'marital_id': person.marital_id,
        'marital': person.marital,
        'education_id': person.education_id,
        'education': person.education,
        'roommates': person.roommates,
        'is_hired': 'TAK' if person.is_hired else 'NIE',
        'answers': answers_list
      })

    return results, 200

  def post(self):
    json_args = reqparse.RequestParser()
    json_args.add_argument('person_id', type=int, required=True)
    json_args.add_argument('question_id', type=int, required=True)
    json_args.add_argument('answer', type=int, required=True)
    args = json_args.parse_args()

    answer = Answers(person_id=args['person_id'], question_id=args['question_id'], answer=args['answer'])
    db.session.add(answer)
    db.session.commit()
    return {'message': 'Answer added successfully'}, 201


api.add_resource(EducationsResource, '/educations')
api.add_resource(MaritalsResource, '/maritals')
api.add_resource(QuestionsResource, '/questions')
api.add_resource(PersonResource, '/person')
api.add_resource(AnswersResource, '/answer')

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')