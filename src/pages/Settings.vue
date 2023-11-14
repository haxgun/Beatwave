<template>
  <div class="main">
    <div class="main__body">
      <div class="main__container">
        <div class="settings">
          <div class="settings__content">
            <h1 class="settings__title">Settings</h1>
            <span>
              <label for="showAlbumArt">Album art</label>
              <InputSwitch v-model="settings.showAlbumArt" aria-labelledby="showAlbumArt" />
            </span>
            <span>
              <label for="showArtist">Artist name</label>
              <InputSwitch v-model="settings.showArtist" aria-labelledby="showArtist" />
            </span>
            <span>
              <label for="showBackground">Show background</label>
              <InputSwitch v-model="settings.showBackground" aria-labelledby="showBackground" />
            </span>
            <span>
              <label for="showBackground">Change Background color</label>
              <ColorPicker v-model="settings.colorBG" />
            </span>
            <span>
              <label for="showSpotifyLogo">Show Spotify logo</label>
              <InputSwitch v-model="settings.showSpotifyLogo" aria-labelledby="showSpotifyLogo" />
            </span>
          </div>
          <div class="settings__preview">
            <div class="preview">
              <div class="preview__content">
                <Overlay
                  class="widget"
                  :showAlbumArt="settings.showAlbumArt"
                  :showArtist="settings.showArtist"
                  :showBackground="settings.showBackground"
                  :colorBG="settings.colorBG"
                  :showSpotifyLogo="settings.showSpotifyLogo"
                  :fakeTitle="'Blinding Lights'"
                  :fakeArtist="'The Weeknd'"
                  :accessToken="accessToken"
                />
              </div>
              <div class="preview__background">
                <img src="@/assets/preview_bg.webp" alt="" />
              </div>
            </div>
            <div class="settings__input">
              <InputText
                id="linkOBS"
                rows="5"
                cols="82"
                class="textarea"
                readonly
                v-model="browserSourceUrl"
              />
              <Button @click="copyText()" icon="pi pi-copy" aria-label="Filter" />
            </div>
          </div>
        </div>
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

    copyText() {
      const inputDoc = this.browserSourceUrl
      navigator.clipboard.writeText(inputDoc)
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
      showSpotifyLogo: true,
      colorBG: '000000'
    }
  })
}
</script>

<style lang="scss" scoped></style>
