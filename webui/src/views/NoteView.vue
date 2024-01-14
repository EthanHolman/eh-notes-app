<template>
  <div class="note-view-container">
    <header>
      <h1 class="title">Note: {{ notesStore.currentNoteData?.name }}</h1>
      <button @click="saveChanges">Save Changes</button>
    </header>
    <div v-if="loading">Loading Note...</div>
    <div v-if="error">Error loading note. See browser console for more details</div>
    <textarea v-model="noteBody" placeholder="Your Note Here" class="text-editor"></textarea>
  </div>
</template>

<script setup lang="ts">
import { getNote, updateNote } from '@/api';
import { useNoteStore } from '@/stores/notesStore';
import { onMounted, ref, watch } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();

const loading = ref(false);
const loaded = ref(false);
const error = ref(false);
const noteBody = ref('');
const notesStore = useNoteStore();

onMounted(() => {
  loadNote();
});

watch(
  () => route.params,
  () => {
    loadNote();
  }
);

function loadNote() {
  loading.value = true;
  const routeNoteId = parseInt(route.params['noteId'] as any);
  if (routeNoteId && routeNoteId > -1) {
    notesStore.setCurrentNote(routeNoteId);

    getNote(routeNoteId)
      .then((response) => {
        noteBody.value = response.body;
        loaded.value = true;
      })
      .catch((error) => {
        error.value = true;
      })
      .finally(() => (loading.value = false));
  }
}

function saveChanges() {
  updateNote(notesStore.currentNoteId!, noteBody.value).then(() => {
    alert('Note updated!');
  });
}
</script>

<style scoped lang="scss">
.note-view-container {
  padding: 1rem;
  flex: 1;
  display: flex;
  flex-direction: column;

  & > header {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    margin-bottom: 1rem;
  }

  .text-editor {
    width: 100%;
    height: 100%;
    padding: 1rem;
    border: 1px solid #ddd;
    border-radius: 5px;
    font-size: 1rem;
  }
}
</style>
