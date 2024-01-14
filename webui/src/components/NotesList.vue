<template>
  <div class="notes-list-container">
    <h2>Your Notes</h2>
    <div v-if="loading">Loading your notes, one moment please...</div>
    <div v-if="error">
      There was an error loading your notes. Check browser console for more details.
    </div>
    <div v-if="loaded" class="note-list-container">
      <div v-for="note of noteStore.allNotes" class="note-item">
        <router-link :to="`/notes/${note.note_id}`">
          <h3>{{ note.name }}</h3>
        </router-link>
        <p>Modified {{ note.modified_dt }}</p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { listAllNotes } from '@/api';
import { useNoteStore } from '@/stores/notesStore';
import { onMounted, ref } from 'vue';

const loaded = ref(false);
const loading = ref(false);
const error = ref(false);
const noteStore = useNoteStore();

onMounted(() => {
  loading.value = true;
  listAllNotes()
    .then((response) => {
      noteStore.allNotes = response;
      loaded.value = true;
    })
    .catch((error) => {
      console.error(error);
      error.value = true;
    })
    .finally(() => (loading.value = false));
});
</script>

<style lang="scss">
.note-list-container {
  & > * {
    margin-bottom: 1rem;
    &:last-child {
      margin-bottom: 0;
    }
  }
  .note-item {
    border: 1px solid grey;
    border-radius: 5px;
    padding: 1rem;
  }
}
</style>
