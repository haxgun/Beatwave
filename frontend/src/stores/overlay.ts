import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useOverlayStore = defineStore(
  'userStore',
  () => {
    const bgColor = ref('#000000')
    const avgCoverColor = ref(false)
    const textColor = ref('#f2f2f2')
    const widthLimitation = ref(false)
    const showBorder = ref(false)
    const borderColor = ref('#000000')
    const borderRadius = ref(0)
    const textFont = ref('Geist')
    const trimArtist = ref(false)

    return {
      bgColor,
      avgCoverColor,
      textColor,
      widthLimitation,
      showBorder,
      borderColor,
      borderRadius,
      textFont,
      trimArtist,
    }
  },
  {
    persist: true,
  },
)
