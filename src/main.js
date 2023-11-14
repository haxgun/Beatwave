import App from '@/App.vue'
import '@/assets/style.scss'
import router from '@/router'
import 'primeicons/primeicons.css'
import Button from 'primevue/button'
import ColorPicker from 'primevue/colorpicker'
import PrimeVue from 'primevue/config'
import InputSwitch from 'primevue/inputswitch'
import InputText from 'primevue/inputtext'
import 'primevue/resources/themes/lara-light-teal/theme.css'
import { createApp } from 'vue'

const app = createApp(App)

app.use(PrimeVue, { ripple: true })
app.use(router)

app.component('InputSwitch', InputSwitch)
app.component('InputText', InputText)
app.component('ColorPicker', ColorPicker)
app.component('Button', Button)
app.mount('#app')
