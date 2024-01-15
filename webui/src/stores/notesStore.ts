import type { Note, NoteSummary } from '@/types';
import { defineStore } from 'pinia';
import { computed, ref } from 'vue';

export const useNoteStore = defineStore('notes', () => {
  const allNotes = ref<NoteSummary[]>([]);
  const currentNoteId = ref<number | undefined>();

  const currentNoteData = computed(() =>
    allNotes.value.find((x) => x.note_id === currentNoteId.value)
  );

  function setAllNotes(newVal: NoteSummary[]) {
    allNotes.value = newVal;
  }

  function setCurrentNote(noteId: number) {
    currentNoteId.value = noteId;
  }

  function addNote({ body, ...note }: Note) {
    allNotes.value.splice(0, 0, note);
    currentNoteId.value = note.note_id;
  }

  return { allNotes, setAllNotes, setCurrentNote, currentNoteData, currentNoteId, addNote };
});
