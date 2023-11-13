import {createApp} from 'vue'
import axios from 'axios'

import App from '@/App.vue'

import '@/scss/style.scss';
import router from '@/router'

const app = createApp(App)

app.use(router)

app.mount('#app')