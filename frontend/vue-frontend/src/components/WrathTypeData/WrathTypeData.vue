<template>
    <div class="wrath-types">
        <h2>Wrath Distribution</h2>

        <button @click="update(wrathdata)"> Wrath Data</button>
        <button @click="update(aurinData)"> {{ aurinType }}</button>
         <!-- :on="generateBarChart" -->
        <!-- <svg ref="barChart" class="bar-chart">
        </svg> -->

        <!-- <img src="./wrath_bar.jpg" alt="wrath bar chart" class="barchart"> -->
        <div id="my_dataviz" style="width:500px;height:300px;"></div>

    </div>
    
</template>


<script>
var echarts = require("echarts");

// set the dimensions and margins of the graph



// A function that create / update the plot for a given variable:

export default {
    name: 'wrathtypedata',
    props: {
        wrathdata: Array,
        aurinData: Array,
        aurinType: String
    },
    methods:{
        init() {
            echarts.init(document.getElementById("my_dataviz")).setOption(this.option);
        },
        update(data){
            console.log('update-echart-data')
            console.log(data)
            this.option.xAxis.data=[]
            this.option.series[0].data=[]
            data.forEach(element => {
                this.option.xAxis.data.push(element.key)
                this.option.series[0].data.push(element.value)
            });
            this.$nextTick(()=>{
                this.init()
            })
        }
    },
    data() {
        return {
            option : {
                xAxis: {
                    type: 'category',
                    data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat',]
                },
                yAxis: {
                    type: 'value'
                },
                series: [{
                    data: [120, 200, 150, 80, 70, 110],
                    type: 'bar'
                }]
            }
        }
    },
    mounted: function(){
         // Initialize the plot with the first dataset
        // this.generateBarChart()
        // this.update(wrathdata)
        this.init()
    }
}
</script>


<style scoped>
.wrath-types {
    border: 1px solid black;
    text-align: center;
    background:  white;
    color: #2c3e50;
    width: 53%;
    border-radius: 10px;
    block-size: 22em;
    padding-top: 0.1px;
    margin-top: 10px;
    float: left;
    /* display:inline;   */
    margin-left: 1%;
    height: 500px;
    margin-right: 1px;
    /* margin-right: 24%; */

}
</style>
