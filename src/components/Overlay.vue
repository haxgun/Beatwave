<template>
  <div
    v-if="albumArt || artistName || fakeArtist"
    :style="{
      width: showMaxWidth ? '' : 'max-content',
      maxWidth: showMaxWidth ? '' : '420px',
      border: showBorder ? '2px solid rgba(38 38 38 / 0.75)' : '',
      backgroundColor: bgOpacity === 100 ? 'rgba(0, 0, 0, 1)' : `rgba(0, 0, 0, 0.${bgOpacity / 10})`,
      borderRadius: borderRadiusValues[borderSize-1] + 'px',
    }"
    class="media"
  >
    <div class="media__image">
      <PreloadedImage id="cover" :src="albumArt || fakeAlbumArt" alt="Album Art" :style="{borderRadius: borderRadiusValues[borderSize-1] / 2 + 'px'}"/>
    </div>
    <div class="media__info">
      <div class="media__info__track">
        <p class="track__name">
          {{ trackName || fakeTitle }}
        </p>
        <p v-if="trimArtist" class="track__artist" v-text="trimArtistName"></p>
        <p v-else class="track__artist" v-text="artistName || fakeArtist"></p>

        <!-- <div class="progress">
          <div class="track__progress"></div>
          <div class="track__progress__bg"></div>
        </div> -->
      </div>
    </div>
    <!-- <div class="spotify-logo">
      <svg width="24" height="24" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M23.9266 0C10.7126 0 0 10.7123 0 23.9263C0 37.1409 10.7126 47.8523 23.9266 47.8523C37.142 47.8523 47.8534 37.1409 47.8534 23.9263C47.8534 10.7131 37.142 0.00114285 23.9263 0.00114285L23.9266 0ZM34.8991 34.5086C34.4706 35.2114 33.5506 35.4343 32.8477 35.0029C27.23 31.5714 20.158 30.7943 11.8294 32.6971C11.0269 32.88 10.2269 32.3771 10.044 31.5743C9.86029 30.7714 10.3611 29.9714 11.1657 29.7886C20.28 27.7054 28.098 28.6029 34.4049 32.4571C35.1077 32.8886 35.3306 33.8057 34.8991 34.5086ZM37.8277 27.9929C37.2877 28.8714 36.1391 29.1486 35.262 28.6086C28.8306 24.6546 19.0269 23.5097 11.4197 25.8189C10.4331 26.1169 9.39114 25.5609 9.09171 24.576C8.79457 23.5894 9.35086 22.5494 10.3357 22.2494C19.0251 19.6129 29.8277 20.89 37.2134 25.4286C38.0906 25.9686 38.3677 27.1169 37.8277 27.9929ZM38.0791 21.2089C30.3677 16.6286 17.6449 16.2074 10.2823 18.442C9.1 18.8006 7.84971 18.1331 7.49143 16.9509C7.13314 15.768 7.8 14.5186 8.98314 14.1591C17.4349 11.5934 31.4849 12.0891 40.3631 17.3597C41.4289 17.9909 41.7774 19.3643 41.146 20.4263C40.5174 21.4897 39.1403 21.8403 38.0803 21.2089H38.0791Z" fill="#1ED760"/>
      </svg>
    </div> -->
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

    showBorder: {
      type: Boolean,
      default: true
    },

    trimArtist: {
      type: Boolean,
      default: true
    },

    bgOpacity: {
      type: Number,
      default: 60
    },
    
    borderSize: {
      type: Number,
      default: 3
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
    userPlayer: null,
    borderRadiusValues: [0, 12, 18, 24, 9999]
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

    trimArtistName() {
      if (!this.userPlayer || this.userPlayer.item.artists.length == 0) {
        return null
      }

      return this.userPlayer.item.artists[0].name
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

<style lang="scss" scoped></style>
