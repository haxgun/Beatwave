<template>
  <div
    v-if="albumArt || artistName || fakeArtist"
    :style="{
      width: showMaxWidth ? '' : 'max-content',
      maxWidth: showMaxWidth ? '' : '420px'
    }"
    class="media"
  >
    <div class="media__image">
      <PreloadedImage id="cover" :src="albumArt || fakeAlbumArt" alt="Album Art" />
    </div>
    <div class="media__info">
      <div class="media__info__track">
        <p class="track__name">
          {{ trackName || fakeTitle }}
        </p>
        <p class="track__artist" v-text="artistName || fakeArtist"></p>

        <div class="progress">
          <div class="track__progress"></div>
          <div class="track__progress__bg"></div>
        </div>
      </div>
    </div>
    <div class="spotify-logo">
        <img src="@/assets/spotify-logo-without-text.svg" alt="Spotify" />
      </div>
  </div>
</template>

<script>
import fakeAlbumArt from '@/assets/fakeAlbumArt.webp'
import PreloadedImage from '@/components/PreloadedImage.vue'
import SpotifyLogo from '@/components/SpotifyLogo.vue'
import axios from 'axios'

const endpointUri = 'https://api.spotify.com/v1/me/player/currently-playing'

export default {
  components: { SpotifyLogo, PreloadedImage },

  props: {
    showMaxWidth: {
      type: Boolean,
      default: true
    },

    accessToken: {
      type: String,
      default: null
    },

    fakeTitle: {
      type: String,
      default: null
    },

    fakeArtist: {
      type: String,
      default: null
    }
  },

  data: () => ({
    userPlayer: null
  }),

  computed: {
    fakeAlbumArt() {
      return fakeAlbumArt
    },

    trackLink() {
      return this.userPlayer ? this.userPlayer.item.external_urls.spotify : null
    },

    trackName() {
      return this.userPlayer ? this.userPlayer.item.name : null
    },

    artistName() {
      if (!this.userPlayer || this.userPlayer.item.artists.length == 0) {
        return null
      }

      return this.userPlayer.item.artists.map(artist => artist.name).join(', ')
    },

    albumArt() {
      if (!this.userPlayer || this.userPlayer.item.album.images.length == 0) {
        return null
      }

      return this.userPlayer.item.album.images[0].url
    }
  },

  mounted() {
    this.loadUserPlayer()
  },

  methods: {
    loadUserPlayer() {
      const headers = {
        Authorization: `Bearer ${this.accessToken}`
      }

      axios.get(endpointUri, { headers }).then((response) => {
        this.userPlayer = response.data

        setTimeout(this.loadUserPlayer, 5000)
      })
    }
  }
}
</script>

<style lang="scss" scoped>
.btn {
  width: 220px;
  align-items: center;
  border: none;
  color: #e8e8e8;
  display: flex;
  gap: 0.75rem;
  height: 3.5rem;
  padding: 0 1.5rem;
  font-weight: 600;
  font-size: 1.125rem;
  transition: all 0.2s;
  text-decoration: none;
  border-radius: 999px !important;
  background-color: #1db954 !important;
}
</style>
