


<template>
    <div>
        <header>
                <h1>Team Name</h1>
                    <!-- img src="images/..svg" alt"logo/imgname" class= "logo"-->
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
.nav {
    text-align: center;
    text-align: center;
    /* padding: 0.8em 1.2em 2em 40; */
    padding: 0.8em 1.2em;
}
</style>
