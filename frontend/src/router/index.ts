import { createRouter, createWebHistory } from 'vue-router'

function hasAccessToken() {
  const cookies = document.cookie.split(';').map((c) => c.trim())
  return cookies.some((cookie) => cookie.startsWith('access_token='))
}

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      name: 'index',
      path: '/',
      component: () => import('@/views/IndexView.vue'),
      beforeEnter: (to, from, next) => (hasAccessToken() ? next({ name: 'settings' }) : next())
    },
    {
      name: 'settings',
      path: '/settings',
      component: () => import('@/views/SettingsView.vue'),
      beforeEnter: (to, from, next) => (hasAccessToken() ? next() : next({ name: 'index' }))
    },
    {
      name: 'overlay',
      path: '/overlay',
      component: () => import('@/views/OverlayView.vue'),
      props: (route) => ({ overlayID: route.params.overlayID })
    },
    {
      path: '/:pathMatch(.*)*',
      component: () => import('@/views/PageNotFoundView.vue'),
      meta: { hideHighlight: true }
    }
  ]
})

export default router
