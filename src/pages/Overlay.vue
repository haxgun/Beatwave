<template>
  <Overlay
    v-if="accessToken"
    :showAlbumArt="showAlbumArt"
    :showArtist="showArtist"
    :showBackground="showBackground"
    :colorBG="colorBG"
    :showSpotifyLogo="showSpotifyLogo"
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
    colorBG: '000000',
    accessToken: null
  }),

  mounted() {
    const { showAlbumArt, showArtist, showBackground, showSpotifyLogo, colorBG, accessToken } =
      this.$route.query
    this.showAlbumArt = Boolean(showAlbumArt)
    this.showArtist = Boolean(showArtist)
    this.showBackground = Boolean(showBackground)
    this.showSpotifyLogo = Boolean(showSpotifyLogo)
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
