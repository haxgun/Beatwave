<script setup lang="ts">
import { ref, type HTMLAttributes } from 'vue'

const props = withDefaults(
  defineProps<{
    items: Array<{ name: string; link: string }>
    class?: HTMLAttributes['class']
    isInHeroSection?: boolean
  }>(),
  {
    isInHeroSection: true,
  },
)

const emits = defineEmits(['itemClick'])
const hovered = ref<number | null>(null)
function handleItemHover(idx: number) {
  hovered.value = idx
}

function clearHover() {
  hovered.value = null
}

function handleClick() {
  emits('itemClick')
}
</script>

<template>
  <div
    class="hidden flex-row items-center font-medium justify-center text-sm transition duration-200 lg:flex"
    :class="[
      props.class,
      props.isInHeroSection
        ? 'text-zinc-300 hover:text-white'
        : 'text-zinc-600 hover:text-zinc-800',
    ]"
    @mouseleave="clearHover"
  >
    <a
      v-for="(item, idx) in props.items"
      :key="`link-${idx}`"
      :href="item?.link"
      class="relative px-4 py-2"
      @mouseenter="handleItemHover(idx)"
      @click="handleClick"
    >
      <transition name="fade">
        <div
          v-if="hovered === idx"
          class="absolute -bottom-1 left-1/2 -translate-x-1/2 h-1 w-5 rounded-lg bg-card"
        />
      </transition>
      <span
        class="relative z-20 transition-colors"
        :class="props.isInHeroSection ? 'text-white' : 'text-zinc-800'"
      >
        {{ item?.name }}
      </span>
    </a>
  </div>
</template>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
