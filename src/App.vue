<template>
  <div>
    <router-view />
  </div>
</template>

<script>
export default {
  computed: {
    widgetMode() {
      return this.$route.name === 'overlay'
    }
  }
}
</script>

<style lang="scss"></style>
