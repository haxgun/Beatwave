<script setup lang="ts">
import AnimatedGradientBackground from '@/components/ui/AnimatedGradientBackground.vue'
</script>

<template>
  <div class="relative w-full h-screen overflow-hidden">
    <AnimatedGradientBackground />
    <div
      class="relative z-10 flex flex-col items-center justify-start h-full px-4 pt-32 text-center"
    >
      <p class="mt-4 text-lg text-gray-300 md:text-xl max-w-lg">
        A customizable animated radial gradient background with a subtle breathing effect.
      </p>
    </div>
  </div>
</template>
