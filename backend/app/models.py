from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Educations(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  education = db.Column(db.String(100))

class Maritals(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  marital = db.Column(db.String(100))

class Person(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  age = db.Column(db.Integer)
  sex = db.Column(db.Enum('M', 'K'))
  marital_id = db.Column(db.Integer, db.ForeignKey('maritals.id'))
  marital = db.relationship('Maritals', backref='maritals')
  education_id = db.Column(db.Integer, db.ForeignKey('educations.id'))
  education = db.relationship('Educations', backref='educations')
  roommates = db.Column(db.Integer)
  is_hired = db.Column(db.Boolean)

class Questions(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  question = db.Column(db.String(200))
  answer_type = db.Column(db.Enum('scale', 'bool'))

class Answers(db.Model):
  person_id = db.Column(db.Integer, db.ForeignKey('person.id'), primary_key=True)
  person = db.relationship('Person', backref='persons')
  question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), primary_key=True)
  question = db.relationship('Questions', backref='questions')
  answer = db.Column(db.Integer)