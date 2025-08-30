<script setup lang="ts">
import type { Slot } from 'vue'
import { onMounted, onUnmounted, ref, type HTMLAttributes } from 'vue'

const props = defineProps<{
  class?: HTMLAttributes['class']
}>()

const navbarRef = ref(null)
const visible = ref(false)

function handleScroll() {
  const scrollY = window.scrollY

  if (scrollY > 100) {
    visible.value = true
  } else {
    visible.value = false
  }
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})

function provide(slot: Slot | undefined) {
  return {
    visible: visible.value,
  }
}
</script>

<template>
  <div
    ref="navbarRef"
    class="fixed top-0 z-50 container left-1/2 -translate-x-1/2"
    :class="props.class"
  >
    <div class="w-full inline-flex items-center mt-5">
      <slot v-bind="provide($slots?.default)" />
    </div>
  </div>
</template>
