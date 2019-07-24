<template>
	<div>
		<div>
			<button class="closer" v-on:click="exit()"> &times </button>  
			<h1>{{ this.$route.params.name }} </h1>
			<hr> 
				<div v-if="!PluginInfo.info">
					<p> version {{ PluginInfo.documentation.version }} </p>
					<p> Authors: {{ PluginInfo.documentation.authors}} </p>
					<p> {{ PluginInfo.documentation.description}} </p>
					<p>Created on {{ PluginInfo._created}} </p>
					<p> Last Updated on {{ PluginInfo._updated}} </p>
					<p> Key Words: <ul class="list" v-for="item in PluginInfo.documentation.keywords"> {{ item }}, </ul> </p>
					<p> Install at <br> {{ PluginInfo.installuri }} </p>
					<!-- <p> {{ PluginInfo.resource}} </p> -->
				</div>
				<div class="text-center"> 
					<b-spinner v-if="PluginInfo.info" label="Spinning"></b-spinner>
				</div>
				<!-- <p> Test
				{{ PluginInfo }}
				<hr>
				{{ link }}
				<hr>
				{{ Test }}
				<hr>
				</p> -->
				<hr>
		</div>
	</div>
</template>

<script>
import axios from 'axios'
export default {
	Name: 'plugin', 
	data() {
		return {
			PluginInfo: {info:"error"},
			Test: '',
			name: this.$route.params.name,
			link: 'http://localhost:9000/cam/' + this.$route.params.name
		}
	},
	methods: {
	exit(){
	this.$router.go(-1)
	}
	},
	mounted () {
    axios.get(this.link)
      .then(response => (this.PluginInfo = response.data, this.Test=response.data))
	  .catch(function (error) {
		alert(error);
	  })
	}
}
// [ /\()}{ ]
</script>

<style>
.closer{
float: right;
font-size: 45px;
margin: 0px;
padding: 0px;
height: 30px;
width: 30px;
text-align: center;
vertical-align: middle;
line-height: 30px;
}
.list{
list-style-type: none;
display: inline;
padding: 0;
}
p{
padding-left: 10px;
}
</style>
