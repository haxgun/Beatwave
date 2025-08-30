<script setup lang="ts">
import { computed } from 'vue'

const props = withDefaults(
  defineProps<{
    variant?: 'ghost' | 'primary' | 'secondary'
    className?: string
    isInHeroSection?: boolean
  }>(),
  {
    variant: 'ghost',
    isInHeroSection: true,
  },
)

const buttonClasses = computed(() => {
  const baseClasses = 'px-4 py-2 rounded-md font-medium text-sm transition-colors cursor-pointer'

  let variantClasses = ''

  if (props.variant === 'ghost') {
    variantClasses = props.isInHeroSection
      ? 'text-white hover:bg-white/10'
      : 'text-black hover:bg-black/5'
  } else if (props.variant === 'primary') {
    variantClasses = 'bg-white text-black hover:bg-gray-100'
  } else if (props.variant === 'secondary') {
    variantClasses = props.isInHeroSection
      ? 'border border-white/20 text-white hover:bg-white/10'
      : 'border border-black/20 text-black hover:bg-black/5'
  }

  return [baseClasses, variantClasses, props.className].filter(Boolean).join(' ')
})
</script>

<template>
  <button :class="buttonClasses">
    <slot />
  </button>
</template>
