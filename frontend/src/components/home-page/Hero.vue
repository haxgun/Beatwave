<script setup lang="ts">
import { DarkVeil } from '@/components/ui/background'
import { Button } from '@/components/ui/button'
import { ArrowRight } from 'lucide-vue-next'

import { useRouter } from 'vue-router'

const router = useRouter()
</script>

<template>
  <main class="relative h-dvh w-dvw overflow-hidden bg-black/80">
    <DarkVeil
      :hue-shift="54"
      :noise-intensity="0"
      :scanline-intensity="0"
      :speed="0.5"
      :scanline-frequency="0"
      :warp-amount="0"
      :resolution-scale="1"
    >
      <section class="absolute inset-0 m-auto flex h-full flex-col justify-center container gap-4">
        <div class="z-20 flex flex-col items-center justify-center gap-5">
          <span class="relative text-4xl font-bold"> Beatwave </span>
          <span class="text-6xl italic font-extrabold">Share Your Music Taste </span>
          <span class="font-light text-xl text-center">
            Elegant, customizable widgets that broadcast<br />
            your tracks in real time — matching your style,<br />
            and letting viewers see what’s playing right now</span
          >
          <div class="mt-4 inline-flex gap-5">
            <Button @click="router.push({ name: 'auth' })" class="text-md" size="lg">
              Get started now
            </Button>
            <Button
              @click="router.push({ name: 'auth' })"
              class="text-md"
              size="lg"
              variant="secondary"
            >
              Discover features
              <ArrowRight class="size-4" />
            </Button>
          </div>
          <!-- <div class="text-xs text-neutral-500 flex flex-col gap-1">
          <span>Completely free.</span>
          <span>We do not store any information.</span>
          <span>All processing happens inside your browser.</span>
        </div> -->
        </div>
      </section>
    </DarkVeil>
  </main>
</template>
