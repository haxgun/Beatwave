import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useUserStore = defineStore('userStore', () => {
  const user = ref({
    username: 'MXMOD',
    email: 'mxmod@example.com',
    avatarUrl: 'https://api.dicebear.com/9.x/pixel-art/svg',
    twitch_display_name: 'haxgun',
    broadcaster_type: 'partner',
  })

  const error = ref(false)
  const loading = ref(false)

  return {
    user,
    error,
    loading,
  }
})
