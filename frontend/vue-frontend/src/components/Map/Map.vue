<template>
    <div class="map-container">
        <ul class="date">
            <li>
                <h3>Victoria</h3>
            </li>
            <li>
                <h3>Date..</h3>
            </li>
        </ul>
       
        <div class="map" id="mapHolder">
            {{ generatemap() }}
        </div>

        <!-- <img src="./victoria_map.png" alt="victoria map" class="map"> -->

        <!-- checkbox to select the displayed data format-->
        <form>
            <label><input type="radio" name="data-display-format" value="" id="rate_format">Rate</label>
            <label><input type="radio" name="data-display-format" value="" id="counts_format">Counts</label>
        </form>

        <ul class="data-info">
            <li>Total number of posts: XXX</li>
            <li>Total number of displayed posts: XXX</li>
        </ul>
    </div>
    
</template>


<script>
// import citytopo from './victopo.json';
export default {
    name: 'map',
    
    // props: "mapDim",
    methods: {

        generatemap: function() {
            var width = 1000,
            height = 800;

            // create svg for displaying map
            var svg = d3.select("body").append("svg")
                .attr("width", width)
                .attr("height", height);

                
            var projection = d3.geo.mercator()
                .center([147.241724,-36.867031])
                .scale(3500)
                .translate([width/1.4,height/40]);
                // .scale(550)
                // .translate([-900,0]);
            

            var path = d3.geo.path()
                .projection(projection);
            
            // convert to topojson for visualization
            d3.json("http://localhost:8080/victopo.json", function(error, topology) {
                if (error) throw error;

                svg.selectAll("path")
                    .data(topojson.feature(topology, topology.objects.viccity_geo).features)
                    .enter().append("path")
                    .attr("d", path);
            })
        }
    },
}
</script>


<style scoped>

.map-container {
    border: 1px solid gray;
    margin: auto;
    /* margin-left: -10px; */
    /* padding-left: -40px; */
    width: 60%;
    /* height: 50%; */
    margin-top: 18px;
    margin-right: 3px;
    display: block;
}

#mapHolder {
    width: 50vw;
    height: 50vh;
    /* border: 1px solid gray; */
    display: block;
}
.map {
    /* width: 80%;
    margin: 2em, auto, 10em, 25%; */
    display: block;
    margin-left: 30%;
    border: 1px solid gray;
    display: block;
    /* width: 65%; */
    margin-top: 40px;
    margin-left: 45px;
    /* margin-right: 60%; */
    margin-bottom: 10px;
    z-index:999;
    position: relative;
}

path {
    /* fill: rgb(219, 217, 223); */
    fill: black;
}

</style>
