<script setup lang="ts">
import { Logotype } from '@/components'
import { Button } from '@/components/ui/button'
import { computed } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

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
    <RouterLink :to="{ name: 'home' }" class="inline-flex items-center gap-2 font-semibold">
      <Logotype />
      <span>Beatwave</span>
    </RouterLink>
    <div class="inline-flex items-center justify-center gap-4">
      <!-- <Button @click="openLink('https://github.com/haxgun/Milady')" variant="ghost" size="icon">
        <GithubIcon />
      </Button> -->
      <RouterLink
        v-for="route in visibleRoutes"
        :key="route.name"
        :to="{ name: route.name }"
        class="rounded-full capitalize text-sm font-medium"
      >
        {{ route.name }}
      </RouterLink>
      <Button @click="router.push({ name: 'auth' })" class="rounded-full">Connect</Button>
    </div>
  </header>
</template>
