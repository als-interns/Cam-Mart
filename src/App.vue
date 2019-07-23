<template>
  <div id="app">
	<b-navbar type="light" variant="info">
		<b-navbar-brand href="#/home">Cam-Mart</b-navbar-brand>
		<b-navbar-nav>
		<b-nav-item href="#/home">Home</b-nav-item>
		<b-nav-item href="#/Login">Login</b-nav-item>
		<b-nav-item href="#/Submit">Submit a Plugin</b-nav-item>
		<b-nav-item href="#/Profile">Profile</b-nav-item>
		</b-navbar-nav>
	</b-navbar>
	<br>
	<router-view/>
	</div>
</template>

<script>

import axios from 'axios'
/*

*/
export default {
  name: 'Home',
  data () {
    return {
	  loggedin: false,
      user: '',
	  navfields: [
		{
		text: 'Home',
		href: '#/home'
		},
		{
		text: 'Login', 
		href: '#/Login'
		},
		{
		text: 'Test', 
		href: '#/Test'
		},
		{
		text: 'Cam-mart', 
		}
	  ]
    }
  }
}

</script>

<style>

</style>
