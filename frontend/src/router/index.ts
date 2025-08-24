import HomePage from '@/pages/HomePage.vue'
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomePage,
      meta: { showInHeader: true },
    },
    {
      path: '/help',
      name: 'help',
      redirect: { name: 'home' },
      meta: { showInHeader: true },
    },
    {
      path: '/auth',
      name: 'auth',
      redirect: { name: 'dashboard' },
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: () => import('@/pages/DashboardPage.vue'),
    },
    {
      path: '/demo',
      name: 'demo',
      component: () => import('@/pages/DemoPage.vue'),
    },
  ],
})

export default router
