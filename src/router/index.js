import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    }

    return new Promise((resolve) => {
      let scrollDuration = 500,
        cosParameter = window.scrollY / 2,
        oldTimestamp = performance.now(),
        scrollCount = 0

      function step(newTimestamp) {
        scrollCount += Math.PI / (scrollDuration / (newTimestamp - oldTimestamp))

        if (scrollCount >= Math.PI) {
          window.scrollTo(0, 0)
        }

        if (window.scrollY === 0) {
          resolve({ x: 0, y: 0 })

          return
        }

        window.scrollTo(0, Math.round(cosParameter + cosParameter * Math.cos(scrollCount)))

        oldTimestamp = newTimestamp

        window.requestAnimationFrame(step)
      }

      window.requestAnimationFrame(step)
    })
  },
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      name: 'index',
      path: '/',
      component: () => import('@/pages/Index.vue')
    },

    {
      name: 'settings',
      path: '/settings',
      component: () => import('@/pages/Settings.vue')
    },

    {
      name: 'overlay',
      path: '/overlay',
      component: () => import('@/pages/Overlay.vue')
    }
  ]
})

export default router
