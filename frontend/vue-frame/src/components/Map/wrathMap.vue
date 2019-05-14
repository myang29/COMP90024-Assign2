<template>
    <div class="row map">
        <l-map :class="map" :zoom="zoom" :center="center">
            {{url}}
            <l-tile-layer :url="url" :attribution="attribution"/>
            <l-marker :lat-lng="marker" />
            <l-geojson :geojson="geojson"/>
        </l-map>


    </div>
</template>

<script>
import {LMap, LTileLayer, LMarker, LGeoJson} from 'vue2-leaflet';
// import { METHODS } from 'http';
export default {
    name: "wrathmap",
    components: {
        LMap,
        LTileLayer,
        LMarker
    },
    data(){
        return {
            // mapBoxAccessToken: pk.eyJ1IjoiZ2lvdmFubmF0b25nIiwiYSI6ImNqdmxzZG0wOTB0aWc0NHBoM3g1NHlyMmsifQ.bncN21VdHnxA93KrFMVtpg,
            // zoom:200,
            // center: L.latLng(47.413220, -1.219482),
            // // url:'https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token='+mapBoxAccessToken,
            // url:'http://{s}.tile.osm.org/{z}/{x}/{y}.png',
            // attribution:'&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
            // // id: 'mapbox.light',
            // attribution: '...',
            // marker: L.latLng(47.413220, -1.219482),
            geojson: null,


            zoom:4,
            center: L.latLng(-37.8136,144.9631),
            url:'http://{s}.tile.osm.org/{z}/{x}/{y}.png',
            attribution:'&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
            marker: L.latLng(-33.88937890660816, 151.2409175169709),
        }
    },
    methods: {

    },
    created() {

        this.$axios.get(
            "http://localhost:8080/aus_geo.json"
        )
        .then(response => {
            this.geojson = response.data;
            console.log(response.data)
            this.loading = false;
        });
    }
}
</script>



<style scoped>
    .map {
        height: 60vh;
    }
</style>
