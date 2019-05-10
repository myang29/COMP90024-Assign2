<template>
    <div>
        <ul class="date">
            <li>
                <h3>Victoria</h3>
            </li>
            <li>
                <h3>Date..</h3>
            </li>
        </ul>

        <img src="./victoria_map.png" alt="victoria map" class="map">

        <!-- checkbox to select the displayed data format-->
        <form>
            <label><input type="radio" name="data-display-format" value="" id="rate_format">Rate</label>
            <label><input type="radio" name="data-display-format" value="" id="counts_format">Counts</label>
        </form>

        <ul class="data-info">
            <li>Total number of posts: XXX</li>
            <li>Total number of displayed posts: XXX</li>
        </ul>
    </div>
    
</template>


<script>
export default {
    name: 'map',
}
</script>


<style scoped>

.map {
    width: 80%;
    margin: 2em, auto, 10em, 25%;
}

</style>
