<template>
  <div class="keywords-rank-container">
    <h2>Keywords Rank</h2>
    <div id="keywords"></div>
  </div>
</template>


<script>

import MsgBus from '../msgBus.js';
var echarts = require("echarts");
require("echarts-wordcloud");


export default {
  name: "keywordsrank",
  components: {
    MsgBus
  },
  mounted() {

    //receive city name


    this.extractFreq();
  },
  data(){
    return {
      cityName: "",
      wordFreq: [],
      option: {
        title: {
          // link: "https://github.com/ecomfe/echarts-wordcloud",
          // subtext: "data-visual.cn",
          // sublink: "http://data-visual.cn"
        },
        tooltip: {},
        series: [
          {
            type: "wordCloud",
            gridSize: 20,
            sizeRange: [12, 50],
            rotationRange: [0, 0],
            shape: "circle",
            textStyle: {
              normal: {
                color: function() {
                  return (
                    "rgb(" +
                    [
                      Math.round(Math.random() * 160),
                      Math.round(Math.random() * 160),
                      Math.round(Math.random() * 160)
                    ].join(",") +
                    ")"
                  );
                }
              },
              emphasis: {
                shadowBlur: 10,
                shadowColor: "#333"
              }
            
            },
            data: []
          }
          ]
        }
    }
  },
  methods: {
    init() {
      // console.log("!!!! option data at last = "+ this.option.series[0].data)
      echarts.init(document.getElementById("keywords")).setOption(this.option);
    },
    compare(attr) {
      return function(a, b) {
        var value1 = a[attr];
        var value2 = b[attr];
        return value2 - value1;
      }
    },
    extractFreq() {
      MsgBus.$on('cityName', (e) => {
        this.cityName = e;
        // console.log("city name from map is: -> "+this.cityName)
      })
      // console.log("city name from map is: -> "+this.cityName)
      let tmp=[]
      // if (this.cityName == "Melbourne"){
        console.log("city name from map is: -> "+this.cityName)
        //"http://172.26.38.75:9024/processed_twit/_design/word/_view/total?group=true"
        // http://172.26.38.75:9024/processed_twit/_design/word/_view/adelaide?group=true
        // http://172.26.38.75:9024/processed_twit/_design/word/_view/brisbane?group=true
        // http://172.26.38.75:9024/processed_twit/_design/word/_view/canberra?group=true
        // http://172.26.38.75:9024/processed_twit/_design/word/_view/darwin?group=true
        // http://172.26.38.75:9024/processed_twit/_design/word/_view/hobart?group=true
        // http://172.26.38.75:9024/processed_twit/_design/word/_view/melbourne?group=true
        // http://172.26.38.75:9024/processed_twit/_design/word/_view/perth?group=true
        // http://172.26.38.75:9024/processed_twit/_design/word/_view/sydney?group=true
      this.$axios.get("http://172.26.38.75:9024/processed_twit/_design/word/_view/melbourne?group=true")
        .then( (response) => {
        tmp = response.data.rows;
        console.log('tmp')
        console.log(tmp)
        for (var i=0; i < tmp.length; i++){
          if(tmp[i].key&&tmp[i].value){
            let obj = {};
            obj.name = tmp[i].key
            obj.value = tmp[i].value
            this.wordFreq.push(obj)
          }
          console.log("temp 1st key = "+this.wordFreq[i].name + this.wordFreq[i].value);
        }

        var sorted = this.wordFreq.sort(this.compare("value")).slice(20,100);
        // console.log("wordFreq + "+this.wordFreq.length);
        // console.log("test element    -> 4" + this.option.series[0].data[0].name);
        this.option.series[0].data = sorted;
        console.log("sorted data = "+ sorted)
        this.$nextTick(()=>{
          this.init();
        })
      })
      // }
      
     
    }
    
  }
};
</script>


<style scoped>
.keywords-rank-container {
  border: 5px solid black;
  text-align: center;
  background: white;
  color: #2c3e50;
  /* width: 44%; */
  /* border-radius: 10px; */
  block-size: 22em;
  padding-top: 0.1px;
  /* margin-top: 1px; */
  margin-right: 1%;
  margin-bottom: 2px;
  /* float: right; */
  height: 500px;

}
#keywords {
  width: 650px;
  height: 450px;
  /* border:1px solid red; */
}
h2{
  margin-top: 1px;
}
</style>
