<template>
    <div class="real-time-container">
        <h2>Real-time Wrath Data</h2>
        <img src="./wrath_bar.jpg" alt="wrath bar chart" class="barchart">
    </div>
    
</template>


<script>
export default {
    name: 'realtimedata',
}
</script>


<style scoped>

.real-time-container {
    border: 1px solid black;
    text-align: center;
    background:  white;
    color: #2c3e50;
    width: 53%;
    border-radius: 10px;
    block-size: 22em;
    padding-top: 0.1px;
    margin-top: 10px;
    margin-left: 0.75%;
    /* display: inline-block;*/
    float: left;
    height: 500px;
    /* display: inline;   */
}

.barchart {
    margin-left: 0;
    margin-right: 0;
    margin-top: 20px;
}
</style>
