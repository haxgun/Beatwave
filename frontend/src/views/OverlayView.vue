<script setup>
import OverlayItem from '@/components/OverlayItem.vue'
import { onMounted, ref } from 'vue'

const showMaxWidth = ref(true)
const showBorder = ref(false)
const trimArtist = ref(false)
const bgOpacity = ref(60)
const borderSize = ref(3)
const accessToken = ref(null)

onMounted(() => {
  const {
    accessToken: token,
    showMaxWidth: maxWidth,
    showBorder,
    trimArtist,
    bgOpacity,
    borderSize
  } = useRoute().query

  showMaxWidth.value = JSON.parse(maxWidth)
  showBorder.value = JSON.parse(showBorder)
  trimArtist.value = JSON.parse(trimArtist)
  bgOpacity.value = JSON.parse(bgOpacity)
  borderSize.value = JSON.parse(borderSize)
  accessToken.value = token
})
</script>

<template>
  <OverlayItem
    v-if="accessToken"
    :showMaxWidth="showMaxWidth"
    :accessToken="accessToken"
    :showBorder="showBorder"
    :trimArtist="trimArtist"
    :bgOpacity="bgOpacity"
    :borderSize="borderSize"
  />
</template>

<style>
:root {
  background: none !important;
}
</style>
