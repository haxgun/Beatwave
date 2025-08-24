<script setup lang="ts">
import Header from '@/components/default-layout/Header.vue'
</script>

<template>
  <div class="w-full flex flex-col">
    <Header />
    <slot />
  </div>
</template>
