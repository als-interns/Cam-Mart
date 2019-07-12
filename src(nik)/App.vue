<template>
  <div id="app">
    <router-view/>
	                                    <!-- plugin info element -->
    <div class="modal-mask" v-if="show">
    <div class="modal-box" style="padding:20px;">
      <button class="closer" v-on:click="show = false;"><b>X</b></button>
        <div>
        <p class="title"><b>{{ information.pluginname }}</b></p>
        <span class="text">by:</span>
        <li v-bind:key="author" class='theauthors text' v-for="author in information.authors" style="display: inline-block;"> {{ author }}, </li>
        <p class="text">Version {{ information.version }} </p>
        <p class="text" style="font-size:14px">Created on {{ information.datecreated }},<br> last updated on {{ information.dateupdated }}
        <hr>
        </div>
        <p class="text"> {{ information.desc }} </p>
        <p class="text" style="display: inline-block;"> Key-Words:&nbsp;
        <li class="text" v-bind:key="keys" v-for="keys in information.keywords" style="display: inline-block; text-transform: capitalize;"> {{ keys }},&nbsp; </li>
        <p class="text">Install by: {{ information.install }} </p>
        <p class="text">id: {{ information.id }}<br> etag: {{ information.etag }} </p>
      </div>
    </div>
	                                    <!-- login template display -->
    <div class="modal-mask" v-if="showlogin">
        <div class="modal-box">
        <button class="closer" v-on:click="showlogin = false;input.username='';input.password='';"><b>X</b></button>
        <p class = "title"><b>Login</b></p>
        <b-form-input v-model="input.username" placeholder="Username" />
        <br>
        <b-form-input class="password" type="password" name="password" v-model="input.password" placeholder="Password" />
        <br>
        <button class="loginbtn" v-on:click="loggedin=true; showlogin=false; user=input.username; input.username='';input.password=''">Login!</button>
    </div>
    </div>
	                                    <!-- top/header -->
    <div class="header">
      <div class="navigation">
        <b-button-group>
          <b-button variant="primary" v-on:click="showlogin=true">Login</b-button>
          <b-button variant="info" v-on:click="loggedin=false; user=''">Logout</b-button>
		  <b-button v-b-popover.hover.bottom="'You must have an account and login in order to submit a plugin'" variant="dark" v-on:click="submit();">
		  Submit a Plugin
		  </b-button>
        </b-button-group>
		<p class="user">Signed in as {{ user }}</p>
      </div>
    <h1> {{ title }} </h1>
	                                    <!-- submit plugin modal -->
	<b-modal id="submit" title="Submit Your Modal">
	<b-form-input v-model="pluginsubmit.name" placeholder="Plugin Name" />
	<b-form-input v-model="pluginsubmit.authors" placeholder="Authors" />
	<b-form-textarea v-model="pluginsubmit.name" placeholder="Description" />
	<b-form-input v-model="pluginsubmit.name" placeholder="Version" />
	<b-form-input v-model="pluginsubmit.name" placeholder="download link?" />
	</b-modal>
    </div>
    <div class="plugin-boxes">
	                                        <!-- list of plugins -->
    <li v-bind:key="item._id" v-for="item in values._items" style="list-style: none;">
    <button class="button" v-on:click="show = true; displayinfo(item)">
      {{ item.name }}
    </button>
    </li>
    </div>
	                                        <!-- pagination template/test -->
    <div class = "pages">
    <button class="back pagebtn text" v-bind:class="{'page1':ispageone }" v-on:click="backpage();"> &lt;--Previous Page </button>
    <span class="text"> page {{ page }} </span>
    <button class="next pagebtn text" v-on:click="page += 1; ispageone = false"> Next Page--> </button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
