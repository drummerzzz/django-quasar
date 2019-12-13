import Vue from 'vue'
import App from '@/App.vue'

import store from '@/store'
import router from '@/router'
import Buefy from 'buefy'
import 'buefy/dist/buefy.css'

// import '../src/assets/css/style.css'

Vue.use(Buefy)


Vue.config.productionTip = false

// Vue.use(VueRouter)

const vue = new Vue({
  router,
  store,
  render: h => h(App)
})

vue.$mount('#app')
