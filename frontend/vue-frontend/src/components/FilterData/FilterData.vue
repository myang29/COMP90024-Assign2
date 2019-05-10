<template>
    <div>
        <h2>Filter data</h2>
            <!-- drop down data type selections -->

            <!-- <form action="" class="dropdown-box"> -->
            <select name="Data_Types">
                <option v-for="data_type in data_types" :key=data_type>{{ data_type.text }}</option>
            </select>
            <!-- </form> -->

            <ul class="search-dropdown-time">
                <li>From</li>
                <li>To</li>

            </ul>
        
            <!-- Button to enable data to show on the map -->
            <a href="#" class="display-btn">Display</a>
    </div>
    
</template>


<script>
export default {
    name: 'filterdata',
    data() {
        return {
            // TODO: decide what data will be used for comparison
            data_types: [
                {text: "Data Types", id: 1},
                {text: 'Illness', id: 2},
                {text: 'Crime', id: 3},
                {text: 'Religon', id: 4},
                {text: 'Unemployment', id: 5}
            ]
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
    margin: 100% 4em 0;
    position: relative;
    z-index: 4;
}

/* .dropdown-box { */

/* } */

</style>
