<template>
  <div id="app">
    <router-view/>
    <div class="modal-mask" v-if="show">
    <div class="modal-box" style="padding:20px;">
      <button class="closer" v-on:click="show = false;" style="float:right;"><b>X</b></button>
        <div>
        <p class="title"><b>{{ information.pluginname }}</b></p>
        <p>by:</p>
        <li class='theauthors' v-for="author in information.authors"> {{ author }}, </li>
        <p>Version {{ information.version }} </p>
        <p style="font-size:14px">Created on {{ information.datecreated }},<br> last updated on {{ information.dateupdated }}
        <hr>
        </div>
        <p> {{ information.desc }} </p>
        <p>Install by: {{ information.install }} </p>
        <p>id: {{ information.id }}<br> etag: {{ information.etag }} </p>
      </div>
    </div>
    <div class="modal-mask" v-if="showlogin">
        <div class="modal-box">
        <button class="closer" v-on:click="showlogin = false;" style="float:right;"><b>X</b></button>
        <p class = "title"><b>Login</b></p>
        <input type="text" name="username" v-model="input.username" placeholder="Username" />
        <br>
        <input type="password" name="password" v-model="input.password" placeholder="Password" />
        <br>
        <button class="loginbtn">Login!</button>
    </div>
    </div>
    <div class="header">
      <div class="top">
        <ul class="navigation">
          <li class="login"> <button v-on:click="showlogin=true">Login</button></li>
          <li><button>Logout</button></li>
        </ul>
      </div>
    <h1> {{ title }} </h1>
    </div>
    <div class="plugin-boxes">
    <li v-for="item in values._items" style="list-style: none;">
    <button class="plugins" v-on:click="show = true; displayinfo(item)">
      {{ item.name }}
    </button>
    </li>
    </div>
    <div class = "pages">
    <button class="back" v-bind:class="{'page1':ispageone }" v-on:click="backpage();"> &lt;--Previous Page </button>
    {{ page }}
    <button class="next" v-on:click="page += 1; ispageone = false"> Next Page--> </button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*'

export default {
  name: 'App',
  data () {
    return {
      values: {},
      title: 'plugins',
      show: false,
      showlogin: false,
      page: 1,
      ispageone: true,
      input: {
        username: '',
        password: ''
      },
      information: {
        'pluginname': '',
        'authors': {},
        'etag': '',
        'id': '',
        'version': '',
        'dateupdated': '',
        'install': '',
        'desc': '',
        'datecreated': ''
      },
      displayinfo: function (plugin) {
        this.information.pluginname = plugin.name.substring(6)
        this.information.authors = plugin.documentation.authors
        this.information.etag = plugin._etag
        this.information.id = plugin._id
        this.information.version = plugin.documentation.version
        this.information.dateupdated = plugin._updated
        this.information.install = plugin.installuri
        this.information.desc = plugin.documentation.description
        this.information.datecreated = plugin._created
        // make request for the display info for a plugin
      },
      backpage: function () {
        if (this.page !== 1) {
          this.page -= 1
        }
        if (this.page === 1) {
          this.ispageone = true
        }
      }
    }
  },
  mounted () {
    axios.get('http://localhost:5000/plugins') // change this to official plugin link
      .then(response => (this.values = response.data))
  }
}

</script>

<style>
.plugins{
background-color:#fafafa;
border-style:groove;
color:black;
margin: -1px;
height:50px;
width:100%;
padding-right:100px;
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
margin-top:20px;
margin-bottom:auto;
background-color: #fff;
overflow: auto;
line-height: auto;
}
.closer{
border-radius: 100px;
background-color: #ff0000;
border-style:solid;
}
.closer:hover{
background-color:#bd0000;
cursor: pointer;
}
.title{
text-align:center;
font-size:30px;
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
.navigation li{
display: inline-block;
text-align:right;
padding: 10px 5px 10px 0px;
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
</style>
