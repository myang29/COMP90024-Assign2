<template>
  <div class="hello">
    <!-- interpplation, use a value defined in script data-->
    {{ name }}

    <!-- interpolation, js expression-->
    {{ btnState ? 'The button is disabled' : 'The button is active' }}
    <!-- interpolation in the attribute, no {{xx}}-->
    <button v-on:click="changeName" v-bind:disabled="btnState">Change Name </button>

    <!-- interpolation, iterat over list objects -->
    <ul>
      <li v-for="(data, index) in skills" :key='index'> {{ index }}. {{data.skill}} </li>
    </ul>

    <!-- interpolation, if-else-->
    <p v-if="skills.length >= 1">You have more than 1 skills </p>
    <p v-else>You have less than one or equal to one skill</p>

    <!-- bind classes(css styles) to a div -->
    <div v-bind:class="{ alert: showAlert, 'another-class': showClass}"></div>
    <!-- reference an object/property to handle diff classes -->
    <div v-bind:class="alertObject"></div>
    <!-- directly write the style in template-->
    <div v-bind:style="{ backgroundColor: bgcolor, width: bgwid, height: bgheight}"></div>
  </div>
</template>

<script>
export default {
  name: 'Frontend',
  data() {
    return {
      name: 'CCC Project 2',
      btnState: true,
      skills: [
        {"skill": "Vue.js"},
        {"skill": "Frontend Developer"}
      ],
      showAlert: true,
      showClass: true,
      alertObject: {
        alert:true,
        "another-class": true
      },
      bgcolor: 'yellow',
      bhwid: '100%',
      bgheight: '30px'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.alert {
  background-color: yellow;
  width: 100%;
  height: 30px;
}

.another-class {
  border: 5px solid black;
}
</style>
