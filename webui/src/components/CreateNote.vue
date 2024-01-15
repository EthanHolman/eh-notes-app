<template>
  <div class="create-note-container">
    <h2 class="p-b1">Create New Note</h2>
    <p v-if="isError">Error creating note</p>
    <input v-model="noteTitle" type="text" placeholder="Note Title" />
    <button @click="submitNote">Create</button>
  </div>
</template>

<script setup lang="ts">
import { createNewNote } from '@/api';
import { useNoteStore } from '@/stores/notesStore';
import type { NoteSummary } from '@/types';
import { ref } from 'vue';

const emit = defineEmits<{ onNewNoteCreated: [note: NoteSummary] }>();

const notesStore = useNoteStore();

const noteTitle = ref('');
const isError = ref(false);
const isSaving = ref(false);

function submitNote() {
  isSaving.value = true;
  createNewNote(noteTitle.value)
    .then((res) => {
      notesStore.addNote(res);
    })
    .catch((error) => {
      console.error(error);
      isError.value = true;
    })
    .finally(() => (isSaving.value = false));
}
</script>

<style scoped lang="scss"></style>
