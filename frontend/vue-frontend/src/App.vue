<template>
  <div id="app">

    <!-- HEADER -->
    <div v-bind:class="header-container">
      <header>
        <h1>Team Name</h1>
        <nav>
          <!-- unordered list for listing nav -->
          <ul class="nav" id="nav">
            <!--# in a link means no location -->
            <li> <a href="#">Real-Time Data</a> </li>
            <li> <a href="#">Past Data</a> </li>
            <li> <a href="#">Overall</a> </li>
          </ul>
        </nav>
      </header>
    </div>

    <!-- Wrath Type -->
    <WrathTypeData class="wrath-types"/>

    <!-- Centre MAP -->
    <Map class="central-map-container"/>

    <!-- Filter data -->
    <FilterData class="filter-container"/>

    <!-- Keywords rank -->
    <KeywordsRank class="keywords-rank-container"/>

    <!-- Real-time wrath data -->
    <RealtimeData class="real-time-container"/>

    
  
  </div>
</template>

<script>
import Map from './components/Map/Map.vue';
import FilterData from './components/FilterData/FilterData.vue';
import RealtimeData from './components/RealtimeData/RealtimeData.vue';
import WrathTypeData from './components/WrathTypeData/WrathTypeData.vue';
import KeywordsRank from './components/KeywordsRank/KeywordsRank.vue';

export default {
  name: 'app',
  // combine all components 
  components: {
    Map,
    FilterData,
    RealtimeData,
    WrathTypeData,
    KeywordsRank
  }
}
</script>

<style>
@import url('http://fonts.googleapis.com/css?family=Montserrat:400,600');
#app {
  /* font-family: 'Avenir', Helvetica, Arial, sans-serif; */
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  /* color: #2c3e50; */
  /* margin-top: 60px; */

  /* space from most left */
  margin: 0;
  font-family: 'Montserrat', sans-serif;
  color: black;
  background: white;

  /* content: "";
  display:block;
  clear: both; */
}

.h1, subhead {
    position: relative;
    z-index: 3;
}


.header-container {
  text-align: center;
  /* padding: 0.8em 1.2em 2em 40; */
  padding: 0.8em 1.2em;
  background-color: yellow;
  width: 100%;
  height: 30px;
  border: 5px black;
    
}

.nav {
  width: 50%;
  margin: 0px auto;
  text-align: center;
  /* padding: 0.8em 1.2em 2em 40; */
  padding: 0.8em 1.2em;
}
/* for nav bar to show horizonally */
nav ul {
  position: inherit;
  widows: auto;
  background: none;
  height: auto;
  display: flex;
  padding-top: 0;
}
nav ul li {
  /* margin: 0px auto; */
  float: left;
}
nav ul li a {
  background-color: inherit;
  text-align: center;
  padding: 1em 2em;
}
nav ul li a:hover {
  background-color: inherit;
}

/* apply to all unordered lists */
ul {
  /* remove bullet point */
  list-style-type: none;
  margin: 0;
  padding: 0;
}

/* wrath type container */
.wrath-types {
  text-align: center;
  /* #00C2FF */
  background: rgb(216, 216, 252);
  color: #2c3e50;
  width: 20%;
  border-radius: 10px;
  block-size: 24.6em;
  /* display: inline-block; */
  float: right;

}

/* Map container */
.central-map-container {
  margin-right:-2%;
  text-align: center;
  width: 65%;
  border-radius: 10px;
  block-size: 20em;
  float: right;
  color: #2c3e50;
}

/* Filter container */
.filter-container {
  text-align: center;
  background: rgb(216, 216, 252);
  color: #2c3e50;
  width: 20%;
  border-radius: 10px;
  block-size: 25em;
  /* display: inline-block; */
  /* float: right; */
}

/* keywords rank container */
.keywords-rank-container {
  text-align: center;
  background: rgb(216, 216, 252);
  /* color: black; */
  color: #2c3e50;
  width: 20%;
  border-radius: 10px;
  block-size: 25em;
  /* display: inline-block; */
  float: right;
}

/* realtime container */
.real-time-container {
  text-align: center;
  background:  rgb(216, 216, 252);
  color: #2c3e50;
  width: 20%;
  border-radius: 10px;
  block-size: 25em;
  /* display: inline-block;
  float: left; */
}
</style>
