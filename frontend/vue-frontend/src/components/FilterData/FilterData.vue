<template>
    <div>

        <h2>Wrath Data Analysis</h2>
        <Map class="text-center"/>
        <div class="row">
            <div class="col-6">
                <!-- <Map class="text-center"/> -->
                <KeywordsRank />
            </div>
            <div class="col-6">
                <WrathTypeData class="text-center"/>
            </div>
        </div>

        <h2>Wrath & Voluntary Work</h2>
        <div class="row">
            <div class="col-6">
                <div class="bar-container">
                    <img src="./voluntary_bar.jpeg" alt="wrath bar chart" class="barchart text-center">
                </div>
            </div>

            <div class="col-6">
                <div class="line-container">
                    <img src="./religion.jpeg" alt="wrath bar chart" class="linechart text-center">
                </div>
            </div>
        </div>

        <h2>Wrath & Religion</h2>
        <div class="row">
            <div class="col-6">
                <div class="bar-container">
                    <img src="./religion_bar.jpeg" alt="wrath bar chart" class="barchart text-center">
                </div>
            </div>
            <div class="col-6">
                <div class="line-container">
                    <img src="./voluntary.jpeg" alt="wrath bar chart" class="linechart text-center">
                </div>
            </div>
        </div>


    </div>
    
</template>


<script>
// for date selection
// import DatePicker from 'vue2-datepicker'
import KeywordsRank from '../KeywordsRank/KeywordsRank.vue'
import WrathTypeData from '../WrathTypeData/WrathTypeData.vue'
import GenerateMap from '../Map/GenerateMap.vue'
import Map from '../Map/Map.vue';
export default {
    name: 'filterdata',
    components: {
        Map,
        KeywordsRank,
        WrathTypeData,
        // RealtimeData,
        GenerateMap,

    },

    data() {
        return {
            type: "Data Types",
            myColors: ['#1f77b4', '#629fc9', '#94bedb', '#c9e0ef'],
            selected: "",
            // TODO: decide what data will be used for comparison
            data_types: [
                {text: "Data Types", id: 1},
                {text: 'Religon', id: 4},
                {text: 'Voluntary Work', id: 5}
            ],
            aurinData: [],
            wrathdata: [],
            wordsFreq: [],
            aurin_url: "",
            wrath_url: "http://172.26.38.75:9024/processed_twit/_design/wrath/_view/rate?group=true",
            freq_url: "http://172.26.38.75:9024/processed_twit/_design/word/_view/total?group=true",
            aurinType: ""


        }
    },
    methods:{
        // wordClickHandler(name, value, vm) {
        //     console.log('wordClickHandler', name, value, vm);
        // },
        getData: function(url){
            if (url != ""){
                this.$axios.get(url)
                    .then( (response) => {
                    this.aurinData = response.data.rows;
                    // console.log(response.data.rows[0]);
            })
            }
        },
        indexSelected: function() {
            console.log(this.id)
            // wrath: http://172.26.38.75:9024/processed_twit/_design/wrath/_view/rate?group=true
            // voluntary: http://172.26.38.75:9024/gccsa_voluntary/_design/view/_view/view
            if (this.id === "Religon"){
                this.url = "http://172.26.38.75:9024/gccsa_religion/_design/views/_view/main_religions";
                this.aurinType = "Religon"
            }
            if (this.id === "Voluntary Work"){
                this.url = "http://172.26.38.75:9024/gccsa_voluntary/_design/view/_view/view";
                this.aurinType = "Voluntary Work"
            }
        },

        parallelRequest() {
            this.$axios.all([
                this.wrath_request(), //or direct the axios request
                this.freq_request()
            ])
            .then(this.$axios.spread((wrath, freq) => {
                this.wrathdata = wrath.data.rows;
                this.wordsFreq = freq.data.rows;
                // console.log("Wrath data" + this.wrathdata)
                // console.log(" FILTER freq data" + this.wordsFreq[0].value)
            }))
        },

        wrath_request() {
            return this.$axios.get(this.wrath_url);
        },
        freq_request() {
            return this.$axios.get(this.freq_url);
        }
    },
    mounted: function(){
        // load wrath data on map and word cloud diagram
        // this.getData();
        this.parallelRequest();
    }
}
</script>


<style scoped>
.filter-container {
    text-align: left;
    /* background: rgb(216, 216, 252); */
    background-color: white;
    /* color: #2c3e50; */
    width: 48%;
    /* height: 50%; */
    /* border-radius: 10px; */
    block-size: 7em;
    padding: 0.1px;
    display: block;
    margin-left: 1%;
    margin-top: 4%;
    border: 0.5px solid black;
    margin-bottom: 5px;
  /* float: right; */
}
h3{
    padding-top: 8px;
    padding-left: 15px;
}

.display-btn {
    background: rgb(1, 1, 8);
    /* width: calc(100% - 6em); */
    display: block;
    color: white;
    border-radius: 20px;
    padding: 0.5em;
    text-decoration: none;
    font-size: 1em;
    margin: 0 4em 0;
    width: 8%;
    text-align: center;
    float: right;
}

.dropdown-selection {
    width: 20%;
    height: 30px;
    font-size: 17px;
    text-align: center;
    margin-top: 1%;
    margin-left: 300px;
    /* padding-top: 0; */
    padding-top: 3px;
    padding-left: 15px;
}

.map-container {
  margin-top: 2%;
}
/* 
.date_range {
    margin-top:0;
    margin-left: 0px;
    margin-right: 22%;
    float: right;
    width: 10%;
} */

h2 {
    padding-top: 80px;
    font-weight: 800;
    
    /* font-family: 'Montserrat', sans-serif; */
}

.barchart {
    margin-top: 30px;
    margin-left: 0;
    margin-right: 10px;
    width: 100%;
    height: 90%;
    padding-top: 10px;
    /* width: 650px;
    height: 450px; */
}
.bar-container{
    border: 1px solid black;
    text-align: center;
    background: white;
    color: #2c3e50;
    /* width: 20%; */
    /* border-radius: 10px; */
    block-size: 22em;
    padding-top: 0.1px;
    /* margin-top: 1px; */
    margin-left: 3%;
    margin-top: 2%;
    /* float: right; */
    height: 500px;
    /* width: 50%; */
    /* marginleft */
}

.line-container{
    border: 1px solid black;
    text-align: center;
    background:  white;
    color: #2c3e50;
    width: 98%;
    /* border-radius: 10px; */
    block-size: 22em;
    padding-top: 4px;
    margin-top: 13px;
    /* float: left; */
    /* display:inline;   */
    /* margin-left: 1%; */
    height: 500px;
    margin-right: 1px;
    /* margin-right: 24%; */
    margin-bottom: 3%;
    padding-bottom: 3%;
    
}

.linechart {
    margin-top: 5px;
    margin-left: 3px;
    margin-right: 3px;
    width: 90%;
    height: 90%;
}
</style>
