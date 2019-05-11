<template>
    <div>
        <h2>Filter data</h2>
            <!-- drop down data type selections -->

            <!-- <form action="" class="dropdown-box"> -->
            <select class="dropdown-selection" name="Data_Types">
                <option v-for="data_type in data_types" :key=data_type.id>{{ data_type.text }}</option>
            </select>
            <!-- </form> -->

            <!-- date picker to select a range of year -->
            <date-picker class="date_range" v-model="date_range" lang="en" range type="year" format="YYYY" width="160" confirm></date-picker>
            <!-- [ "2012-04-30T14:00:00.000Z", "2019-04-30T14:00:00.000Z" ] -->

            <!-- Button to enable data to show on the map -->
            <a href="#" class="display-btn">Display</a>
    </div>
    
</template>


<script>
// for date selection
import DatePicker from 'vue2-datepicker'

export default {
    name: 'filterdata',
    components: {
        DatePicker
    },
    // props: {
    //     class: "filter-container"
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
            date_range: ""
        }
    }
}
</script>


<style scoped>

.display-btn {
    background: rgb(1, 1, 8);
    width: calc(100% - 6em);
    display: block;
    color: white;
    border-radius: 20px;
    padding: 0.5em;
    text-decoration: none;
    font-size: 1em;
    margin: 40% 4em 0;
    position: relative;
    z-index: 4;
}

.dropdown-selection {
    width: 160px;
    font-size: 16px;
    text-align: center;
    margin-top: 25%;
    margin-left: 10px;
}

.date_range {
    margin-top: 10%;
    margin-left: 10px;
}

/* .dropdown-box { */

/* } */

</style>
