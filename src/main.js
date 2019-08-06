// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
// import axios from 'axios'
import Vue from 'vue'
import App from './App'
import router from './router'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import Vuex from 'vuex'
import GAuth from 'vue-google-oauth2'




Vue.config.productionTip = false

/* eslint-disable no-new */
Vue.use(BootstrapVue)
Vue.use(Vuex)

const gauthOption = {
		clientId: '978857662335-vf2tkju8rgvtqr6f1vqp6jh7948ovdsj.apps.googleusercontent.com',
		prompt: 'select_account',
}

Vue.use(GAuth, gauthOption)

const store =  new Vuex.Store({
	state: {
		user: 'none',
		token: '',
	},
	mutations: {
		newUser(state, theuser) {
			state.user = theuser
		},
		newToken(state, token){
			state.token = token
		}
	}
})
//Vue.prototype.$user = {username: 'none'}

new Vue({
  el: '#app',
  store,
  router,
  render: h => h(App),
  components: { App },
  template: '<App/>'
})
