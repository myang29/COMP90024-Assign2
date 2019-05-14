<template>
  <div id="app">
    <Header/>
     <p>Never go to bed mad. Stay up and fight.          - Phyllis Diller</p>

      <p>Speak when you are angry and you will 
        make the best speech you will ever regret.          - Ambrose Bierce</p>
    <!-- Filter data -->
    <FilterData/>

  
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
    // RealtimeData,
    // WrathTypeData,
    KeywordsRank,
    Header
  },
  data: {
    return: {
      showBoarder: true,
      
    },

  }
}
</script>

<style>
@import url('http://fonts.googleapis.com/css?family=Montserrat:400,600');
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  /* color: #2c3e50; */
  /* margin-top: 60px; */

  /* space from most left */
  margin: 0;
  /* font-family: 'Montserrat', sans-serif; */
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
p{
  font-size: 28px;
  margin-top: 10px;
  padding-top: 40px;
  padding-bottom: 20px;
  
}


</style>
