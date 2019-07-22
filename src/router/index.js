import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Test from '@/components/Test'
import PluginInfo from '@/components/PluginInfo'
import Login from '@/components/Login'
import Submit from '@/components/Submit'

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
	component: Login
	},
	{
	path: '/Submit',
	component: Submit
	},
  ]
})
