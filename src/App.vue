<template>
  <div id="app">
    <b-navbar toggleable="md" type="dark" class="nav-background">
    <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>
    <b-navbar-brand href="#">XiCAM Plugins</b-navbar-brand>
    <b-collapse is-nav id="nav_collapse">
    </b-collapse>
    </b-navbar>
    <b-container>
      <b-row align-h="center" class="mt-5">
        <b-col cols="12">
          <b-card class="p-3">
            <h3 class="mb-4">Cam-Mart Plugins:</h3>
            <a href="http://cam.lbl.gov:5000/pluginpackages?where={%22name%22:%22xicam.IPython%22}" class="button" style="margin:54px;">Ipython</a>
            <a href="http://cam.lbl.gov:5000/pluginpackages?where={%22name%22:%22xicam.Log%22}" class="button" style="margin:54px;">Log</a>
            <a href="http://cam.lbl.gov:5000/pluginpackages?where={%22name%22:%22xicam.ThreadMonitor%22}" class="button" style="margin:54px;">Thread Monitor</a>
            <a href="http://cam.lbl.gov:5000/pluginpackages?where={%22name%22:%22xicam.SAXS%22}" class="button" style="margin:54px;">SAXS</a>
          </b-card>
        </b-col>
      </b-row>
    </b-container>
    <b-container>
      <b-row align-h="center" class="mt-5">
        <b-col cols="12">
          <b-card class="p-3">
            <h3 class="mb-4">IPython Information:</h3>
            <div class="text">
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
            </div>
          </b-card>
        </b-col>
      </b-row>
    </b-container>            
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

  text {

  }

 
</style>