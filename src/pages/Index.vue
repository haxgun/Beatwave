<template>
  <Landing :loginUri="loginWithSpotifyUri" />
</template>

<script>
import Landing from '@/components/Landing.vue'
import buildUrl from 'build-url'

export default {
  components: { Landing },

  computed: {
    loginWithSpotifyUri() {
      const settingsPage = this.$router.resolve({ name: 'settings' })
      const redirectUri = `${location.origin}${settingsPage.href}`

      const queryParams = {
        client_id: import.meta.env.VITE_SPOTIFY_CLIENT_ID,
        redirect_uri: redirectUri,
        response_type: 'token',
        scope: 'user-read-currently-playing'
      }

      return buildUrl('https://accounts.spotify.com/authorize', {
        queryParams
      })
    }
  }
}
</script>
