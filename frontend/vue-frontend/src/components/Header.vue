
<template>
    <div class="header-container">
        <header>
            <!-- h1 class="text-info"-->
            <h1>Wrath Analysis over Australia</h1>
            <h4 class="col-12">Team 45</h4>
            <nav>
            <!-- unordered list for listing nav -->
            <!-- <ul class="nav" id="nav"> -->
                <!--# in a link means no location -->
                <!-- <li> <a href="#">Real-Time Data</a> </li>
                <li> <a href="#">Past Data</a> </li>
                <li> <a href="#">Overall</a> </li> -->
            <!-- </ul> -->
            </nav>
      </header>
    </div>
    
    
</template>


<script>
export default {
    name: 'header'
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

.header-container {
    width: 98%;
    text-align: center;
    border: 1px solid black;
    margin-bottom: 0px;
    margin-left: 1%;
    padding-bottom: 0px;
    background-color: white;
    height: 100px;
    
}
.header a {
    /* color: #fff; */
    /* padding-right: 5px; */
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
