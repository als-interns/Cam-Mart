<template>
	<div id="Submit">
		<h1>Submit a plugin</h1>
<!-- plugin name --> 
		<b-form-input v-model="input.name" placeholder="Plugin Name" />
		<b-alert v-model="nameNoInput" variant="danger" dismissible> Cannot be Empty </b-alert>
		<b-alert v-model="nameNotOriginal" variant="danger" dismissible> This Plugin Name Already Exists </b-alert>
		<br>
<!-- version input -->
		<b-form-input v-model="input.Version" placeholder="Version" />
		<b-alert v-model="verNoInput" variant="danger" dismissible> Cannot be empty </b-alert>
		<br>
<!-- description input -->
		<b-form-textarea v-model="input.Description" placeholder="Plugin Description"> </b-form-textarea>
		<b-alert v-model="descNoInput" variant="danger" dismissible> Cannot be empty </b-alert>
		<br>
<!-- install input -->
		<b-form-input v-model="input.Install" placeholder="Install Info" />
		<b-alert v-model="instNoInput" variant="danger" dismissible> Cannot be empty </b-alert>

<!-- authors -->
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
				<b-alert v-model="authNoInput" variant="danger" dismissible> Has to have at least 1 author (don't forget to click "add") </b-alert>
			<hr>
		</div> 
<!-- key words -->
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
				<b-alert v-model="keyNoInput" variant="danger" dismissible> Atleast 1 </b-alert>
			<hr>
		</div> 
<!-- submit button -->
		<b-button @click="compileInfo()"> Submit! </b-button>
		{{ Compiled }}
	</div>
</template>

<script>
/*
NoInput vars are for alert display
errors- 0 - none, 1 - no input, 2 - unoriginal name(not yet)
error[0] - error at name
error[1] - version
error[2] - description
error[3] - install
error[4] - authors
error[5] - plugins ( gone )
error[6] - keywords
Compiled - the JSON sent

*/
import axios from 'axios'
export default{
	data() {
		return{
			nameNotOriginal: false,
			nameNoInput: false,
			verNoInput: false,
			descNoInput: false,
			instNoInput: false,
			authNoInput: false,
			plugNoInput: false,
			keyNoInput: false,
			errors: [0,0,0,0,0,0,0],
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
			if (this.errorCheck(this.input)) {
				var keywords = [];
				var authors = [];
				for(var i = 0; i < this.input.Authors.length; i++){
					authors.push(this.input.Authors[i].name)
				}
				for(var i = 0; i < this.input.Key_Words.length; i++){
					keywords.push(this.input.Key_Words[i].name)
				}
				this.Compiled= {
					name: this.input.name,
					documentation: {
						description: this.input.Description,
						keywords: keywords,
						authors: authors,
						version: this.input.Version},
					installuri: this.input.Install,
					token: this.$store.state.token,
					submitter: this.$store.state.user
				}
				axios.post('http://localhost:9000/addplugin', this.Compiled)
				.catch(error => {
					if(error == 'Error: Request failed with status code 401'){
						this.$router.push({name:'Login'})
					}
				});
			}
		},
		errorCheck(input){
			if(input.name){
				this.errors[0] = 0;
				this.nameNoInput = false;
			}else{
				this.errors[0] = 1;
				this.nameNoInput = true;
			}
			if(input.Version){
				this.errors[1] = 0;
				this.verNoInput = false;
			}else{
				this.errors[1] = 1;
				this.verNoInput = true;
			}
			if(input.Description){
				this.errors[2] = 0;
				this.descNoInput = false; 
			}else{
				this.errors[2] = 1;
				this.descNoInput = true;
			}
			if(input.Install){
				this.errors[3] = 0;
				this.instNoInput = false; 
			}else{
				this.errors[3] = 1;
				this.instNoInput = true; 
			}
			if(input.Authors.length > 0){
				this.errors[4] = 0;
				this.authNoInput = false;
			}else{
				this.errors[4] = 1;
				this.authNoInput = true;
			}
			if(input.Key_Words.length > 0){
				this.errors[6] = 0;
				this.keyNoInput = false;
			}else{
				this.errors[6] = 1;
				this.keyNoInput = true;
			}
			var correct = true;
			for(var i in this.errors){
				if (this.errors[i]){
					correct = false;
				}
			}
			if (!(correct)){
				alert('There has been an error! Please check your input.')
			}
			return correct;
		}
	},
	/*
	mounted: function () {
		if(this.$store.state.user == 'none'){
			this.$router.push({name:'Login'})
		}	
	}*/
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
