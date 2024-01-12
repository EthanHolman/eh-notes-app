<template>
  <h2>Your Notes</h2>
  <div class="note-list-container">
    <div v-for="note of notes" class="note-item">
      <h3>{{ note.name }}</h3>
      <p>Modified {{ note.modifiedDt.toLocaleDateString() }}</p>
    </div>
    <div>I am another note</div>
  </div>
</template>

<script setup lang="ts">
import type { Note } from '@/types';
import { ref } from 'vue';

const notes = ref<Note[]>([
  { name: 'Passwords', createdDt: new Date(), modifiedDt: new Date() },
  { name: 'Stolen Identities', createdDt: new Date(), modifiedDt: new Date() }
]);
</script>

<style lang="scss">
.note-list-container {
  & > div {
    border: 1px solid grey;
    padding: 1rem;
  }
}
</style>
