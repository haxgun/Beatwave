<template>
  <div class="main">
    <div class="main__body">
      <div class="main__container">
        <div class="blick"></div>
        <div class="blick2"></div>
        <div class="logo">
          <img src="@/assets/logo.svg" alt="Logotype" width="140px" />
          <span class="logo__gradient"></span>
        </div>
        <h1 class="title">Milady</h1>
        <p class="description">The ultimate accessory for your Stream.</p>
        <p class="subdescription">
          Milady displays on your Stream information about the current track, the artist and the
          cover of the track playing on
          <span style="white-space: nowrap">
            <SpotifyLogo style="position: relative; top: 5px" :color="'#2ebd59'" />
            Spotify</span
          >
        </p>
        <a :href="loginUri" v-show="showLoginButton" class="btn"><SpotifyLogo :size="'24px'" :color="'#fff'" /> Login with Spotify </a>
        <p class="footer">
          Completely free.<br />
          We do not store any information.<br />
          All processing happens inside your browser.
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import SpotifyLogo from '@/components/SpotifyLogo.vue'

export default {
  components: { SpotifyLogo },
  props: {
    showLoginButton: {
      type: Boolean,
      default: true
    },

    loginUri: {
      type: String,
      default: null
    }
  }
}
</script>

<style lang="scss" scoped>
.main {
  min-height: 100vh;
}
</style>
