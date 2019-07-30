<template>
  <div id="app">
    <router-view/>
	<h1>Login</h1>
	{{ response }}
	<br>
	{{ this.$store.state.user }}
	<hr>
		<b-form-input v-model="input.username" placeholder="Username" />
		<br>
        <b-form-input v-model="input.password" class="password" type="password" name="password" placeholder="Password" />
        <br>
		<p> {{ input.username }}  {{ input.password }} </p>
		<b-button @click="Login()">Login</b-button>
		<br>
		<b-button> Login with Google</b-button>
		<br>
		<b-button> Login with ORCID </b-button>
		<div class="g-signin2"></div>
	</div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Login',
  data () {
    return {
		response: 'none yet',
		input: {
			username:'',
			password:''
		}
	  }
    },
	methods: {
		Login(){
			//if(this.$store.state.user == 'none'){
			axios.post('http://localhost:9000/login', {username:this.input.username, password:this.input.password})
			.then(response => this.response = response.data)
			//}
		}
	},
	watch: {
		response: function(){
			if(this.response != 'fail'){
				this.$store.commit('newUser', this.input.username)
			}
			this.$store.commit('newToken', this.response)
		}
	}
  }
</script>

<style>
b-form-input{
width: 50% !important; 
}
</style>
