import { createRouter, createWebHistory } from 'vue-router';
import HomeView from './views/HomeView.vue';
import NoteView from './views/NoteView.vue';
import AboutView from './views/AboutView.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/notes/:noteId',
      name: 'noteview',
      component: NoteView
    },
    {
      path: '/about',
      name: 'aboutview',
      component: AboutView
    }
  ]
});

export default router;
