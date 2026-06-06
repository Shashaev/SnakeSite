<script setup>
  import { RouterLink, RouterView } from 'vue-router'
  import HeaderCom from './components/Header.vue'
  import FooterCom from './components/Footer.vue'
</script>

<template>
  <HeaderCom />
  <RouterView v-slot="{ Component }">
    <transition name="fade" mode="out-in">
      <component :is="Component" />
    </transition>
  </RouterView>
  <FooterCom />
</template>

<style>
  .fade-enter-active,
  .fade-leave-active {
    transition: opacity 0.4s ease;
  }
  .fade-enter-from,
  .fade-leave-to {
    opacity: 0;
  }

  @font-face {
      font-family: 'MyFont';
      src: 
          url('/Roboto/Roboto-Italic-VariableFont_wdth\,wght.ttf') format('ttf'),
          url('/Roboto/Roboto-VariableFont_wdth\,wght.ttf') format('ttf');
      font-weight: 400;
      font-style: normal;
  }

  html {
    scrollbar-width: none;
  }

  .main {
      min-height: 100vh;
  }

  body {
    margin: 0px;
    padding: 0px;
    color: #000000;
    font-family: 'MyFont', sans-serif;
    overflow-x: hidden;
  }

  a {
    color: aliceblue;
    text-decoration: none;
  }
</style>
