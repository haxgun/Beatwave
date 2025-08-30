<script setup lang="ts">
import { Logotype } from '@/components'
import { LanguageSwitcher } from '@/components/ui'
import { Button } from '@/components/ui/button'
import { SocialLinksData } from '@/data'
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'
import { useRouter } from 'vue-router'

const router = useRouter()
const { t } = useI18n()

const visibleRoutes = computed(() => {
  return router.getRoutes().filter((route) => {
    return route.name && route.meta?.showInHeader === true
  })
})
</script>

<template>
  <header
    class="h-18 items-center justify-between fixed inline-flex text-white container left-1/2 -translate-x-1/2 z-100"
  >
    <RouterLink :to="{ name: 'home' }" class="inline-flex items-center gap-2.5 font-semibold">
      <Logotype />
      <span>Beatwave</span>
    </RouterLink>
    <div class="inline-flex items-center justify-center gap-4">
      <div class="inline-flex gap-2">
        <Button
          v-for="social in SocialLinksData"
          as="a"
          target="__blank"
          variant="ghost"
          size="icon"
          class="h-fit w-fit cursor-pointer p-2"
          :key="social"
          :aria-label="social.name"
          :href="social.url"
        >
          <component :is="social.icon" :size="20" />
        </Button>
        <LanguageSwitcher />
      </div>

      <RouterLink
        v-for="route in visibleRoutes"
        :key="route.name"
        :to="{ name: route.name }"
        class="rounded-full capitalize text-sm font-medium"
      >
        {{ route.name }}
      </RouterLink>
      <Button @click="router.push({ name: 'auth' })" class="rounded-full">
        {{ t('default-layout.header.connect') }}
      </Button>
    </div>
  </header>
</template>
