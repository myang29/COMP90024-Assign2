
<template>
    <div class="header-container" :style="backgroundDiv">
        <header>
            <h1>Wrath Analysis over Australia</h1>
            <nav>
       
            </nav>
        </header>
    </div>
    
    
</template>


<script>
export default {
    name: 'header',
    data() {
      return{
        backgroundDiv: {backgroundImage:'url(' + require('./Anger.jpeg') + ')',
        backgroundRepeat:'no-repeat',
        backgroundSize:'100% 100%'
    }
      }
    }
}
</script>


<style scoped>
.header {
    /* background: #333; */
    /* color: #fff; */
    text-align: center;
    padding: 10px;
    margin-bottom: 0;
    /* border: 5px black; */

}
h1{
  padding-top: 215px;
  padding-left: 15%;
  padding-right: 60%;
  color: black;
  font-weight: 1000;
  font-family: 'Montserrat', sans-serif;
}

.header-container {
    width: 100%;
    text-align: center;
    /* border: 1px solid black; */
    margin-bottom: 0px;
    margin-left: 1%;
    padding-bottom: 0px;
    background-color: white;
    height: 500px;
    
}
.header a {
    color: #fff;
    padding-right: 5px;
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
</style>
