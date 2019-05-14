<template>
    <div class="wrath-types">
        <h2>Wrath Distribution</h2>

 

        <img src="./wrath_bar.jpeg" alt="wrath bar chart" class="barchart">

    </div>
    
</template>


<script>


export default {
    name: 'wrathtypedata',
}
</script>


<style scoped>
.wrath-types {
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
    margin-right: 5%;
    /* margin-right: 24%; */
    margin-bottom: 3%;
    padding-bottom: 3%;

}
.barchart {
    margin-top: 5px;
    margin-left: 3px;
    margin-right: 3px;
    width: 90%;
    height: 90%;
}
</style>
