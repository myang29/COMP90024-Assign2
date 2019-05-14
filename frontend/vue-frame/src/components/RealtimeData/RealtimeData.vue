<template>
    <div class="real-time-container">
        <h2>Relation linear Chart</h2>
        <img src="./religion.jpeg" alt="wrath bar chart" class="barchart">
    </div>
    
</template>


<script>
export default {
    name: 'realtimedata',
}
</script>


<style scoped>

.real-time-container {
    /* border: 1px solid black; */
    text-align: center;
    background:  white;
    color: #2c3e50;
    width: 98%;
    /* border-radius: 10px; */
    block-size: 22em;
    padding-top: 0.1px;
    /* margin-top: 10px;
    margin-left: 0.75%;
    /* display: inline-block;*/
    /* float: left; */
    /* height: 500px;  */
    /* display: inline;   */

    margin-top: 10px;
    /* float: left; */
    /* display:inline;   */
    margin-left: 1%;
    height: 500px;
    margin-right: 1px;
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
