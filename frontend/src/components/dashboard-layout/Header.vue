<script setup lang="ts">
import { Logotype } from '@/components'
import { ProfileMenu } from '@/components/dashboard-layout/profile-menu'
import { cn } from '@/lib/utils'
import { useRouter } from 'vue-router'

const router = useRouter()

const links = [
  { label: 'Dashboard', to: '/dashboard', active: true },
  { label: 'Settings', to: '/settings', active: false },
  { label: 'Logout', to: '/logout', active: false },
]
</script>

<template>
  <div
    class="w-full py-2 bg-black/95 backdrop-blur-lg inline-flex justify-between items-center px-6 border-b border-white/10"
  >
    <div class="inline-flex items-center gap-4">
      <Logotype class="cursor-pointer" @click="router.push({ name: 'home' })" />
      <div class="inline-flex items-center gap-1">
        <span
          class="rounded-sm text-xs font-medium px-2 py-1.5"
          v-for="link in links"
          :key="link.label"
          :class="
            cn(
              link.active
                ? 'bg-white/8 text-white'
                : 'text-white/10 hover:bg-white/5 hover:text-white transition-colors cursor-pointer',
            )
          "
        >
          {{ link.label }}
        </span>
      </div>
    </div>
    <ProfileMenu />
  </div>
</template>
