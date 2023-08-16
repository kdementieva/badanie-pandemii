<template>
  <h2 class="mt-3 mb-5">Część 2 - Pytania merytoryczne</h2>
  <v-form @submit.prevent="add_answers">
    <div
    v-for="(question, index) in questions"
    :key="question.id"
    class="mt-2">
      <p class="mb-5">
        {{ `Pytanie ${index + 1}: ${question.question}` }}
      </p>

      <v-slider
      v-model="answers[index]"
      :min="0"
      :max="10"
      :step="1"
      thumb-label
      :rules="rules"
      v-if="question.answer_type == 'scale'" />

      <v-radio-group
      v-model="answers[index]"
      :rules="rules"
      v-if="question.answer_type == 'bool'">
        <v-radio label="Tak" value="1" />
        <v-radio label="Nie" value="0" />
      </v-radio-group>
    </div>
    <v-btn
    type="submit"
    class="mt-2 mb-2"
    color="blue-darken-4">Prześlij</v-btn>

  </v-form>
</template>

<script>
import axios from 'axios'

export default {
  emits: ['success', 'clear_person'],
  props: ['person_id'],
  data() {
    return {
      questions: [],
      answers: [],
      rules: [
        (v) => !!v || 'To pole jest wymagane'
      ]
    }
  },
  async created() {
    axios.get('http://localhost:5000/questions').then(res => this.questions = res.data)
  },
  methods: {
    add_answers() {
      this.questions.forEach((q, i) => {
        if(this.answers[i] == null)
          return
      })

      this.questions.forEach((q, i) => {
        axios.post('http://localhost:5000/answer', {
        person_id: this.person_id,
        question_id: q.id,
        answer: parseInt(this.answers[i]),
        }).then(res => {
          this.questions = []
          this.answers = []
          this.$emit('success', true)
          this.$emit('clear_person', null)
        })
      })


    }
  }
}
</script>