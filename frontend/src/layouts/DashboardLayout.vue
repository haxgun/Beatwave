<script setup lang="ts">
import Header from '@/components/dashboard-layout/Header.vue'
</script>

<template>
  <div class="w-dvw h-dvh flex flex-col bg-[url('/dashboard/background.jpg')] bg-cover bg-center">
    <Header />
    <slot />
  </div>
</template>
