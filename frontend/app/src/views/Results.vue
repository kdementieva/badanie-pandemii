<template>
  <h3 class="my-3">Wyniki ankiety</h3>
  <v-data-table-virtual
    :headers="headers"
    :items="items"
    class="elevation-1"
    :height="table_height"
  >
  </v-data-table-virtual>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      table_height: 0,
      headers: [
        { title: 'Wiek', key: 'age' },
        { title: 'Płeć', key: 'sex' },
        { title: 'Stan cywilny', key: 'marital' },
        { title: 'Wykształcenie', key: 'education' },
        { title: 'Il. współlokatorów', key: 'roommates' },
        { title: 'Czy zatrudniony', key: 'is_hired' },
        { title: 'P1', key: 'q1' },
        { title: 'P2', key: 'q2' },
        { title: 'P3', key: 'q3' },
        { title: 'P4', key: 'q4' },
        { title: 'P5', key: 'q5' },
        { title: 'P6', key: 'q6' },
        { title: 'P7', key: 'q7' },
        { title: 'P8', key: 'q8' },
        { title: 'P9', key: 'q9' },
        { title: 'P10', key: 'q10' }
      ],
      items: []
    }
  },
  created() {
    axios.get('http://localhost:5000/answer').then(res => {
      res.data.forEach(el => {
        let item = {}
        item['age'] = el.age
        item['sex'] = el.sex
        item['marital'] = el.marital
        item['education'] = el.education
        item['roommates'] = el.roommates
        item['is_hired'] = el.is_hired

        el.answers.forEach((question, index) => {
          item[`q${index + 1}`] = question.answer
        })

        this.items.push(item)
      })
    })
  },
  mounted() {
    this.calculate_table_height()
    window.addEventListener('resize', this.calculate_table_height)
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.calculate_table_height)
  },
  methods: {
    calculate_table_height() {
      const window_height = window.innerHeight
      const table_height = window_height - 200
      this.table_height = table_height
    }
  }
}
</script>