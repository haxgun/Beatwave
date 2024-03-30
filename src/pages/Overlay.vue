<template>
  <Overlay
    v-if="accessToken"
    :showMaxWidth="showMaxWidth"
    :accessToken="accessToken"
  />
</template>

<script>
import Overlay from '@/components/Overlay.vue'

export default {
  components: { Overlay },

  data: () => ({
    showMaxWidth: true,
    accessToken: null
  }),

  mounted() {
    const {
      accessToken,
      showMaxWidth,
    } = this.$route.query

    this.showMaxWidth = JSON.parse(showMaxWidth)
    this.accessToken = accessToken
  }
}
</script>

<style>
:root {
  background: none !important;
}
</style>
