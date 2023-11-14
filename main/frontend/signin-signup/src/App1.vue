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
import SigninForm from "./components/SigninForm.vue"; // Corrected the import statement
import SignupForm from "./components/SignupForm.vue"; // Corrected the import statement

export default {
  components: {
    SigninForm,
    SignupForm
   
  },
};
</script>

<style>
</style>
