
<template>
    <div class="header-container">
        <header>
            <h1>Team 45 - Wrath</h1>
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
    /* border: 5px black; */

}

.header-container {
  text-align: center;
  border: 4px dotted black;
    
}
.header a {
    /* color: #fff; */
    /* padding-right: 5px; */
}
.nav {
    text-align: center;
    text-align: center;
    /* padding: 0.8em 1.2em 2em 40; */
    padding: 0.8em 1.2em;
}
</style>
