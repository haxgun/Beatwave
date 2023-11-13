<template>
  <div>
    <router-view />
  </div>
</template>

<script>
export default {
  computed: {
    widgetMode () {
      return this.$route.name === 'nowPlaying'
    }
  }
}
</script>

<style lang="scss">
</style>
