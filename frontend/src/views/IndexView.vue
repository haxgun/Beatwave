<script lang="ts" setup>
import MelodyIcon from '@/components/icons/MelodyIcon.vue'
import SpotifyIcon from '@/components/icons/SpotifyIcon.vue'
</script>

<template>
  <div class="main">
    <div class="main__body">
      <div class="main__container">
        <div class="blick"></div>
        <div class="blick2"></div>
        <div class="logo">
          <MelodyIcon :size="140" />
          <span class="logo__gradient"></span>
        </div>
        <h1 class="title">Milady</h1>
        <p class="description">The ultimate accessory for your Stream.</p>
        <p class="subdescription">
          Milady displays on your Stream information about the current track, the artist and the
          cover of the track playing on
          <span style="white-space: nowrap">
            <SpotifyIcon style="position: relative; top: 5px" :color="'#2ebd59'" />
            Spotify</span
          >
        </p>
        <a href="http://localhost:8000/auth/login" class="btn">
          <SpotifyIcon :size="24" :color="'#fff'" />
          Login with Spotify
        </a>
        <p class="footer">
          Completely free.<br />
          We do not store any information.<br />
          All processing happens inside your browser.
        </p>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.main {
  min-height: 100vh;
}
</style>
