<template>
  <div class="flex flex-col justify-center py-12 min-h-screen bg-gradient-to-r from-red-500 to-red-700 p-4 text-white ">
    <div class="sm:mx-auto sm:w-full sm:max-w-md">
      <h2 class="mt-6 text-3xl font-extrabold text-center">Sign In</h2>
    </div>
    <div class="mt-8 sm:mx-auto sm:w-full sm:max-w-md">
      <div class="py-8 px-4 shadow-2xl bg-white sm:px-10 sm:rounded-lg">
        <form @submit.prevent="signIn" class="space-y-6">
          <div>
            <label for="user_name" class="block text-sm font-medium text-gray-700">Username</label>
            <div class="mt-1">
              <input
                v-model.trim="username"
                type="text"
                autocomplete="user-name"
                required
                class="block w-full py-2 px-4 placeholder-gray-500 text-gray-700 bg-gray-100 border-2 border-gray-200 rounded-md focus:outline-none focus:border-blue-500"
              />
            </div>
          </div>
          <div>
            <label for="email" class="block text-sm font-medium text-gray-700">Email address</label>
            <div class="mt-1">
              <input
                v-model.trim="email"
                type="email"
                autocomplete="email"
                required
                class="block w-full py-2 px-4 placeholder-gray-500 text-gray-700 bg-gray-100 border-2 border-gray-200 rounded-md focus:outline-none focus:border-blue-500"
              />
            </div>
          </div>
          <div>
            <label for="password" class="block text-sm font-medium text-gray-700">Password</label>
            <div class="relative mt-1">
              <input
                v-model="password"
                :type="show ? 'text' : 'password'"
                autocomplete="current-password"
                required
                class="block w-full py-2 px-4 placeholder-gray-500 text-gray-700 bg-gray-100 border-2 border-gray-200 rounded-md focus:outline-none focus:border-blue-500"
              />
              <div class="flex absolute inset-y-0 right-0 items-center pr-3 text-sm leading-5">
                <button
                  @click="show = !show"
                  type="button"
                  :class="{ 'text-blue-600': show, 'text-gray-400': !show }"
                  class="focus:text-blue-500 focus:outline-none"
                >
                  <span v-if="!show">Show</span>
                  <span v-else>Hide</span>
                </button>
              </div>
            </div>
          </div>
          <div class="flex justify-between items-center">
            <div class="flex items-center">
              <input
                id="remember_me"
                name="remember_me"
                type="checkbox"
                class="w-4 h-4 text-blue-600 rounded border-gray-300 focus:ring-blue-500"
              />
              <label for="remember_me" class="block ml-2 text-sm text-gray-700">Remember me</label>
            </div>
            <div class="text-sm">
              <router-link to="/sign-up" class="font-medium text-gray-700 hover:text-blue-500">
                Don't have an account?
              </router-link>
            </div>
          </div>
          <div>
            <button
              type="submit"
              class="flex justify-center py-2 px-4 w-full text-sm font-medium text-white bg-red-600 rounded-md border border-transparent hover:bg-red-500 focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 focus:outline-none group"
            >
              Sign in
            </button>
          </div>
          <div align="center" class="g-recaptcha" 
          data-sitekey="6LcEiOooAAAAAHPqCjda1gr7oVgGH5kX0IgNPGr_"></div>
        </form>
        <div class="mt-6">
          <div class="relative">
            <div class="flex absolute inset-0 items-center" aria-hidden="true">
              <div class="w-full border-t border-gray-700"></div>
            </div>
            <div class="flex relative justify-center text-sm">
              <span class="px-2 text-gray-700 bg-white">Or continue with</span>
            </div>
          </div>
        </div>
        <div class="grid grid-cols-3 gap-3 mt-6">
          <GoogleLogin />
          <FacebookLogin />
          <InstagramLogin />
        </div>
      </div>
    </div>
  </div>
</template>

 <script>
import GoogleLogin from "./GoogleLogin.vue";
import FacebookLogin from "./FacebookLogin.vue";
import InstagramLogin from "./InstagramLogin.vue";
import axios from 'axios';

export default {
  components: {
    GoogleLogin,
    FacebookLogin,
    InstagramLogin,
  },
   data() {
    return {
      email: "",
      password: "",
      username : "",
      message : "",
      show: false,
    };
  },
  
  methods: {
  async signIn(){
   axios
        .post('http://localhost:3000/api/sign-in', {
          username : this.userName,
          email: this.email,
          password: this.password,

        })
        .then(res => {
        if(res.data.redirect){
           window.location.href = res.data.redirect;
          }else{
            this.message = res.data.message;
          }
        })
        .catch((error) => {
          console.error('Error signing in:', error.message);
          // Handle errors
          if (error.response) {
            this.message = `Error: ${error.response.data.message}`;
          } else if (error.request) {
            this.message = 'Error: No response received from the server.';
          } else {
            this.message = `Error: ${error.message}`;
          }
        });
      },
    },
};
</script>
