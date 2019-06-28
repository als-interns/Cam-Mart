<template>
  <div id="app">
    <router-view/>
    <h1> {{ msg }} </h1>
    <li v-for="item in values._items" style="list-style: none;">
    <button class="plugins" v-on:click="display = item.documentation.description; show = true;">
      {{ item.plugins[0] }}
    </button>
    </li>
    <p v-if="show"> {{ display }}
    <button v-on:click="show = false">X</button>
    <div class = "pages">
    <button class="back" v-if="page != 1" v-on:click="page -= 1"> <--Previous Page </button>
    {{ page }}
    <button class="next" v-on:click="page += 1"> Next Page--> </button>
    </div>
    </p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  data () {
    return {
      values: {},
      display: '',
      msg: 'plugins',
      show: false,
      page: 1,
      test: 1
    }
  },
  mounted () {
    axios.get('http://131.243.88.16:5000/plugins')
      .then(response => (this.values = response.data))
  }
}

</script>

<style>
.plugins{
background-color:white;
border-style:groove;
margin: 0px;
height:50px;
width:100%;
padding-right:100px;
box-sizing: border-box;
font-size: 24px;
cursor:pointer;
text-align: left;
}
.plugins:hover{
background-color:#cecece;
}
.next{
float:right;
}
.pages{
text-align:center
}
.back{
float:left;
}
</style>
