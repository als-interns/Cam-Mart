<template>
  <div id="app">
    <router-view/>
	<h1>Login</h1>
	<hr>
		<b-form-input v-model="input.username" placeholder="Username" />
		<br>
        <b-form-input v-model="input.password" class="password" type="password" name="password" placeholder="Password" />
        <br>
		<p> {{ input.username }}  {{ input.password }} </p>
		<b-button>Login</b-button>
	</div>
</template>

<script>
export default {
  name: 'Login',
  data () {
    return {
		input: {
			username:'',
			password:''
		}
	  }
    }
  }
</script>

<style>
b-form-input{
width: 50% !important; 
}
</style>
