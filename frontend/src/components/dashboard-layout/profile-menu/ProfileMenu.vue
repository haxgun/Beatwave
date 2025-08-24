<script setup lang="ts">
import { Button } from '@/components/ui/button'

import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuGroup,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from '@/components/ui/dropdown-menu'

import { TwitchVerify } from '@/components/icons'

import { openLink } from '@/lib/utils.ts'
import { LifeBuoy, NotebookText, Settings as SettingsIcon } from 'lucide-vue-next'

import { UserAvatar, UserBio } from '@/components/dashboard-layout/profile-menu'
import { Skeleton } from '@/components/ui/skeleton'
import router from '@/router'
import { useAuthStore, useUserStore } from '@/stores'
import { storeToRefs } from 'pinia'

const authStore = useAuthStore()

const userStore = useUserStore()
const { user, loading, error } = storeToRefs(userStore)

// watch(error, (newError) => {
//   if (newError === true) {
//     authStore.logout()
//   }
// })

// onMounted(() => {
//   userStore.fetchUser()
// })
//
</script>

<template>
  <DropdownMenu>
    <div v-if="loading" class="inline-flex items-center gap-2">
      <Skeleton class="size-8 flex flex-shrink-0 rounded-sm" />
      <div class="flex flex-col gap-1 items-start w-full">
        <Skeleton class="line-clamp-1 h-3 w-24 rounded-md" />
        <Skeleton class="line-clamp-3 h-2 w-16 rounded-md" />
      </div>
      <Skeleton class="size-8 flex flex-shrink-0 rounded-sm" />
    </div>
    <div v-else-if="error" class="font-bold w-full flex items-center justify-center h-5 mb-2">
      Error
    </div>
    <DropdownMenuTrigger v-else-if="user && !loading && !error" as-child>
      <Button variant="profile" size="none" class="p-0 inline-flex items-center gap-2 relative">
        <UserAvatar :avatar_url="user.avatar_url" :username="user.username" />
        <TwitchVerify
          class="size-4 absolute -right-1 -top-1"
          v-if="user.broadcaster_type === 'partner'"
        />
      </Button>
    </DropdownMenuTrigger>
    <DropdownMenuContent align="start" class="w-56 mb-1">
      <DropdownMenuLabel class="flex items-center justify-start gap-2" v-if="user">
        <UserBio
          :avatar_url="user.avatar_url"
          :username="user.username"
          :twitch_display_name="user.twitch_display_name"
          :partner="user.broadcaster_type === 'partner'"
        />
      </DropdownMenuLabel>
      <DropdownMenuSeparator />
      <DropdownMenuGroup>
        <DropdownMenuItem @click="router.push({ name: 'configurator-settings' })">
          <SettingsIcon class="mr-1 size-4" />
          <span>Settings</span>
        </DropdownMenuItem>
      </DropdownMenuGroup>
      <DropdownMenuSeparator />
      <DropdownMenuItem @click="openLink('https://discord.gg/pYV4PBV5YW')">
        <LifeBuoy class="mr-1 size-4" />
        <span>Support</span>
      </DropdownMenuItem>
      <DropdownMenuItem @click="router.push({ name: 'terms' })">
        <NotebookText class="text-muted-foreground mr-1 size-4" />
        <span>Terms of Service</span>
      </DropdownMenuItem>
    </DropdownMenuContent>
  </DropdownMenu>
</template>

<style scoped>
.line-clamp-1 {
  display: -webkit-box;
  line-clamp: 1;
  -webkit-line-clamp: 1;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.line-clamp-3 {
  display: -webkit-box;
  line-clamp: 3;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>
