<template>
  <div id="app">
	<b-navbar type="light" variant="info">
		<b-navbar-brand href="#/home">Cam-Mart</b-navbar-brand>
		<b-navbar-nav>
		<b-nav-item href="#/home">Home</b-nav-item>
		<b-nav-item href="#/Login">Login</b-nav-item>
		<b-nav-item href="#/Submit">Submit a Plugin</b-nav-item>
		</b-navbar-nav>
	</b-navbar>
	<br>
	<router-view/>
	</div>
</template>

<script>

import axios from 'axios'
/*
showlogin - boolean to show login
page - pages (not working, just a template)
ispageone - boolean by default is true to prevent from going into negative pages
loggedin - boolean
*/
export default {
  name: 'Home',
  data () {
    return {
	  indplugin: {},
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
	  ],
	  submit: function () {
		if (!(this.loggedin)){
			alert("Log in or create an account")
		}else{
			this.$bvModal.show("submit")
		}
	  }
    }
  }
}

</script>

<style>

</style>
