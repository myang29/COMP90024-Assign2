<template>
  <div id="app">
    <Header/>

    <!-- Filter data -->
    <FilterData/>

    <!-- Keywords rank -->
    <KeywordsRank/>

    <!-- Wrath Type -->
    <WrathTypeData/>

    <!-- Real-time wrath data -->
    <RealtimeData/>

     <!-- Centre MAP -->
    <Map/>
    <GenerateMap/>
    
  
  </div>
</template>

<script>
import Map from './components/Map/Map.vue';
import FilterData from './components/FilterData/FilterData.vue';
import RealtimeData from './components/RealtimeData/RealtimeData.vue';
import WrathTypeData from './components/WrathTypeData/WrathTypeData.vue';
import KeywordsRank from './components/KeywordsRank/KeywordsRank.vue';
import Header from './components/Header.vue';
import GenerateMap from './components/Map/GenerateMap.vue';
export default {
  name: 'app',
  // combine all components 
  components: {
    GenerateMap,
    Map,
    FilterData,
    RealtimeData,
    WrathTypeData,
    KeywordsRank,
    Header
  },
  data: {
    return: {
      showBoarder: true,
      // mapDim: 
      //   {'mapWidth': 960, 'mapHeight': 1160}
      // ,
      // [960, 1160],
      // mapWidth: 960,
      // mapHeight: 1160,
    }
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
  background: rgb(243, 241, 241);

  /* content: "";
  display:block;
  clear: both; */
}
.app {
  background-color: rgb(248, 240, 240);
}

.h1, subhead {
    position: relative;
    z-index: 3;
}

/* apply to all unordered lists */
ul {
    /* remove bullet point */
    list-style-type: none;
    margin: 0;
    padding: 0;
}

/* wrath type container */
/* .wrath-types {
  text-align: center; */
  /* #00C2FF */
  /* background: white;
  color: #2c3e50;
  width: 20%;
  border-radius: 10px;
  block-size: 24.6em; */
  /* display: inline-block; */
  /* float: right;

} */

/* Map container */
/* .central-map-container {
  margin-right:-2%;
  text-align: center;
  width: 65%;
  border-radius: 10px;
  block-size: 20em;
  float: right;
  color: #2c3e50;
} */

/* Filter container */
/* .filter-container {
  text-align: center;
  background: rgb(216, 216, 252);
  color: #2c3e50;
  width: 100%;
  height: 20%;
  border-radius: 10px;
  block-size: 20em;
  padding-top: 0.1px;
  /* display: inline-block; */
  /* float: right; */
/* }  */

/* keywords rank container */
/* .keywords-rank-container {
  text-align: center;
  background: white; */
  /* color: black; */
  /* color: #2c3e50;
  width: 20%;
  border-radius: 10px;
  block-size: 25em; */
  /* display: inline-block; */
  /* float: right;
} */

/* realtime container */
/* .real-time-container {
  text-align: center;
  background:  white;
  color: #2c3e50;
  width: 20%;
  border-radius: 10px;
  block-size: 25em;
  padding-top: 0.1px;
  margin-top: 10px; */
  /* display: inline-block;
  float: left; */
/* } */
</style>
