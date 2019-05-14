<template>
    <div class="real-time-container">
        <h2>Relation line Chart</h2>
        <img src="img_src" alt="Please first select a comparing data type" class="barchart" :change="loadImg">
    </div>
    
</template>


<script>
export default {
    name: 'RealtimeData',
    props: {
        typeName: String
    }, 
    data() {
        return{
            img_src: ""
        }
    },
    methods: {
        loadImg(){
            if (this.typeName === "Religion"){
                this.img_src = "./religion.jpeg"
            }else {
                this.img_src = "./voluntary.jpeg"
            }
        }
    }
}
</script>


<style scoped>

.real-time-container {
    border: 1px solid black;
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

    margin-top: 4px;
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
