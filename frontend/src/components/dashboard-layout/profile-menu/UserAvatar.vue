<script setup lang="ts">
const props = defineProps<{
  avatar_url?: string
  username?: string
}>()
</script>

<template>
  <img
    v-if="props.avatar_url"
    class="size-8 rounded-sm bg-neutral-500"
    :src="props.avatar_url"
    :alt="props.username || 'User avatar'"
  />
  <img
    v-else
    class="size-8 rounded-full bg-neutral-900"
    src="https://api.dicebear.com/9.x/lorelei/svg"
    :alt="props.username || 'User avatar'"
  />
</template>
