<script setup lang="ts">
import { TwitchVerify } from '@/components/icons'
import { UserAvatar } from '.'

const props = defineProps<{
  avatar_url?: string
  twitch_display_name: string
  username: string
  partner?: boolean
}>()
</script>

<template>
  <div class="inline-flex items-center gap-2">
    <div class="relative">
      <UserAvatar :avatar_url="props.avatar_url" :username="props.username" />
      <TwitchVerify class="size-4 absolute -right-1 -top-1" v-if="props.partner" />
    </div>
    <div class="flex flex-col gap-px">
      <span class="text-sm font-bold leading-none">{{ props.username }}</span>
      <span class="text-xs text-gray-500 leading-none">@{{ props.twitch_display_name }}</span>
    </div>
  </div>
</template>
