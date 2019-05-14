
<template>
    <div class="container">
        <div class="row">

            <div class="col-6">
                <wrathMap/>
            </div>
                
            <div class="col-6">
                <h2>right</h2>
            </div>
        </div>
    </div>

</template>


<script>

import wrathMap from './wrathMap';
export default {
    name: 'generatemap',
    components: {
        wrathMap
    },
    props: {

    }, 
    data: function() {
return {
        return(){
            []
        },
    };
},
    methods: {
    },
    // geneate map at the start
    mounted: function(){
        // map polygon topojson file link 'http://172.26.38.75:9024/aurin_disease/_design/testview/_view/testview'
    }
}

</script>


<style lang="scss" scoped>
    .container {
        border: 5px solid black;
    }
</style>
