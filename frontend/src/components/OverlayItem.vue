<script lang="ts" setup>
import fakeAlbumArt from '@/assets/fakeAlbumArt.webp'
import PreloadedImage from '@/components/PreloadedImage.vue'
import axios from 'axios'
import { computed, onMounted, ref } from 'vue'
import SpotifyIcon from '@/components/icons/SpotifyIcon.vue'

defineProps({
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
  fakeTitle: {
    type: String,
    default: null
  },
  fakeArtist: {
    type: String,
    default: null
  }
})
const accessToken = ref(document.cookie
  .split('; ')
  .find((row) => row.startsWith('access_token='))
  ?.split('=')[1])

const refreshToken = ref(document.cookie
  .split('; ')
  .find((row) => row.startsWith('refresh_token='))
  ?.split('=')[1])

const userPlayer = ref(null)
const borderRadiusValues = [0, 12, 18, 24, 9999]

const trackName = computed(() => {
  return userPlayer.value ? userPlayer.value.item.name : null
})

const trimArtistName = computed(() => {
  if (!userPlayer.value || userPlayer.value.item.artists.length === 0) {
    return null
  }
  return userPlayer.value.item.artists[0].name
})

const artistName = computed(() => {
  if (!userPlayer.value || userPlayer.value.item.artists.length === 0) {
    return null
  }
  return userPlayer.value.item.artists.map((artist) => artist.name).join(', ')
})

const albumArt = computed(() => {
  if (!userPlayer.value || userPlayer.value.item.album.images.length === 0) {
    return null
  }
  return userPlayer.value.item.album.images[0].url
})

const loadUserPlayer = () => {
  const headers = {
    Authorization: `Bearer ${accessToken.value}`
  }

  axios
    .get('https://api.spotify.com/v1/me/player/currently-playing', { headers })
    .then((response) => {
      userPlayer.value = response.data
      setTimeout(loadUserPlayer, 1000)
    })
    .catch(async (error) => {
      if ((error.response && error.response.status === 401) || (error.response && error.response.status === 400)) {
        try {
          const refreshResponse = await axios.post(
            'http://localhost:8080/api/auth/refresh_token',
            null, {
              params: {
                refresh_token: refreshToken.value,
              },
            }
          );

          accessToken.value = refreshResponse.data.access_token
          document.cookie = `access_token=${accessToken.value}; path=/;`;

          loadUserPlayer();
        } catch (refreshError) {
          console.error('Error refreshing token:', refreshError);
        }
      }
    })
}

onMounted(() => {
  loadUserPlayer()
})
</script>

<template>
  <div
    v-if="albumArt || artistName || fakeArtist"
    :style="{
      width: showMaxWidth ? '' : 'max-content',
      maxWidth: showMaxWidth ? '' : '420px',
      border: showBorder ? '2px solid rgba(38 38 38 / 0.75)' : '',
      backgroundColor:
        bgOpacity === 100 ? 'rgba(0, 0, 0, 1)' : `rgba(0, 0, 0, 0.${bgOpacity / 10})`,
      borderRadius: borderRadiusValues[borderSize - 1] + 'px'
    }"
    class="media"
  >
    <div class="media__image">
      <PreloadedImage
        id="cover"
        :src="albumArt || fakeAlbumArt"
        alt="Album Art"
        :style="{ borderRadius: borderRadiusValues[borderSize - 1] / 2 + 'px' }"
      />
    </div>
    <div class="media__info">
      <div class="media__info__track">
        <p class="track__name">
          {{ trackName || fakeTitle }}
        </p>
        <p v-if="trimArtist" class="track__artist" v-text="trimArtistName"></p>
        <p v-else class="track__artist" v-text="artistName || fakeArtist"></p>
      </div>
    </div>
    <div class="spotify-logo">
      <SpotifyIcon color="#1db954" :size="24" />
    </div>
  </div>
</template>
