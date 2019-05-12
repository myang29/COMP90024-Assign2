import Vue from 'vue'
import App from './App.vue'
import VueResource from '../node_modules/vue-resource'
// import axios from 'axios'
// import router from 'vue-router'

import VueAxios from './plugins/axios'

Vue.use(VueAxios)
Vue.use(VueResource);
// Vue.use(axios);

Vue.config.productionTip = false

new Vue({
  // router,
  render: h => h(App),
}).$mount('#app')
