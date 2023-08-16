<template>
  <PersonalQuestions
  v-if="person_id == null"
  @person_id="(i) => person_id = i" />
  <SubstantiveQuestions
  v-else="person_id == null"
  :person_id="person_id"
  @success="(i) => show_success = i"
  @clear_person="(i) => person_id = i" />

  <v-snackbar
  v-model="show_success"
  color="success"
  transition="fade-transition"
  timeout="2000">
    Dziękujemy za udział w ankiecie
    <template v-slot:actions>
      <v-btn
      color="red-darken-4"
      variant="text"
      @click="show_success = false">
        Zamknij
      </v-btn>
    </template>
  </v-snackbar>
</template>

<script>
import PersonalQuestions from '@/views/PersonalQuestions'
import SubstantiveQuestions from '@/views/SubstantiveQuestions'

export default {
  components: {
    PersonalQuestions,
    SubstantiveQuestions
  },
  data() {
    return {
      person_id: null,
      show_success: false
    }
  }
}
</script>