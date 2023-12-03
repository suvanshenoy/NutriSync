<template>
  <div class="w-full">
    <router-view></router-view>
  <!--  <div class="w-full"> 
      <SigninForm />
    </div>
     <div class="w-1/2">
      <SignupForm />
    </div> -->
  </div>
</template>

<script>
import SigninForm from "./components/SigninForm.vue"; 
import SignupForm from "./components/SignupForm.vue"; 
import TestFlask from "./tests/TestFlask.vue";

export default {
  components: {
    SigninForm,
    SignupForm,
    TestFlask,
   
  },
};
</script>

<style>
</style>
