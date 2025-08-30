<script setup lang="ts">
import { Footer, Header } from '@/components/default-layout'
</script>

<template>
  <div class="w-full flex flex-col">
    <Header />
    <slot />
    <Footer />
  </div>
</template>
