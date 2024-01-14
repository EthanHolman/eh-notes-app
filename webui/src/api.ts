import axios from 'axios';
import { API_BASE_URL } from './globals';
import type { Note, NoteSummary } from './types';

export function listAllNotes(): Promise<NoteSummary[]> {
  return axios.get(`${API_BASE_URL}/notes`).then((x) => x.data);
}

export function createNewNote(name: string) {
  return axios.post(`${API_BASE_URL}/notes`, { name }).then((x) => x.data);
}

export function getNote(noteId: number): Promise<Note> {
  return axios.get(`${API_BASE_URL}/notes/${noteId}`).then((x) => x.data);
}

export function updateNote(noteId: number, body: string) {
  return axios.patch(`${API_BASE_URL}/notes/${noteId}`, { body });
}