/*
vales - stores the request
title - basically the header
show - boolean to show plugin info box
showlogin - boolean to show login
page - pages (not working, just a template)
ispageone -  boolean by default is true to prevent from going into negative pages
input - login input(leared when login is closed)
information - info to display for a plugin
indplugin - stores request to an individual plugin
loggedin - boolean
*/
export default {
  name: 'App',
  data () {
    return {
      values: {},
      title: 'Plugins',
      show: false,
      showlogin: false,
      page: 1,
      ispageone: true,
	  indplugin: {},
	  loggedin: false,
	  showsubmit: false,
      user: '',
	  pluginsubmit: {
	  name:'',
	  authors: '',
	  version: '',
	  desc: '',
	  download: ''
	  },
	  input: {
        username: '',
        password: ''
      },
      information: {
        'pluginname': '',
        'authors': {},
        'keywords': {},
        'etag': '',
        'id': '',
        'version': '',
        'dateupdated': '',
        'install': '',
        'desc': '',
        'datecreated': ''
      },
      displayinfo: function (plugin) {
        var requestURL ="http://cam.lbl.gov:5000/pluginpackages?where={%22name%22:%22" + plugin.name + "%22}"
	    axios.get(requestURL) 
        .then(response => (this.indplugin = response.data))
        this.information.pluginname = plugin.name
        this.information.authors = plugin.documentation.authors
        this.information.etag = plugin._etag
        this.information.id = plugin._id
        this.information.version = plugin.documentation.version
        this.information.dateupdated = plugin._updated
        this.information.install = plugin.installuri
        this.information.desc = plugin.documentation.description
        this.information.datecreated = plugin._created
        this.information.keywords = plugin.documentation.keywords
      },
      backpage: function () {
        if (this.page !== 1) {
          this.page -= 1
        }
        if (this.page === 1) {
          this.ispageone = true
        }
      },
	  submit: function () {
		if (!(this.loggedin)){
			alert("Log in or create an account")
		}else{
			this.$bvModal.show("submit")
		}
	  }
    }
  },
  mounted () {
    axios.get('http://localhost:9000/cam')
      .then(response => (this.values = response.data))
  }
}

</script>

<style>
.plugins{
background-color:#fafafa;
border-style:groove;
color:black;
margin: 0px;
height:50px;
width:100%;
padding-right:10px;
box-sizing: border-box;
font-size: 24px;
cursor:pointer;
text-align: left;
}
.plugins:hover{
background-color:#808080;
color:white;
}
.plugins:active{
background-color:#666666;
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
.pagebtn{
font-family: "proxima nova";
font-weight: 100;
font-size: 30px;
text-align: center;
color: #000000;
border: solid 2px #353535;
border-radius: 50px;
padding: 0px 7px;
transition-duration: 200ms;
-webkit-transition-duration: 200ms;
}
.pagebtn:hover {
background-color: #353535;
color: #fff;
}
.page1{
cursor: not-allowed !important;
}
.modal-mask{
position:fixed;
z-index: 9998;
width:100%;
height:100%;
background-color: rgba(0, 0, 0, 0.5);
overflow: scroll;
}
.modal-box{
position: center;
width:60%;
height:80%;
top:50px;
margin-right:auto;
margin-left:auto;
margin-top:50px;
margin-bottom:auto;
background-color: #fff;
overflow: auto;
line-height: auto;
padding: 10px;
}
.closer{
border-radius: 50%;
background-color: #ff0000;
border-style:solid;
height: 28px;
width: 28px;
float: right;
}
.closer:hover{
background-color:#bd0000;
cursor: pointer;
}
.closer b{
position:relative;
margin: auto;
}
.title{
text-align:center;
font-size:30px;
font-family: "proxima nova";
}
.theauthors{
distplay:inline;
list-style:none;
}
button{
cursor: pointer;
}
.plugin-boxes{
overflow-y:scroll;
}
.top{
text-align:right;
background-color: #d4d4d4;
}

.top button{
background-color:#f2f2f2;
border-radius:5px;
padding: 5px;
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
font-family: "proxima nova";
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
font-family: "proxima nova";
font-weight: 100;
font-size: 20px;
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
