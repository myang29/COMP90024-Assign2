import Vue from 'vue'
import App from './App.vue'

import { Icon }  from 'leaflet'
import 'leaflet/dist/leaflet.css'
import VueResource from '../node_modules/vue-resource'
import './scss/main.scss';

import VueAxios from './plugins/axios'

import VueWordCloud from 'vuewordcloud';
Vue.component(VueWordCloud.name, VueWordCloud);
// this part resolve an issue where the markers would not appear
delete Icon.Default.prototype._getIconUrl;
Icon.Default.mergeOptions({
  iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
  iconUrl: require('leaflet/dist/images/marker-icon.png'),
  shadowUrl: require('leaflet/dist/images/marker-shadow.png')
});
Vue.use(VueAxios)
Vue.use(VueResource);

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
