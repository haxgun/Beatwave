<template>
  <div class="main">
    <div class="main__body">
      <div class="main__container">
        <InputSwitch v-model="settings.showAlbumArt" />
        <InputSwitch v-model="settings.showArtist" />
        <InputSwitch v-model="settings.showBackground" />
        <div class="preview">
          <div class="preview__content">
            <Overlay
              class="widget"
              :showAlbumArt="settings.showAlbumArt"
              :showArtist="settings.showArtist"
              :accessToken="accessToken"
              :showBackground="settings.showBackground"
              :fakeTitle="settings.fakeTitle"
              :fakeArtist="settings.fakeArtist"
              :fakeAlbumArt="settings.fakeAlbumArt"
            />
          </div>
          <div class="preview__background">
            <img src="@/assets/preview_bg.webp" alt="" />
          </div>
        </div>
        <InputText rows="5" cols="82" class="textarea" readonly v-model="browserSourceUrl" />
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
      showAlbumArt: true,
      showArtist: true,
      showBackground: true,
      fakeTitle: 'Blinding Lights',
      fakeArtist: 'The Weeknd',
      fakeAlbumArt: '/src/assets/fakeAlbumArt.webp'
    }
  })
}
</script>

<style lang="scss" scoped></style>
