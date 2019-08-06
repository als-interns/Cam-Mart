<template>
	<div id="profile">
		<h1> {{ user }}'s Profile </h1>
		<p> about </p>
		<p> contributed plugins</p>
		<p> {{ this.$gAuth.getAuthCode() }} </p>
	</div>
</template>

<script>
export default{
	data() {
		return{
		user: this.$route.params.user
		}
	},
	methods: {
	
	}
}
</script>

<style>

</style>
