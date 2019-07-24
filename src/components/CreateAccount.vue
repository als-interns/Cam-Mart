<template>
  <div id="app">
    <router-view/>
	<h1>Create an Account</h1>
	<b-form-input v-model="username" placeholder="Username" />
	<br>
	<b-form-input v-model="email" placeholder="Email" />
	<br>
	<b-form-input v-model="password" type="password" placeholder="Password" />
	<br>
	<b-button @click="Create()" >Create an Account</b-button>
	</div>
</template>

<script>
import axios from 'axios'

export default{
	data() {
		return{
			username: '',
			password: '',
			email: '',
		}
	},
	methods: {
		Create(){
			var compile = {
				username: this.username,
				email: this.email,
				password: this.password
			}
			axios.post('http://localhost:9000/users',compile)
		}
	}
}
</script>

<style>

</style>
