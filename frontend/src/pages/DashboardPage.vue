<script setup lang="ts">
import Configuration from '@/components/dashboard-page/Configuration.vue'
import DefaultOverlay from '@/components/overlays/DefaultOverlay.vue'
import DashboardLayout from '@/layouts/DashboardLayout.vue'

import { useOverlayStore } from '@/stores'
import { storeToRefs } from 'pinia'

const overlayStore = useOverlayStore()
const {
  bgColor,
  avgCoverColor,
  textColor,
  widthLimitation,
  showBorder,
  borderColor,
  borderRadius,
  textFont,
  trimArtist,
} = storeToRefs(overlayStore)
</script>

<template>
  <DashboardLayout>
    <div class="inline-flex size-full">
      <div class="flex-1 h-full flex items-center justify-center relative overflow-hidden">
        <DefaultOverlay
          :backgroundColor="bgColor"
          :avgCoverColor="avgCoverColor"
          :showBorder="showBorder"
          :borderColor="borderColor"
          :borderRadius="borderRadius"
          :textColor="textColor"
          :textFont="textFont"
          :trimArtist="trimArtist"
        />
      </div>
      <Configuration />
    </div>
  </DashboardLayout>
</template>
