import { defineStore } from 'pinia'
import { ref, type Ref } from 'vue'

export type Theme = 'light' | 'dark' | 'system'

export const useThemeStore = defineStore(
  'theme',
  () => {
    const currentTheme: Ref<Theme> = ref('system')

    const applyTheme = (theme: Theme) => {
      const appElement = document.documentElement

      if (theme === 'system') {
        const systemDark = window.matchMedia('(prefers-color-scheme: dark)').matches
        if (systemDark) {
          appElement?.classList.add('dark')
        } else {
          appElement?.classList.remove('dark')
        }
      } else if (theme === 'dark') {
        appElement?.classList.add('dark')
      } else {
        appElement?.classList.remove('dark')
      }
    }

    const setTheme = (theme: Theme) => {
      currentTheme.value = theme
      applyTheme(theme)
    }

    const toggleTheme = () => {
      const themes: Theme[] = ['light', 'dark', 'system']
      const currentIndex = themes.indexOf(currentTheme.value)
      const nextIndex = (currentIndex + 1) % themes.length

      setTheme(themes[nextIndex])
    }

    const initTheme = () => {
      applyTheme(currentTheme.value)

      const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)')
      mediaQuery.addEventListener('change', () => {
        if (currentTheme.value === 'system') {
          applyTheme('system')
        }
      })
    }

    return {
      currentTheme,
      setTheme,
      toggleTheme,
      initTheme,
    }
  },
  {
    persist: true,
  },
)
