<script setup lang="ts">
import { Logotype } from '@/components'
import { BoltIcon, PaintbrushIcon } from 'lucide-vue-next'
</script>

<template>
  <section class="container flex items-center justify-center">
    <div class="inline-flex gap-3">
      <div class="flex flex-col gap-3">
        <div
          class="rounded-4xl flex flex-col gap-5 bg-linear-65 from-[#021416] via-[#007469] to-[#007565] text-white p-7.5"
        >
          <Logotype :size="48" />
          <span class="text-2xl font-semibold">Выбирая нас, ты выбираешь будущее!</span>
        </div>
        <div class="rounded-4xl flex flex-col gap-3 bg-neutral-500 text-black p-7.5">
          <span class="inline-flex items-center gap-1">
            <BoltIcon class="size-4" />
            <span class="text-xs font-medium">Simple setup</span>
          </span>
          <span class="text-2xl font-semibold">
            Easy integration into OBS,<br />
            Streamlabs Desktop, XSplit and more.
          </span>
        </div>
      </div>
      <div class="flex flex-col gap-3">
        <div class="inline-flex gap-3">
          <div class="text-xl font-semibold rounded-4xl bg-neutral-500 text-black p-7.5">
            Zero Delay
          </div>
          <div class="text-xl font-semibold rounded-4xl bg-neutral-500 text-black p-7.5">
            Spotify Canvas
          </div>
        </div>
        <div class="flex flex-col gap-3 rounded-4xl bg-neutral-500 text-black p-7.5">
          <span class="inline-flex items-center gap-1">
            <PaintbrushIcon class="size-4" />
            <span class="text-xs font-medium">Style it up!</span>
          </span>
          <span class="text-2xl font-semibold">
            Style your player to suit your <br />
            streaming style and aesthetic.
          </span>
        </div>
      </div>
    </div>
  </section>
</template>

<style lang="css" scoped></style>
>
