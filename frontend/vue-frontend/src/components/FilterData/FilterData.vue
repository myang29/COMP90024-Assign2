<template>
    <div>
        <div class="filter-container">
            <h3>Filter data</h3>
            
            <button class="display-btn" v-on:click="getData(aurin_url)">Display</button>

           
            <!-- <form action="" class="dropdown-box"> -->
            <select v-on:change="indexSelected" v-model="id" class="dropdown-selection" name="Data_Types">
                <option v-for="data_type in data_types" :key=data_type.id>{{ data_type.text }}</option>
                <h3>selected.text</h3>
            </select>
        </div>

        <Map/>

        <!-- Keywords rank -->
        <!-- <KeywordsRank /> -->

        <!-- Wrath Type -->
        <!-- <WrathTypeData :wrathdata="wrathdata" :aurinData="aurinData" :aurinType="aurinType"/> -->
        <div class="row">
            <div class="col-6">
                <WrathTypeData :wrathdata="wrathdata" :aurinData="aurinData" :aurinType="aurinType"/>
            </div>
            <div class="col-6">
            <!-- <h2>hahaha</h2> -->
            <!-- Keywords rank -->
                <RealtimeData />
            </div>

        </div>

    </div>
    
</template>


<script>
// for date selection
// import DatePicker from 'vue2-datepicker'
import KeywordsRank from '../KeywordsRank/KeywordsRank.vue'
import WrathTypeData from '../WrathTypeData/WrathTypeData.vue'
import RealtimeData from '../RealtimeData/RealtimeData.vue'
import GenerateMap from '../Map/GenerateMap.vue'
import Map from '../Map/Map.vue';
// import wordcloud from 'vue-wordcloud'
export default {
    name: 'filterdata',
    components: {
        Map,
        KeywordsRank,
        WrathTypeData,
        RealtimeData,
        GenerateMap,

    },

    data() {
        return {
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
    width: 98%;
    /* height: 50%; */
    /* border-radius: 10px; */
    block-size: 7em;
    padding: 0.1px;
    display: block;
    margin-left: 1%;
    margin-top: 0.5%;
    border: 1px solid black;
    margin-bottom: 0px;
  /* float: right; */
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
    font-size: 16px;
    text-align: center;
    margin-top: 0%;
    margin-left: 140px;
    /* padding-top: 0; */
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

</style>
