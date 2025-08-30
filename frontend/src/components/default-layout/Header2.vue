<script setup lang="ts">
import {
  MobileNav,
  MobileNavHeader,
  MobileNavMenu,
  MobileNavToggle,
  Navbar,
  NavbarButton,
  NavBody,
} from '@/components/ui/navbar'
import { ref } from 'vue'

const isMenuOpen = ref(false)

function toggleMenu() {
  isMenuOpen.value = !isMenuOpen.value
}
function closeMenu() {
  isMenuOpen.value = false
}

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

const headerLinks = SocialLinksData.filter((link) => link.showInHeader)
</script>

<template>
  <Navbar>
    <template #default="{ visible }">
      <NavBody :visible="visible">
        <RouterLink :to="{ name: 'home' }" class="inline-flex items-center gap-2.5 font-semibold">
          <Logotype />
          <span>Beatwave</span>
        </RouterLink>
        <div class="inline-flex items-center justify-center gap-4">
          <div class="inline-flex gap-2">
            <Button
              v-for="social in headerLinks"
              as="a"
              target="__blank"
              variant="ghost"
              size="icon"
              class="h-fit w-fit cursor-pointer p-2"
              :key="social.name"
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
      </NavBody>

      <MobileNav :visible="visible">
        <MobileNavHeader>
          <RouterLink :to="{ name: 'home' }" class="inline-flex items-center gap-2.5 font-semibold">
            <Logotype />
            <span>Beatwave</span>
          </RouterLink>
          <MobileNavToggle :is-open="isMenuOpen" @click="toggleMenu" />
        </MobileNavHeader>

        <MobileNavMenu :is-open="isMenuOpen" @close="closeMenu">
          <!-- <a
            v-for="(item, idx) in navItems"
            :key="`mobile-link-${idx}`"
            :href="item.link"
            class="w-full px-4 py-2 text-neutral-600 hover:bg-gray-100 rounded-md"
            @click="closeMenu"
          >
            {{ item.name }}
          </a> -->

          <NavbarButton to="/signup" class="w-full mt-4" @click="router.push({ name: 'auth' })">
            {{ t('default-layout.header.connect') }}
          </NavbarButton>
        </MobileNavMenu>
      </MobileNav>
    </template>
  </Navbar>
</template>
