<script setup lang="ts">
import { Logotype } from '@/components'
import { ProfileMenu } from '@/components/dashboard-layout/profile-menu'
import { LanguageSwitcher, ThemeSwitcher } from '@/components/ui'
import { cn } from '@/lib/utils'
import { useI18n } from 'vue-i18n'
import { useRouter } from 'vue-router'

const router = useRouter()

const links = [{ label: 'dashboard-layout.header.links.dashboard', to: '/dashboard', active: true }]
const { t } = useI18n()
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
          {{ t(link.label) }}
        </span>
      </div>
    </div>
    <div class="inline-flex gap-3">
      <div class="inline-flex gap-px">
        <LanguageSwitcher />
        <ThemeSwitcher />
      </div>

      <ProfileMenu />
    </div>
  </div>
</template>
