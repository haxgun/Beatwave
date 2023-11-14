<template>
  <div v-if="albumArt || artistName" :style="{ backgroundColor: showBackground ? 'rgb(0 0 0 / 60%)' : 'transparent' }" class="media">
    <div v-if="showAlbumArt && albumArt " class="media__image">
      <PreloadedImage id="cover" :src="albumArt" alt="Album Art" />
    </div>
    <div class="media__info">
      <div class="track__name">{{ trackName }}</div>
      <div v-if="showArtist" class="track__artist">{{ artistName }}</div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

import PreloadedImage from '@/components/PreloadedImage.vue'

const endpointUri = 'https://api.spotify.com/v1/me/player/currently-playing'

export default {
  components: { PreloadedImage },

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

    accessToken: {
      type: String,
      default: null
    }
  },

  data: () => ({
    userPlayer: null
  }),

  computed: {
    spotifyInfo() {
      return this.userPlayer != null
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

        setTimeout(this.loadUserPlayer, 5000)
      })
    }
  }
}
</script>

<style lang="scss" scoped></style>
