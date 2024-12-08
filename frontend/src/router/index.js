import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      name: 'index',
      path: '/',
      component: () => import('@/views/IndexView.vue')
    },

    {
      name: 'settings',
      path: '/settings',
      component: () => import('@/views/SettingsView.vue')
    },

    {
      name: 'overlay',
      path: '/overlay',
      component: () => import('@/views/OverlayView.vue'),
      props: (route) => ({ overlayID: route.params.overlayID })
    }
  ]
})

export default router
