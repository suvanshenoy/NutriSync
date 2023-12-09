<template>
  <div class="w-full">
    <router-view></router-view>
  </div>
</template>

<script>
import SigninForm from "./components/SigninForm.vue"; 
import SignupForm from "./components/SignupForm.vue"; 

export default {
  components: {
    SigninForm,
    SignupForm,
   
  },
};
</script>

<style>
</style>
