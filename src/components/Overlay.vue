<template>
  <div
    v-if="albumArt || artistName || fakeArtist"
    :style="{
      backgroundColor: showBackground ? `#${colorBG}99` : 'transparent',
      width: showMaxWidth ? 'max-content' : '',
      maxWidth: showMaxWidth ? '420px' : ''
    }"
    class="media"
  >
    <div v-show="showAlbumArt" class="media__image">
      <PreloadedImage id="cover" :src="albumArt || fakeAlbumArt" alt="Album Art" />
    </div>
    <div class="media__info">
      <div class="media__info__track">
        <div class="track__name">
          {{ trackName || fakeTitle }}
        </div>
        <div v-show="showArtist" class="track__artist" v-text="artistName || fakeArtist"></div>
      </div>
      <div v-show="showSpotifyLogo" class="spotify-logo">
        <img src="@/assets/spotify-logo-without-text.svg" alt="Spotify" />
      </div>
    </div>
  </div>
  <a :href="trackLink" class="btn">
    <SpotifyLogo/>
    PLAY ON SPOTIFY</a>
</template>

<script>
import fakeAlbumArt from '@/assets/fakeAlbumArt.webp'
import PreloadedImage from '@/components/PreloadedImage.vue'
import axios from 'axios'
import SpotifyLogo from "@/components/SpotifyLogo.vue";

const endpointUri = 'https://api.spotify.com/v1/me/player/currently-playing'

export default {
  components: {SpotifyLogo, PreloadedImage },

  props: {
    showArtist: {
      type: Boolean,
      default: true
    },

    showAlbumArt: {
      type: Boolean,
      default: true
    },

    showBackground: {
      type: Boolean,
      default: true
    },

    colorBG: {
      type: String,
      default: '000000'
    },

    showSpotifyLogo: {
      type: Boolean,
      default: true
    },

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

      return this.userPlayer.item.artists[0].name
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

        setTimeout(this.loadUserPlayer, 1000)
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
