<template>
    <div class="map-container">

        <!-- <img src="./victoria_map.png" alt="victoria map" class="map"> -->

        <!-- checkbox to select the displayed data format -->
        <div class="radio-btn">
            <label><input type="radio" name="data-display-format" value="" >Rate</label>
            <label><input type="radio" name="data-display-format" value="" >Counts</label>
        </div>
        <!-- <svg>
            <path>
                {{ generatemap() }}
            </path>

        </svg> -->
        <div :v-bind="generatemap()" class="map"></div>
        <!-- <p>{{cities}}</p> -->
        <!-- <svg id ="generateMap">
            {{ generatemap() }}
        </svg> -->
        <!-- <div>
            <svg v-on="generatemap()">
            </svg>
        </div> -->
        

        <!-- <ul class="data-info">
            <li>Total number of posts: XXX</li>
            <li>Total number of displayed posts: XXX</li>
        </ul> -->
    </div>
    
</template>


<script>
// import citytopo from './victopo.json';
export default {
    name: 'map',
    data: {
        return() {
            cities: [
                {name: "Ballarat", location: {latitute: -37.56622, longitude: 143.84957}},
                {name: "Bendigo", location: {latitute: -36.75818, longitude: 144.28024}},
                {name: "Berwick", location: {latitute: -38.03333, longitude: 145.35}},
                {name: "Cranbourne", location: {latitute: -38.1, longitude: 145.28333}},
                {name: "Frankston", location: {latitute: -38.14458, longitude: 145.12291}},
                {name: "Frankston East", location: {latitute: -38.13333, longitude: 145.13333}},
                {name: "Geelong", location: {latitute: -38.14711, longitude: 144.36069}},
                {name: "Hoppers Crossing", location: {latitute: -37.88264, longitude: 144.7003}},
                {name: "Melbourne", location: {latitute: -37.814, longitude: 144.96332}},
                {name: "Melton", location: {latitute: -37.68339, longitude: 144.58543}},
                {name: "Reservoir", location: {latitute: -37.71667, longitude: 145}},
                {name: "Saint Albans", location: {latitute: -37.73333, longitude: 144.8}},
                {name: "Shepparton", location: {latitute: -36.38047, longitude: 145.39867}},
                {name: "Werribee", location: {latitute: -37.9, longitude: 144.66667}}
            ];

        }
    },
    
    methods: {

        generatemap() {
            var width = 1300,
            height = 1200;

            // create svg for displaying map
            var svg = d3.select("body").append("svg")
                .attr("width", width)
                .attr("height", height);

                
            var projection = d3.geo.mercator()
                .center([143.27214643,-38.62315014])
                .scale(5000)
                .translate([width/4.5,height/2.4]);
                // .scale(550)
                // .translate([-900,0]);
            

            var path = d3.geo.path()
                .projection(projection);
            
            // convert to topojson for visualization
            d3.json("http://localhost:8080/sa2topo.json", function(error, topology) {
                if (error) throw error;
                var color = d3.scale.category20c();  
                svg.selectAll("path")
                    .data(topojson.feature(topology, topology.objects.sa2geo).features)
                    .enter().append("path")
                    .attr("d", path)
                    .style("stroke", "black")
                    // .style("fill",function(d,i)  
                    //             {  
                    //                 return color(i);  
                    //             }) 
                    // .attr("fill", black)
                    .attr("fill", "rgb(255,250,250)");
            });

            // var color=d3.hsl(60, 1.0, 0.5);
            // var computeColor=d3.interpolate(color)
            // var city = this.cities;
            // var paleblue = d3.rgb(12,36,85);
            // var darkblue = d3.rgb(2,100,7);
            // svg.selectAll(".place-label")
            //     .data(city)
            //     .attr("class","place-label")
            //     .enter().append("text")
            //     .attr('width', 20)
            //     .attr('height', 20)
            //     // .attr("xlink:href",'https://cdn3.iconfinder.com/data/icons/softwaredemo/PNG/24x24/DrawingPin1_Blue.png')
            //     .attr("dy", ".35em")
            //     .attr("transform", function(d) {
            //         return "translate(" + projection([
            //             d.location.latitute,
            //             d.location.longitude
            //         ])+ ")";
            //     })
            //     .text(function(d) {return d.name});

                // .text(function(d) {return d.name});
        
        }
    },
}
</script>


<style scoped>
/* 
.map-container { 
    border: 1px solid gray;
    margin: auto; 
    margin-left: -10px;
    padding-left: -40px;
    width: 60%;
    height: 50%;
    margin-top: 18px;
    margin-right: 3px;
    display: block; 
} */

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
    margin-left: 10%;
    border: 5px solid pink;
    display: block;
    /* width: 65%; */
    /* margin-top: 40px; */
    /* margin-left: 45px; */
    /* margin-right: 60%; */
    /* margin-bottom: 10px; */
    z-index:999;
    position: relative;
}


.radio-btn {
    margin-top: 0;
    font-size: 20px;
}

</style>
