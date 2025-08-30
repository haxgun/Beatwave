<script setup lang="ts">
import { DarkVeil } from '@/components/ui/background'
import { Button } from '@/components/ui/button'
import { moveTo } from '@/lib/utils'
import { ArrowRight } from 'lucide-vue-next'
import { useI18n } from 'vue-i18n'

import { useRouter } from 'vue-router'

const router = useRouter()

const { t } = useI18n()
</script>

<template>
  <DarkVeil
    :hue-shift="54"
    :noise-intensity="0"
    :scanline-intensity="0"
    :speed="0.5"
    :scanline-frequency="0"
    :warp-amount="0"
    :resolution-scale="1"
    as="main"
    class="flex relative h-dvh w-dvw overflow-hidden bg-black/80"
  >
    <section class="absolute inset-0 m-auto flex h-full flex-col justify-center container gap-4">
      <div class="z-20 flex flex-col items-center justify-center gap-5">
        <span class="relative text-4xl font-bold"> Beatwave </span>
        <span class="text-6xl italic font-extrabold whitespace-pre-wrap text-center">
          {{ t('home-page.hero.title') }}
        </span>
        <span class="font-light text-xl text-center whitespace-pre-wrap">
          {{ t('home-page.hero.description') }}
        </span>
        <div class="mt-4 inline-flex gap-5">
          <Button @click="router.push({ name: 'auth' })" class="text-md" size="lg">
            {{ t('home-page.hero.buttons.start') }}
          </Button>
          <Button @click="moveTo('features')" class="text-md" size="lg" variant="secondary">
            {{ t('home-page.hero.buttons.features') }}
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
</template>
