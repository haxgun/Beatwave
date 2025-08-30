<script setup lang="ts">
import { Footer, Header2 } from '@/components/default-layout'
</script>

<template>
  <div class="w-full flex flex-col">
    <Header2 />
    <slot />
    <Footer />
  </div>
</template>
