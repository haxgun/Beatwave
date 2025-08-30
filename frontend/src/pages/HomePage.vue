<script setup lang="ts">
import { Features, Hero } from '@/components/home-page'
import DefaultLayout from '@/layouts/DefaultLayout.vue'
</script>

<template>
  <DefaultLayout>
    <Hero />
    <Features />
  </DefaultLayout>
</template>
