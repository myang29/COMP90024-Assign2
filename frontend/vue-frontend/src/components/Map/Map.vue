<template>
  <div class="map-container">

        <div id="map"></div>


  </div>
</template>


<script>
import statesData from "./data2";
import { Promise } from "q";
import { log } from 'util';
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
        return d >  0.055

          ? "#CA4D65"
          : d > 0.050
          ? "#F3311B"
          : d > 0.045
          ? "#F3581B"
          : d > 0.0435
          ? "#F38B2F"
          : d > 0.042
          ? "#F39D5A"
          : d > 0.038
          ? "#F3AD5A"
          : d > 0.035
          ? "#F6CE6C"
          : d > 0.025
          ? "#FED976"
          : "#FFEDA0";
      }
      // [0, 0.025, 0.035, 0.038, 0.042, 0.0435, 0.045,0.050, 0.055],
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
        // send city name to wordcloud
        // MsgBus.$emit('cityName', layer.feature.properties.name);
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
          grades = [0, 0.025, 0.035, 0.038, 0.042, 0.0435, 0.045,0.050, 0.055],
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



#map {
  /* width: 100%; */
  height: 500px;
  margin-top: 0;
  margin-left: 2%;
  margin-right: 1%;
  border: 1px solid black;
  width: 97%;
  
}

.radio-btn {
  margin-top: 0;
  font-size: 20px;
}
</style>
