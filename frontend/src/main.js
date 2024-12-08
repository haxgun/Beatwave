import App from '@/App.vue'
import '@/assets/style.scss'
import router from '@/router'
import 'primeicons/primeicons.css'
import Button from 'primevue/button'
import ColorPicker from 'primevue/colorpicker'
import PrimeVue from 'primevue/config'
import Dropdown from 'primevue/dropdown'
import InputSwitch from 'primevue/inputswitch'
import InputText from 'primevue/inputtext'
import 'primevue/resources/themes/lara-light-teal/theme.css'
import Slider from 'primevue/slider'
import { createApp } from 'vue'

const app = createApp(App)

app
  .use(PrimeVue, { ripple: true })
  .use(router)
  .component('InputText', InputText)
  .component('ColorPicker', ColorPicker)
  .component('InputSwitch', InputSwitch)
  .component('Slider', Slider)
  .component('Dropdown', Dropdown)
  .component('Button', Button)
  .mount('#app')
