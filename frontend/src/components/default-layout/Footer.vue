<script setup lang="ts">
import { Logotype } from '@/components'
import { Button } from '@/components/ui/button'
import { FOOTER_NAV_PRODUCT_DATA, SocialLinksData } from '@/data'
import { hidden, moveTo, openLink } from '@/lib/utils'
import { useI18n } from 'vue-i18n'

const { t } = useI18n()
</script>
<template>
  <footer class="container m-auto mt-10 flex flex-col gap-10 py-16">
    <div class="flex justify-between gap-8">
      <div class="flex flex-col gap-4" :class="[hidden ? 'max-w-52' : '']">
        <div @click="moveTo('main')" class="flex flex-row items-center gap-3">
          <Logotype :size="25" />
          <span
            class="font-bold leading-4 cursor-pointer text-lg transition-colors hover:text-gray-300"
          >
            Beatwave
          </span>
        </div>
        <span class="text-sm max-w-[400px] text-neutral-300 font-normal whitespace-pre-line">
          {{ t('default-layout.footer.description') }}
        </span>
        <span class="text-xs text-[#7D7D7D]">
          {{ t('default-layout.footer.copyright') }} © 2025 Beatwave.
        </span>
        <div class="flex flex-wrap gap-2">
          <Button
            v-for="social in SocialLinksData"
            :key="social"
            :aria-label="social.name"
            @click="openLink(social.url)"
            variant="ghost"
            size="icon"
            class="h-fit w-fit cursor-pointer p-2"
          >
            <component :is="social.icon" :size="20" />
          </Button>
        </div>
      </div>
      <div
        class="flex"
        :class="[hidden ? 'flex-col justify-start gap-8' : 'flex-row justify-end gap-32']"
      >
        <div v-for="nav in FOOTER_NAV_PRODUCT_DATA" :key="nav.title" class="flex flex-col gap-2">
          <span class="text-base font-bold capitalize">
            {{ nav.title }}
          </span>
          <div class="flex flex-col gap-2">
            <RouterLink
              v-for="item in nav.items"
              :key="item.name"
              :to="item.url"
              class="text-base font-normal text-[#A9A9A9] capitalize transition duration-150 hover:text-[#F2F2F2]"
            >
              {{ item.name }}
            </RouterLink>
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>
