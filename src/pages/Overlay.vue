<template>
  <Overlay
    v-if="accessToken"
    :showAlbumArt="showAlbumArt"
    :showArtist="showArtist"
    :showBackground="showBackground"
    :colorBG="colorBG"
    :showSpotifyLogo="showSpotifyLogo"
    :showMaxWidth="showMaxWidth"
    :accessToken="accessToken"
  />
</template>

<script>
import Overlay from '@/components/Overlay.vue'

export default {
  components: { Overlay },

  data: () => ({
    showAlbumArt: true,
    showArtist: true,
    showBackground: true,
    showSpotifyLogo: true,
    showMaxWidth: true,
    colorBG: '000000',
    accessToken: null
  }),

  mounted() {
    const {
      accessToken,
      colorBG,
      showAlbumArt,
      showArtist,
      showBackground,
      showMaxWidth,
      showSpotifyLogo
    } = this.$route.query

    this.showAlbumArt = JSON.parse(showAlbumArt)
    this.showArtist = JSON.parse(showArtist)
    this.showBackground = JSON.parse(showBackground)
    this.showSpotifyLogo = JSON.parse(showSpotifyLogo)
    this.showMaxWidth = JSON.parse(showMaxWidth)
    this.colorBG = colorBG
    this.accessToken = accessToken
  }
}
</script>

<style>
:root {
  background: none !important;
}
</style>
