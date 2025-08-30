import { useWindowSize } from '@vueuse/core'
import type { ClassValue } from 'clsx'
import { clsx } from 'clsx'
import { twMerge } from 'tailwind-merge'
import { computed } from 'vue'

const { width } = useWindowSize()

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}

export const openLink = (url: string) => {
  window.open(url, '_blank')
}

export const hidden = computed(() => width.value < 880)

export const moveTo = (containerId: string) => {
  const container = document.getElementById(containerId)
  if (container) {
    const scrollTopOffset = container.getBoundingClientRect().top + window.scrollY - 25
    window.scrollTo({
      top: scrollTopOffset - 70,
      left: 0,
      behavior: 'smooth',
    })
  }
}
