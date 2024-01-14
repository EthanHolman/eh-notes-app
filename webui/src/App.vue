<script setup lang="ts">
import { RouterView } from 'vue-router';
import AppHeader from './components/AppHeader.vue';
import NoteSidebar from './components/NoteSidebar.vue';
</script>

<template>
  <AppHeader />
  <div class="layout">
    <NoteSidebar />
    <RouterView />
  </div>
</template>

<style scoped lang="scss">
.layout {
  display: flex;
  flex-direction: row;
  overflow: hidden;
  flex: 1;
}
</style>

<style lang="scss">
#app {
  display: flex;
  flex-direction: column;
  height: 100%;
}
</style>
