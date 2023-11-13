<template>
  <div class="main">
    <div class="main__body">
      <div class="main__container">
        <b-switch v-model="settings.showSpotifyLogo" />
        <b-switch v-model="settings.showAlbumArt" />
        <b-switch v-model="settings.showArtist" />

        <Overlay
          class="widget"
          :showAlbumArt="settings.showAlbumArt"
          :showArtist="settings.showArtist"
          :showSpotifyLogo="settings.showSpotifyLogo"
          :accessToken="accessToken"
        />
        <textarea class="textarea" readonly>{{ browserSourceUrl }}</textarea>
      </div>
    </div>
  </div>
</template>

<script>
import queryString from 'query-string'
import Overlay from '@/components/Overlay.vue'

export default {
  components: { Overlay },

  computed: {
    accessToken() {
      const parsed = queryString.parse(this.$route.hash)
      return parsed['access_token']
    },

    browserSourceUrl() {
      const nowPlayingPage = this.$router.resolve({ name: 'overlay' }),
        base = `${location.origin}${nowPlayingPage.href}`

      const query = queryString.stringify({
        accessToken: this.accessToken,
        ...this.settings
      })

      return `${base}?${query}`
    }
  },

  data: () => ({
    settings: {
      showSpotifyLogo: true,
      showAlbumArt: true,
      showArtist: true
    }
  })
}
</script>

<style lang="scss" scoped></style>
