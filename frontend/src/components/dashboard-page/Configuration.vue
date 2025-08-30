<script setup lang="ts">
import { ColorPicker, SelectFont } from '@/components/ui'
import { Slider } from '@/components/ui/slider'
import { SwitchToggle } from '@/components/ui/switch-toggle'

import { useOverlayStore } from '@/stores'
import { storeToRefs } from 'pinia'
import { useI18n } from 'vue-i18n'

const overlayStore = useOverlayStore()
const {
  bgColor,
  avgCoverColor,
  textColor,
  widthLimitation,
  showBorder,
  borderColor,
  textFont,
  trimArtist,
} = storeToRefs(overlayStore)

const { t } = useI18n()
</script>

<template>
  <div class="w-[360px] h-full bg-black/95 backdrop-blur-lg border-l border-white/10 p-6">
    <div class="flex flex-col gap-5">
      <div class="flex flex-col gap-1">
        <span class="text-md font-medium">{{ t('dashboard-page.configuration.title') }}</span>
        <span class="text-sm text-neutral-600">
          {{ t('dashboard-page.configuration.description') }}
        </span>
      </div>
      <div class="flex flex-col gap-2">
        <span class="text-xs uppercase text-neutral-700 font-medium">
          {{ t('dashboard-page.configuration.blocks.background.title') }}
        </span>
        <div class="inline-flex items-center justify-between w-full">
          <span class="text-sm w-1/2">
            {{ t('dashboard-page.configuration.blocks.background.features.color') }}
          </span>
          <ColorPicker v-model="bgColor" />
        </div>
        <div class="inline-flex items-center justify-between w-full">
          <span class="text-sm w-1/2">
            {{ t('dashboard-page.configuration.blocks.background.features.avg-cover-color') }}
          </span>
          <SwitchToggle v-model="avgCoverColor" />
        </div>
        <div class="inline-flex items-center justify-between w-full">
          <span class="text-sm w-1/2">
            {{ t('dashboard-page.configuration.blocks.background.features.opacity') }}
          </span>
          <Slider :default-value="[100]" :max="100" :step="1" />
        </div>
        <div class="inline-flex items-center justify-between w-full">
          <span class="text-sm w-1/2">
            {{ t('dashboard-page.configuration.blocks.background.features.width-limitation') }}
          </span>
          <SwitchToggle v-model="widthLimitation" />
        </div>
      </div>

      <div class="flex flex-col gap-2">
        <span class="text-xs uppercase text-neutral-700 font-medium">
          {{ t('dashboard-page.configuration.blocks.border.title') }}
        </span>
        <div class="inline-flex items-center justify-between w-full">
          <span class="text-sm w-1/2">
            {{ t('dashboard-page.configuration.blocks.border.features.color') }}
          </span>
          <ColorPicker v-model="borderColor" />
        </div>
        <div class="inline-flex items-center justify-between w-full">
          <span class="text-sm w-1/2">
            {{ t('dashboard-page.configuration.blocks.border.features.show') }}
          </span>
          <SwitchToggle v-model="showBorder" />
        </div>
        <div class="inline-flex items-center justify-between w-full">
          <span class="text-sm w-1/2">
            {{ t('dashboard-page.configuration.blocks.border.features.radius') }}
          </span>
          <Slider :default-value="[100]" :max="3" :step="1" />
        </div>
      </div>

      <div class="flex flex-col gap-2">
        <span class="text-xs uppercase text-neutral-700 font-medium">
          {{ t('dashboard-page.configuration.blocks.text.title') }}
        </span>
        <div class="inline-flex items-center justify-between w-full">
          <span class="text-sm w-1/2">
            {{ t('dashboard-page.configuration.blocks.text.features.color') }}
          </span>
          <ColorPicker v-model="textColor" />
        </div>
        <div class="inline-flex items-center justify-between w-full">
          <span class="text-sm w-1/2">
            {{ t('dashboard-page.configuration.blocks.text.features.font') }}
          </span>
          <SelectFont v-model="textFont" />
        </div>
      </div>

      <div class="flex flex-col gap-2">
        <span class="text-xs uppercase text-neutral-700 font-medium">
          {{ t('dashboard-page.configuration.blocks.other.title') }}
        </span>
        <div class="inline-flex items-center justify-between w-full">
          <span class="text-sm w-1/2">
            {{ t('dashboard-page.configuration.blocks.other.features.trim-artist') }}
          </span>
          <SwitchToggle v-model="trimArtist" />
        </div>
      </div>
    </div>
  </div>
</template>
