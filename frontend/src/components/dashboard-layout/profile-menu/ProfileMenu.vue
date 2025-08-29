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

import { openLink } from '@/lib/utils.ts'
import { LifeBuoyIcon, LogOutIcon, NotebookTextIcon, SettingsIcon } from 'lucide-vue-next'
import { useI18n } from 'vue-i18n'

import { UserAvatar, UserBio } from '@/components/dashboard-layout/profile-menu'
import { Skeleton } from '@/components/ui/skeleton'
import router from '@/router'
import { useAuthStore, useUserStore } from '@/stores'
import { storeToRefs } from 'pinia'

const authStore = useAuthStore()

const { t } = useI18n()

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
      <Button
        variant="profile"
        size="none"
        class="p-0 size-fit items-center gap-2 relative hover:shadow-[0_0_0_2px_#242424]"
      >
        <UserAvatar :avatar_url="user?.avatar_url" :username="user?.username" />
      </Button>
    </DropdownMenuTrigger>
    <DropdownMenuContent align="end" class="w-56 mb-1">
      <DropdownMenuLabel class="flex items-center justify-start gap-2">
        <UserBio
          :avatar_url="user?.avatar_url"
          :username="user?.username"
          :twitch_display_name="user?.twitch_display_name"
        />
      </DropdownMenuLabel>
      <DropdownMenuSeparator />
      <DropdownMenuGroup>
        <DropdownMenuItem @click="router.push({ name: 'configurator-settings' })">
          <SettingsIcon class="mr-1 size-4" />
          <span>{{ t('components.profileMenu.buttons.settings') }} </span>
        </DropdownMenuItem>
      </DropdownMenuGroup>
      <DropdownMenuSeparator />
      <DropdownMenuItem @click="openLink('https://discord.gg/pYV4PBV5YW')">
        <LifeBuoyIcon class="mr-1 size-4" />
        <span>{{ t('components.profileMenu.buttons.support') }}</span>
      </DropdownMenuItem>
      <DropdownMenuItem @click="router.push({ name: 'terms' })">
        <NotebookTextIcon class="text-muted-foreground mr-1 size-4" />
        <span>{{ t('components.profileMenu.buttons.terms') }}</span>
      </DropdownMenuItem>
      <DropdownMenuSeparator />
      <DropdownMenuItem>
        <LogOutIcon class="text-muted-foreground mr-1 size-4" />
        <span>{{ t('components.profileMenu.buttons.logout') }}</span>
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
