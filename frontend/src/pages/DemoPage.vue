<script setup lang="ts">
import { AnimatedGradientBackground } from '@/components/ui/background'
import { ColorPicker } from '@/components/ui/color-picker'
import { Input } from '@/components/ui/input'

import { ref } from 'vue'

const color = ref('#8a5c5c')
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
      <div class="flex flex-row items-center justify-center">
        <ColorPicker v-model="color" />
        <Input v-model="color" />
      </div>
    </div>
  </div>
</template>
