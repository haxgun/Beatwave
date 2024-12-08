<script lang="ts" setup>
import { onMounted, ref, watch } from 'vue'

const props = defineProps({
  src: {
    type: String,
    required: true
  }
})

const mountedSrc = ref(null)

const load = () => {
  const image = new Image()

  image.onload = () => {
    mountedSrc.value = props.src
  }

  image.src = props.src
}

watch(() => props.src, load)

onMounted(() => {
  load()
})
</script>

<template>
  <Transition name="fade">
    <img v-show="mountedSrc" :src="mountedSrc" />
  </Transition>
</template>
