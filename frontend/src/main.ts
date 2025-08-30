import { createApp } from 'vue'

import { i18n } from '@/i18n'
import { createPinia } from 'pinia'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import App from './App.vue'
import './assets/main.css'
import router from './router'

const pinia = createPinia().use(piniaPluginPersistedstate)
const app = createApp(App)

app.use(i18n).use(pinia).use(router).mount('#app')
