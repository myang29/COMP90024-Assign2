<template>
  <div class="map-container">
    <!-- <img src="./victoria_map.png" alt="victoria map" class="map"> -->

    <!-- checkbox to select the displayed data format -->
    <!-- <div class="radio-btn">
      <label>
        <input type="radio" name="data-display-format" value>Rate
      </label>
      <label>
        <input type="radio" name="data-display-format" value>Counts
      </label>
    </div> -->
    
    <div id="map"></div>
    <!-- <svg>
            <path>
                {{ generatemap() }}
            </path>

    </svg>-->
    <!-- <div :v-bind="generatemap()" class="map"></div>
    <div>
      <svg v-bind="loadData()"></svg>
    </div> -->
    <!-- <p>{{ dbData.total_rows}}</p> -->
    <!-- <p>{{cities}}</p> -->
    <!-- <svg id ="generateMap">
            {{ generatemap() }}
    </svg>-->
  </div>
</template>


<script>
import statesData from "./data2";
import { Promise } from "q";
// import citytopo from './victopo.json';
export default {
  name: "map",
  data() {
    return {
      cities: [
        {
          name: "Ballarat",
          location: { latitute: -37.56622, longitude: 143.84957 }
        },
        {
          name: "Bendigo",
          location: { latitute: -36.75818, longitude: 144.28024 }
        },
        {
          name: "Berwick",
          location: { latitute: -38.03333, longitude: 145.35 }
        },
        {
          name: "Cranbourne",
          location: { latitute: -38.1, longitude: 145.28333 }
        },
        {
          name: "Frankston",
          location: { latitute: -38.14458, longitude: 145.12291 }
        },
        {
          name: "Frankston East",
          location: { latitute: -38.13333, longitude: 145.13333 }
        },
        {
          name: "Geelong",
          location: { latitute: -38.14711, longitude: 144.36069 }
        },
        {
          name: "Hoppers Crossing",
          location: { latitute: -37.88264, longitude: 144.7003 }
        },
        {
          name: "Melbourne",
          location: { latitute: -37.814, longitude: 144.96332 }
        },
        {
          name: "Melton",
          location: { latitute: -37.68339, longitude: 144.58543 }
        },
        {
          name: "Reservoir",
          location: { latitute: -37.71667, longitude: 145 }
        },
        {
          name: "Saint Albans",
          location: { latitute: -37.73333, longitude: 144.8 }
        },
        {
          name: "Shepparton",
          location: { latitute: -36.38047, longitude: 145.39867 }
        },
        {
          name: "Werribee",
          location: { latitute: -37.9, longitude: 144.66667 }
        }
      ],
      dbData: [],
      errormsg: "",
      loading: ""
    };
  },

  methods: {
    async loadData() {
      this.loading = true;
      try {
        await Promise.all([this.generatemap()]);
      } catch (error) {
        this.errormsg = error.message;
      } finally {
        this.loading = false;
      }
    },

    getData: function() {
      return this.$axios
        .get(
          "http://172.26.38.75:9024/processed_twit/_design/wrath/_view/rate?group=true"
        )
        .then(response => {
          this.dbData = response.data;
          console.log(this.dbData.total_rows);
        });
    },

    generatemap() {
      var width = 1300,
        height = 1200;

      // create svg for displaying map
      var svg = d3
        .select("body")
        .append("svg")
        .attr("width", width)
        .attr("height", height);

      var projection = d3
        .geoMercator()
        .center([133.8807, 23.698])
        .scale(1000)
        .translate([width / 2, height / 100]);
      // .scale(550)
      // .translate([-900,0]);

      var path = d3.geoPath().projection(projection);

      // convert to topojson for visualization
      return d3.json("http://localhost:8080/aus_topo.json", function(
        error,
        topology
      ) {
        if (error) throw error;
        // var color = d3.scale.category20c();
        svg
          .selectAll("path")
          .data(topojson.feature(topology, topology.objects.australia).features)
          .enter()
          .append("path")
          .attr("d", path)
          .style("stroke", "black")
          .attr("fill", "rgb(255,250,250)");
      });

      // Promise.all([
      //      d3.json("http://localhost:8080/sa2topo.json"),
      //      d3.json("http://localhost:8080/victopo.json")]).then(([victopo, wrath]) =>{
      //         svg.selectAll("path")
      //         .data(topojson.feature(victopo, victopo.objects.sa2geo).features)
      //         .enter().append("path")
      //         .attr("d", path)
      //         .style("stroke", "black")
      //         .attr("fill", "rgb(255,250,250)");

      //         console.log(wrath.objects.viccity_geo);
      //     })
    },
    initMap() {
      var map = L.map("map").setView([-27.4698, 138.6007], 4);

      L.tileLayer(
        "https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw",
        {
          maxZoom: 30,
          attribution:
            'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
            '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
            'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
          id: "mapbox.light"
        }
      ).addTo(map);

      // control that shows state info on hover
      var info = L.control();

      info.onAdd = function(map) {
        this._div = L.DomUtil.create("div", "info");
        this.update();
        return this._div;
      };

      info.update = function(props) {
        this._div.innerHTML =
          "<div style='border:1px solid red'>" +
          "<h4>Australia Wrath Data distribution </h4>" +
          (props
            ? "<b>" +
              props.name +
              "</b><br />" +
              props.density +
              " posts / mi<sup>2</sup>"
            : "Hover over a state");
        +"</div>";
      };

      info.addTo(map);

      // get color depending on population density value
      function getColor(d) {
        return d > 100
          ? "#800026"
          : d > 50
          ? "#BD0026"
          : d > 20
          ? "#E31A1C"
          : d > 10
          ? "#FC4E2A"
          : d > 5
          ? "#FD8D3C"
          : d > 2
          ? "#FEB24C"
          : d > 1
          ? "#FED976"
          : "#FFEDA0";
      }

      function style(feature) {
        return {
          weight: 2,
          opacity: 1,
          color: "white",
          dashArray: "3",
          fillOpacity: 0.7,
          fillColor: getColor(feature.properties.density)
        };
      }

      function highlightFeature(e) {
        var layer = e.target;

        layer.setStyle({
          weight: 5,
          color: "#666",
          dashArray: "",
          fillOpacity: 0.7
        });

        if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
          layer.bringToFront();
        }

        info.update(layer.feature.properties);
      }

      var geojson;

      function resetHighlight(e) {
        geojson.resetStyle(e.target);
        info.update();
      }

      function zoomToFeature(e) {
        map.fitBounds(e.target.getBounds());
      }

      function onEachFeature(feature, layer) {
        layer.on({
          mouseover: highlightFeature,
          mouseout: resetHighlight,
          click: zoomToFeature
        });
      }

      geojson = L.geoJson(statesData, {
        style: style,
        onEachFeature: onEachFeature
      }).addTo(map);

      // map.attributionControl.addAttribution(
      //   'Population data &copy; <a href="http://census.gov/">US Census Bureau</a>'
      // );

      var legend = L.control({ position: "bottomright"});

      legend.onAdd = function(map) {
        var div = L.DomUtil.create("div", "info legend"),
          grades = [0, 1, 2, 5, 10, 20, 50, 100],
          labels = [],
          from,
          to;

        for (var i = 0; i < grades.length; i++) {
          from = grades[i];
          to = grades[i + 1];

          labels.push(
            '<i style="background:' +
              getColor(from + 1) +
              '"></i> ' +
              from +
              (to ? "&ndash;" + to : "+")
          );
        }

        div.innerHTML = labels.join("<br>");
        return div;
      };

      legend.addTo(map);
    }
  },
  mounted() {
    // this.loadData();
    this.initMap();
  }
};
</script>


<style scoped>
.map-boarder {
  border: 5px solid black;
}
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
  /* border: 5px solid pink; */
  display: block;
  /* width: 65%; */
  /* margin-top: 40px; */
  /* margin-left: 45px; */
  /* margin-right: 60%; */
  /* margin-bottom: 10px; */
  z-index: 999;
  position: relative;
}
#map {
  width: 100%;
  height: 500px;
}

.radio-btn {
  margin-top: 0;
  font-size: 20px;
}
</style>
