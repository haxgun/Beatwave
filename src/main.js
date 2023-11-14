import { createApp } from 'vue'

import App from '@/App.vue'

import PrimeVue from 'primevue/config'
import InputSwitch from 'primevue/inputswitch'
import InputText from 'primevue/inputtext'
import ColorPicker from 'primevue/colorpicker';


import 'primevue/resources/themes/lara-light-teal/theme.css'

import '@/assets/style.scss'
import router from '@/router'

const app = createApp(App)

app.use(PrimeVue, { ripple: true })
app.use(router)

app.component('InputSwitch', InputSwitch)
app.component('InputText', InputText)
app.component('ColorPicker', ColorPicker)
app.mount('#app')
