<script setup lang="ts">
import { ColorPicker, SelectFont } from '@/components/ui/'
import { Slider } from '@/components/ui/slider'
import { SwitchToggle } from '@/components/ui/switch-toggle'
import { ref } from 'vue'

const bgColor = ref('#ffffff')
const avgCoverColor = ref(false)
const textColor = ref('#ffffff')
const widthLimitation = ref(false)
const showBorder = ref(false)
const borderColor = ref('#ffffff')
const textFont = ref('Geist')
const trimArtist = ref(false)

const toggleWidthLimitation = () => {
  widthLimitation.value = !widthLimitation.value
}

const toggleShowBorder = () => {
  showBorder.value = !showBorder.value
}

const toggleTrimArtist = () => {
  trimArtist.value = !trimArtist.value
}
const toggleAvgCoverColor = () => {
  avgCoverColor.value = !avgCoverColor.value
}
</script>

<template>
  <div class="w-[360px] h-full bg-black/95 backdrop-blur-lg border-l border-white/10 p-6">
    <div class="flex flex-col gap-5">
      <div class="flex flex-col gap-1">
        <span class="text-lg font-medium">Configuration</span>
        <span class="text-sm text-neutral-600">
          Customize the appearance of the music display. Customize everything to your liking.
        </span>
      </div>
      <div class="flex flex-col gap-2">
        <span class="text-xs uppercase text-neutral-700 font-medium font-mono">Background</span>
        <div class="inline-flex items-center justify-between w-full">
          <span class="text-sm w-1/2">Color</span>
          <ColorPicker v-model="bgColor" />
        </div>
        <div class="inline-flex items-center justify-between w-full">
          <span class="text-sm w-1/2"
            >Avg cover color {{ avgCoverColor ? 'enabled' : 'disabled' }}</span
          >
          <SwitchToggle v-model="avgCoverColor" />
        </div>
        <div class="inline-flex items-center justify-between w-full">
          <span class="text-sm w-1/2">Opacity</span>
          <Slider :default-value="[100]" :max="100" :step="1" />
        </div>
        <div class="inline-flex items-center justify-between w-full">
          <span class="text-sm w-1/2">Width limitation</span>
          <SwitchToggle :checked="widthLimitation" @update:checked="toggleWidthLimitation" />
        </div>
      </div>

      <div class="flex flex-col gap-2">
        <span class="text-xs uppercase text-neutral-700 font-medium font-mono">Border</span>
        <div class="inline-flex items-center justify-between w-full">
          <span class="text-sm w-1/2">Color</span>
          <ColorPicker v-model="borderColor" />
        </div>
        <div class="inline-flex items-center justify-between w-full">
          <span class="text-sm w-1/2">Show</span>
          <SwitchToggle :checked="showBorder" @update:checked="toggleShowBorder" />
        </div>
        <div class="inline-flex items-center justify-between w-full">
          <span class="text-sm w-1/2">Radius</span>
          <Slider :default-value="[100]" :max="3" :step="1" />
        </div>
      </div>

      <div class="flex flex-col gap-2">
        <span class="text-xs uppercase text-neutral-700 font-medium font-mono">Text</span>
        <div class="inline-flex items-center justify-between w-full">
          <span class="text-sm w-1/2">Color</span>
          <ColorPicker v-model="textColor" />
        </div>
        <div class="inline-flex items-center justify-between w-full">
          <span class="text-sm w-1/2">Font</span>
          <SelectFont v-model="textFont" />
        </div>
      </div>

      <div class="flex flex-col gap-2">
        <span class="text-xs uppercase text-neutral-700 font-medium font-mono">Other</span>
        <div class="inline-flex items-center justify-between w-full">
          <span class="text-sm w-1/2">Trim artist</span>
          <SwitchToggle :checked="trimArtist" @update:checked="toggleTrimArtist" />
        </div>
      </div>
    </div>
  </div>
</template>
