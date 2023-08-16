<template>
  <v-container
  fluid
  class="h-screen bg-grey-lighten-4 p-auto">
    <div class="container-width mx-auto">
      <h1>Ankieta dot. zmiany nastrojów podczas kwarantanny</h1>
      <router-view />
    </div>
  </v-container>
</template>

<style>
html {
  overflow: auto !important;
}
.container-width {
  width: 90%;
}
</style>