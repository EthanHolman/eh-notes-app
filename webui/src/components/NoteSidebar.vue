<template>
  <div class="notes-sidebar-container">
    <CreateNote />
    <NotesList />
    <router-link to="/about">About This App</router-link>
  </div>
</template>

<script setup lang="ts">
import NotesList from './NotesList.vue';
import CreateNote from './CreateNote.vue';
</script>

<style scoped lang="scss">
.notes-sidebar-container {
  overflow: auto;
  padding: 1rem;
  background-color: #eee;

  & > * {
    margin-bottom: 1rem;

    &:last-child {
      margin-bottom: 0;
    }
  }
}
</style>
