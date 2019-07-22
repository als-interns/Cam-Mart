<template>
  <div id="Home">
	                                        <!-- list of plugins -->
	<div class="tablebox">
    <b-table 
	id="ptable"
	striped 
	hover 
	selectable
	responsive = "sm"
    :select-mode="'single'"
    selectedVariant="success"
	:items="values._items" 
	:fields="fields"
	:current-page="page"
	:per-page="perpage"
	@row-selected="rowSelected"
	></b-table>
	<div class="text-center"> 
		<b-spinner v-if="values.test" label="Spinning"></b-spinner>
	</div>
	<div 
	<b-pagination
		align="center"
		v-model="page"
		:per-page="perpage"
		:total-rows="values._meta.total"
		aria-controls="ptable"
		@change="pageChange"
		>
	</b-pagination>
	</div>
	
	</div>
	
  </div>
</template>

<script>
import axios from 'axios'
/*
values - stores the request
title - basically the header
show - boolean to show plugin info box
showlogin - boolean to show login
page - pages (not working, just a template)
ispageone - boolean by default is true to prevent from going into negative pages
loggedin - boolean
*/
export default {
  name: 'Home',
  data () {
    return {
	  perpage: 5,
      values: {test:"true"},
      showlogin: false,
      page: this.$route.params.page,
      ispageone: true,
	  loggedin: false,
	  showsubmit: false,
      user: '',
	  selected:{},
	  fields: {
			name: {
				label: 'Plugin Name',
				sortable: true
			}, 
			version: {
				label: 'Version',
				sortable: false,
				key: 'documentation.version'
			}
	  }
	  }
    },
	components: {
		
	},
    methods: {
	  pageChange(page){
		this.$router.push({name: 'home', params: {page: page}})
	  },
      rowSelected(items) {
        this.selected = items
		this.$router.push({name: 'plugin', params: {name: this.selected[0].name}})
     }
	},
  mounted () {
    axios.get('http://localhost:9000/cam')
      .then(response => (this.values = response.data))
  }
}

</script>

<style>
.tablebox{
height: 500px;
}

.next{
float:right;
}
.pages{
text-align:center;
}
.back{
float:left;
}

.page1{
cursor: not-allowed !important;
}

button{
cursor: pointer;
}
.top{
text-align:right;
background-color: #d4d4d4;
}

input{
margin:10px;
}
.loginbtn{
margin:10px;
}
body {
background: #ffffff !important;
font-family: 'Lato', sans-serif !important;
}
.navigation{
background: #4a8fff;
width: 100%;
}
.button {
font-weight: 100;
font-size: 30px;
text-align: center;
color: #000000;
border: solid 2px #353535;
border-radius: 10px;
padding: 0px 0px;
transition-duration: 200ms;
-webkit-transition-duration: 200ms;
width:100%;
}
.button:hover {
background-color: #353535;
color: #fff;
}
.text{
font-weight: 50;
font-size: 16px;
text-align: left;
}
.user{
float: right;
position:relative;
}
.modal-backdrop{
background-color: rgba(0,0,0,0.5) !important;
}
</style>
