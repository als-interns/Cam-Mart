<template>
  <div id="app">
    <b-navbar toggleable="md" type="dark" class="nav-background">
    <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>
    <b-navbar-brand href="#">XiCAM Plugins</b-navbar-brand>
    <b-collapse is-nav id="nav_collapse">
    </b-collapse>
     <b-navbar-nav class="ml-auto">
      <b-nav-form>
        <b-form-input size="sm" class="mr-sm-2" type="text" placeholder="Search"/>
        <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
      </b-nav-form>
      <b-nav-item-dropdown text="Lang" right>
        <b-dropdown-item href="#">EN</b-dropdown-item>
        <b-dropdown-item href="#">ES</b-dropdown-item>
        <b-dropdown-item href="#">RU</b-dropdown-item>
        <b-dropdown-item href="#">FA</b-dropdown-item>
      </b-nav-item-dropdown>
      <b-nav-item-dropdown right>
        <template slot="button-content">
          <em>User</em>
        </template>
        <b-dropdown-item href="#">Profile</b-dropdown-item>
        <b-dropdown-item href="#">Signout</b-dropdown-item>
      </b-nav-item-dropdown>
    </b-navbar-nav>
    </b-navbar>
    
    <b-container>
      <b-row align-h="center" class="mt-5">
        <b-col cols="12">
          <b-card class="p-3">
            <h3 class="mb-4">Cam-Mart Plugin Installation:</h3>
            <a href="https://pypi.org/project/xicam.ipython/#files" class="button" style="margin:54px;" target="_blank">Ipython</a>
            <a href="https://pypi.org/project/xicam.log/" class="button" style="margin:54px;" target="_blank">Log</a>
            <a href="https://pypi.org/project/xicam.threadmonitor/" class="button" style="margin:54px;" target="_blank">Thread Monitor</a>
            <a href="https://pypi.org/project/xicam.SAXS/" class="button" style="margin:54px;" target="_blank">SAXS</a>
          </b-card>
        </b-col>
      </b-row>
    </b-container>
    <b-container>
      <b-row align-h="center" class="mt-5">
        <b-col cols="3">
          <b-card class="p-3">
            <h3 class="mb-2"></h3>
              <div>
                  <b-dropdown id="dropdown-1" text="Plugin Information" class="m-md-1">
                  <b-dropdown-item>IPython</b-dropdown-item>
                  <b-dropdown-item>Log</b-dropdown-item>
                  <b-dropdown-item>Thread Monitor</b-dropdown-item>
                   <b-dropdown-item>SAXS</b-dropdown-item>
                </b-dropdown>
              </div>
          </b-card>
        </b-col>
      </b-row>
    </b-container>
    <br><br><br><br>
    <b-container>
      <b-row align-h="center" class="mt-5">
        <b-col cols="12">
          <b-card class="p-3">
            <h3 class="mb-4">IPython Information:</h3>
            <div class="text">
              <p>Name: xicam.Ipython</p>
              <p>Description: An IPython console interface which exposes all internal variables of Xi-cam. You can use this to freely manipulate data in Xi-cam.</p>
              <p>Version: 0.1.0</p>
            </div>
          </b-card>
        </b-col>
      </b-row>
    </b-container>
    <b-container>
      <b-row align-h="center" class="mt-5">
        <b-col cols="12">
          <b-card class="p-3">
            <h3 class="mb-4">Log Information:</h3>
            <div class="text">
              <p>Name: xicam.log</p>
              <p>Description: A logging display which exposes history of logged messages for debugging purposes.</p>
              <p>Version: 0.1.0</p>
            </div>
          </b-card>
        </b-col>
      </b-row>
    </b-container>
    <b-container>
      <b-row align-h="center" class="mt-5">
        <b-col cols="12">
          <b-card class="p-3">
            <h3 class="mb-4">Thread Monitor Information:</h3>
            <div class="text">
              <p>Name: xicam.threadmonitor</p>
              <p>Description: A built-in plugin for tracking status of threads.</p>
              <p>Version: 0.1.0</p>
            </div>
          </b-card>
        </b-col>
      </b-row>
    </b-container>
    <b-container>
      <b-row align-h="center" class="mt-5">
        <b-col cols="12">
          <b-card class="p-3">
            <h3 class="mb-4">SAXS Information:</h3>
            <div class="text">
              <p>Name: xicam.SAXS</p>
              <p>Description: A package of plugins for SAXS/WAXS data reduction.</p>
              <p>Version: 0.1.0</p>
            </div>
          </b-card>
        </b-col>
      </b-row>
    </b-container> 
    <br><br>  
             
  </div>
</template>

<script>
</script>

<style>
  body {
    background: #EEF1F4 !important;
    font-family: 'Lato', sans-serif !important;
  }
  .nav-background {
    background: #353535;
  }
  .button {
    font-family: "proxima nova";
    font-weight: 100;
    font-size: 30px;
    text-align: center;
    color: #000000;
    border: solid 2px #353535;
    border-radius: 50px;
    padding: 10px 20px;
    transition-duration: 200ms;
    -webkit-transition-duration: 200ms;
  }

  .button:hover {
    background-color: #353535;
    color: #fff;

  }

  .text {
    background: #c7c3c3;
    font-family: "proxima nova";
    font-weight: 100;
    font-size: 20px;
    text-align: left;
    color: #000000;
    border: solid 2px #f0eded;
    border-radius: 10px;
    padding: 10px 20px;
  }



 
</style>