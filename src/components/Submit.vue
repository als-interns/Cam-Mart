<template>
	<div id="Submit">
		<h1>Submit a plugin</h1>
		<b-form-input v-model="input.name" placeholder="Plugin Name" />
		<b-form-input v-model="input.Version" placeholder="Version" />
		<b-form-textarea v-model="input.Description" placeholder="Plugin Description"> </b-form-textarea>
		<b-form-input v-model="input.Install" placeholder="Install Info" />
		<div> 
			<hr>
				<p> Authors: </p>
				<b-table bordered thead-class="hidden_header" small :items="input.Authors" :fields=fields>
					<template slot="remove" slot-scope="row">
						<b-button small @click="doadelete(row.item.id)" > &times </b-button> 
					</template>						
				</b-table>
				<b-form-input v-model="author" placeholder="Add Author" />
				<b-button v-on:click="input.Authors.push({name:author, id: input.Authors.length}), author=''"> Add </b-button> 
			<hr>
		</div> 
		<div> 
			<hr>
				<p> Plugins: </p>
				<b-table bordered thead-class="hidden_header" small :items="input.Plugins" :fields=fields>
					<template slot="remove" slot-scope="row">
						<b-button small @click="doadeleteplugins(row.item.id)" > &times </b-button> 
					</template>						
				</b-table>
				<b-form-input v-model="plugin" placeholder="Add a Plugin" />
				<b-button v-on:click="input.Plugins.push({name:plugin, id: input.Plugins.length}), plugin=''"> Add </b-button> 
			<hr>
		</div> 
		<div> 
			<hr>
				<p> Key Words: </p>
				<b-table bordered thead-class="hidden_header" small :items="input.Key_Words" :fields=fields>
					<template slot="remove" slot-scope="row">
						<b-button small @click="doadeletekeys(row.item.id)" > &times </b-button> 
					</template>						
				</b-table>
				<b-form-input v-model="key_word" placeholder="Add a Key Word" />
				<b-button v-on:click="input.Key_Words.push({name:key_word, id: input.Key_Words.length}), key_word=''"> Add </b-button> 
			<hr>
		</div> 
		<b-button @click="compileInfo()"> Submit! </b-button>
		{{ Compiled }}
	</div>
</template>

<script>
import axios from 'axios'
export default{
	data() {
		return{
			test: '',
			fields: ['name','remove'],
			author: '',
			key_word: '',
			plugin: '', 
			input: {
				name: '',
				version: '',
				Authors: [],
				Description: '',
				Key_Words: [],
				Plugins: [],
				Install: ''
			},
			Compiled: {}
			
		}
	}, 
	methods: {
		doadelete(id){
			this.input.Authors.splice(id,1)
			for(var i=0; i<this.input.Authors.length; i++){
				this.input.Authors[i].id = i;
			}
		},
		doadeletekeys(id){
			this.input.Key_Words.splice(id,1)
			for(var i=0; i<this.input.Key_Words.length; i++){
				this.input.Key_Words[i].id = i;
			}
		},
		doadeleteplugins(id){
			this.input.Plugins.splice(id,1)
			for(var i=0; i<this.input.Plugins.length; i++){
				this.input.Plugins[i].id = i;
			}
		},
		compileInfo(){
			var plugins = [];
			var keywords = [];
			var authors = [];
			for(var i = 0; i < this.input.Plugins.length; i++){
				plugins.push(this.input.Plugins[i].name)
			}
			for(var i = 0; i < this.input.Authors.length; i++){
				authors.push(this.input.Authors[i].name)
			}
			for(var i = 0; i < this.input.Key_Words.length; i++){
				keywords.push(this.input.Key_Words[i].name)
			}
			this.Compiled= {
				name: this.input.name,
				plugins: plugins,
				documentation: {
					description: this.input.Description,
					keywords: keywords,
					authors: authors,
					version: this.input.Version},
				installuri: this.input.Install
			}
			axios.post('http://localhost:9000/cam', this.Compiled);
		}
	}
}

</script>

<style>
.hidden_header{
display:none;
}
hr{
border: none;
height: 5px;
background-color: #000000
}
</style>
