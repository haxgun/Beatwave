<script setup lang="ts">
import { cn } from '@/lib/utils'
import { type HTMLAttributes } from 'vue'

const props = withDefaults(
  defineProps<{
    avatar_url?: string
    username?: string
    class?: HTMLAttributes['class']
  }>(),
  {
    class: 'size-8 rounded-sm bg-neutral-900',
  },
)
</script>

<template>
  <img
    v-if="props.avatar_url"
    :class="cn(props.class)"
    :src="props.avatar_url"
    :alt="props.username || 'User avatar'"
  />
  <img
    v-else
    :class="cn(props.class)"
    src="https://api.dicebear.com/9.x/lorelei/svg"
    :alt="props.username || 'User avatar'"
  />
</template>
