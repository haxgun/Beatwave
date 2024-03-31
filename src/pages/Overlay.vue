<template>
  <Overlay
    v-if="accessToken"
    :showMaxWidth="showMaxWidth"
    :accessToken="accessToken"
    :showBorder="showBorder"
    :trimArtist="trimArtist"
    :bgOpacity="bgOpacity"
    :borderSize="borderSize"
  />
</template>

<script>
import Overlay from '@/components/Overlay.vue'

export default {
  components: { Overlay },

  data: () => ({
    showMaxWidth: true,
    accessToken: null
  }),

  mounted() {
    const {
      accessToken,
      showMaxWidth,
      showBorder,
      trimArtist,
      bgOpacity,
      borderSize
    } = this.$route.query

    this.showMaxWidth = JSON.parse(showMaxWidth)
    this.showBorder = JSON.parse(showBorder)
    this.trimArtist = JSON.parse(trimArtist)
    this.bgOpacity = JSON.parse(bgOpacity)
    this.borderSize = JSON.parse(borderSize)
    this.accessToken = accessToken
  }
}
</script>

<style>
:root {
  background: none !important;
}
</style>
