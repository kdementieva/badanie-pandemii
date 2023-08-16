<template>
  <h2 class="mt-3 mb-5">Część 1 - Pytania klasyfikacyjne</h2>
  <v-form @submit.prevent="add_person()">
    <v-text-field
    v-model="person.age"
    type="number"
    label="Pytanie 1: Podaj swój wiek" :rules="rules"
    class="mb-5" />

    <v-select
    v-model="person.sex"
    :items="sex_options"
    item-title="text"
    item-value="value"
    label="Pytanie 2: Wybierz swoją płeć"
    :rules="rules"
    class="mb-5" />

    <v-select
    v-model="person.marital"
    :items="marital_options"
    item-title="marital"
    item-value="id"
    label="Pytanie 3: Wybierz swój stan cywilny"
    :rules="rules"
    class="mb-5" />

    <v-select
    v-model="person.education"
    :items="education_options"
    item-title="education"
    item-value="id"
    label="Pytanie 4: Wybierz swoje wykształcenie"
    :rules="rules"
    class="mb-5" />

   <v-text-field
    v-model="person.roommates"
    type="number"
    label="Pytanie 5: Ilość współlokatorów"
    :rules="rules"
    class="mb-5" />

    <p class="mb-3">Pytanie 6: Czy jesteś zatrudniony/a?</p>
    <v-radio-group v-model="person.is_hired" :rules="rules">
      <v-radio label="Tak" value="1" />
      <v-radio label="Nie" value="0" />
    </v-radio-group>

    <v-btn
    type="submit"
    class="mt-2"
    color="blue-darken-4">Dalej</v-btn>
  </v-form>
</template>

<script>
import axios from 'axios'

export default {
  emits: ['person_id'],
  data() {
    return {
      person: {
        age: null,
        sex: null,
        marital: null,
        education: null,
        roommates: null,
        is_hired: null
      },
      sex_options: [
        { value: 'M', text: 'Mężczyzna' },
        { value: 'K', text: 'Kobieta' }
      ],
      marital_options: [],
      education_options: [],
      rules: [
        (v) => !!v || 'To pole jest wymagane'
      ]
    }
  },
  async created() {
    await axios.get('http://localhost:5000/maritals').then(res => {
      this.marital_options = res.data
    })
    await axios.get('http://localhost:5000/educations').then(res => {
      this.education_options = res.data
    })
  },
  methods: {
    add_person() {
      for(const field in this.person)
        if(this.person[field] == null)
          return

      axios.post('http://localhost:5000/person', {
        age: this.person.age,
        sex: this.person.sex,
        marital_id: this.person.marital,
        education_id: this.person.education,
        roommates: this.person.roommates,
        is_hired: parseInt(this.person.is_hired)
      }).then(res => {
        this.$emit('person_id', res.data.id)
        this.person.age = null
        this.person.sex = null
        this.person.marital = null
        this.person.education = null
        this.person.roommates = null
        this.person.is_hired = null
      })
    }
  }
}
</script>