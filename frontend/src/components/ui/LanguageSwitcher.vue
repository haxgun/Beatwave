<script lang="ts" setup>
import { Button } from '@/components/ui/button'
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuLabel,
  DropdownMenuRadioGroup,
  DropdownMenuRadioItem,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from '@/components/ui/dropdown-menu'

const { t } = useI18n()

import { LanguagesIcon } from 'lucide-vue-next'

import { AVAILABLE_LOCALES } from '@/i18n'
import { useLocalStorage } from '@vueuse/core'
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'

interface Props {
  variant?: 'default' | 'rounded'
}

const props = withDefaults(defineProps<Props>(), {
  variant: 'default',
})

const { locale } = useI18n<{ locale: string; availableLocales: string[] }>()
const currentLocale = useLocalStorage<string>('lang', 'en')

const currentLanguage = computed(() => {
  return AVAILABLE_LOCALES.find((lang) => lang.code === currentLocale.value)
})

const currentLanguageName = computed(() => {
  return currentLanguage.value?.name || 'English'
})
</script>

<template>
  <DropdownMenu>
    <DropdownMenuTrigger as-child>
      <Button
        v-if="props.variant === 'default'"
        variant="ghost"
        size="icon"
        aria-label="Language Switcher"
        class="h-fit w-fit cursor-pointer p-2"
      >
        <LanguagesIcon class="size-4" />
      </Button>
      <Button
        v-else
        aria-label="Language Switcher"
        class="mr-2 rounded-full border border-transparent bg-transparent text-white opacity-50 transition hover:border-white/10 hover:bg-white/10 hover:opacity-100"
      >
        <LanguagesIcon class="size-4" />
        <span class="text-sm">{{ currentLanguageName }}</span>
      </Button>
    </DropdownMenuTrigger>
    <DropdownMenuContent align="end" class="w-40">
      <DropdownMenuLabel>
        {{ t('components.languageSwitcher') }}
      </DropdownMenuLabel>
      <DropdownMenuSeparator />
      <DropdownMenuRadioGroup v-model="currentLocale">
        <DropdownMenuRadioItem
          v-for="lang of AVAILABLE_LOCALES"
          :key="lang.code"
          :value="lang.code"
          @select="
            () => {
              locale = lang.code
              currentLocale = lang.code
            }
          "
        >
          {{ lang.name }}
        </DropdownMenuRadioItem>
      </DropdownMenuRadioGroup>
    </DropdownMenuContent>
  </DropdownMenu>
</template>
