
<template>

    <!-- <div :v-bind="generatemap()" class="map"></div> -->

    <div>
        <!-- :v-bind="generatemap()"-->
        <svg class="map" width="480" height="600"> {{ q }}</svg>
    </div>
</template>


<script>
export default {
    name: 'generatemap',
    data: {
        return(){
            wrathData: d3.map();
            q: d3.queue()
                .defer(d3.json, "http://localhost:8080/sa2topo.json")
                // .defer(d3.json, "")
                .await(this.$options.methods.ready());
        }
    },
    methods: {
        generatemap: function() {
            // in dic format {id: value}
            var wrathData = d3.map();

            // asynchronous tasks, load topojson and wrath data
            d3.queue()
                .defer(d3.json, "http://localhost:8080/sa2topo.json")
                // .defer(d3.json, "")
                .await(this.$options.methods.ready());
        },
        // callback function
        ready: function(error, data){
            if(error) throw error;

            var vic = topojson.feature(data, data.objects.sa2geo);

            // projection and path
            var projection = d3.geoMercator()
                .center([143.27214643,-38.62315014])
                .scale(5000)
                .translate([width/4.5,height/2.4]);
                // .scale(550)
                // .translate([-900,0]);
            

            var path = d3.geoPath()
                .projection(projection);

            d3.select("svg.map").selectAll("path")
                .data(vic.features)
                .enter("path")
                .attr("d", path)
                .attr("fill", "green");
        }

    }
}

</script>


<style scoped>

</style>
