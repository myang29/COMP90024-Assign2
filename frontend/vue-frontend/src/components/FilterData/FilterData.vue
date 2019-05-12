<template>
    <div class="filter-container">
        <h3>Filter data</h3>
            
             <!-- Button to enable data to show on the map -->
            <!-- <a href="#" class="display-btn">Display</a> -->

            <button style="display-btn" v-on:click="getData">Display</button>

            <!-- drop down data type selections -->
            <!-- date picker to select a range of year -->
            <!-- <date-picker class="date_range" v-model="date_range" lang="en" range type="year" format="YYYY" width="160" confirm></date-picker> -->
           
           
            <!-- <form action="" class="dropdown-box"> -->
            <select class="dropdown-selection" name="Data_Types">
                <option v-for="data_type in data_types" :key=data_type.id>{{ data_type.text }}</option>
            </select>
            <p>{{ dbData.total_rows }}</p>
            <!-- </form> -->

    </div>
    
</template>


<script>
// for date selection
// import DatePicker from 'vue2-datepicker'

export default {
    name: 'filterdata',
    // components: {
    //     DatePicker
    // },

    data() {
        return {
            // TODO: decide what data will be used for comparison
            data_types: [
                {text: "Data Types", id: 1},
                {text: 'Illness', id: 2},
                {text: 'Crime', id: 3},
                {text: 'Religon', id: 4},
                {text: 'Unemployment', id: 5}
            ],
            // fromdate: '',
            // todate: '',
            // date_range: "",
            dbData: []
        }
    },
    methods:{
        getData: function(){
            this.$axios.get('http://172.26.38.75:9024/aurin_disease/_design/testview/_view/testview')
            .then( (response) => {
                this.dbData = response.data;
                console.log(response);
            })
        }
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
/* 
.date_range {
    margin-top:0;
    margin-left: 0px;
    margin-right: 22%;
    float: right;
    width: 10%;
} */

</style>
