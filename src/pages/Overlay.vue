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
      showAlbumArt,
      showArtist,
      showBackground,
      showSpotifyLogo,
      showMaxWidth,
      colorBG,
      accessToken
    } = this.$route.query
    this.showAlbumArt = Boolean(showAlbumArt)
    this.showArtist = Boolean(showArtist)
    this.showBackground = Boolean(showBackground)
    this.showSpotifyLogo = Boolean(showSpotifyLogo)
    this.showMaxWidth = Boolean(showMaxWidth)
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
