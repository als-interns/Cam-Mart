import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Test from '@/components/Test'
import PluginInfo from '@/components/PluginInfo'
import Login from '@/components/Login'
import Submit from '@/components/Submit'
import Profile from '@/components/Profile'
import CreateAccount from '@/components/CreateAccount'
Vue.use(Router)

export default new Router({
  routes: [
	{
	path: '/',
	component: Home
	},
	{
    path: '/test',
	component: Test
    }, 
	{
	path: '/home',
	redirect: '/home/page/1'
	},
	{
	path: '/home/page/:page',
	component: Home,
	name: 'home'
	},
	{
	path: '/viewPlugin/:name',
	component: PluginInfo,
	name: 'plugin'
	},
	{
	path: '/login',
	component: Login,
	name: 'Login'
	},
	{
	path: '/Submit',
	component: Submit
	},
	{
	path: '/Profile/:user',
	component: Profile
	},
	{
	path: '/CreateAccount',
	component: CreateAccount
	}
  ]
})
