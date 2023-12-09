<template>
  <div class="bg-gradient-to-r from-red-500 to-red-700 min-h-screen flex flex-col justify-center py-12 sm:px-6 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-md">
      <h2 class="mt-6 text-center text-3xl font-extrabold text-white">
        Sign Up
      </h2>
    </div>
    <div class="mt-8 sm:mx-auto sm:w-full sm:max-w-md">
      <div class="bg-white py-8 px-4 shadow-2xl sm:rounded-lg sm:px-10">
        <form @submit.prevent="signUp" class="space-y-6">
          <div>
            <label for="first_name" class="block text-sm font-medium text-gray-700">
              First Name
            </label>
            <div class="mt-1">
              <input
                v-model.trim="firstName"
                type="text"
                autocomplete="given-name"
                required
                class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm bg-gray-100 text-gray-800"
              />
            </div>
          </div>

          <div>
            <label for="last_name" class="block text-sm font-medium text-gray-700">
              Last Name
            </label>
            <div class="mt-1">
              <input
                v-model.trim="lastName"
                type="text"
                autocomplete="family-name"
                required
                class="appearance-none block w-full px-3 py-2 border rounded-md shadow-sm placeholder-gray-400 border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm bg-gray-100 text-gray-800"
              />
            </div>
          </div>

          <div>
            <label for="email" class="block text-sm font-medium text-gray-700">
              Email address
            </label>
            <div class="mt-1">
              <input
                v-model.trim="email"
                type="email"
                autocomplete="email"
                required
                class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm bg-gray-100 text-gray-800"
              />
            </div>
          </div>
          
          <div>
            <label for="password" class="block text-sm font-medium text-gray-700">
              Password
            </label>
            <div class="relative mt-1">
              <input
                v-model.trim="password"
                :type="show ? 'text' : 'password'"
                autocomplete="new-password"
                required
                class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm bg-gray-100 text-gray-800"
              />
              <div class="flex absolute inset-y-0 right-0 items-center pr-3 text-sm leading-5">
                <button
                  @click="show = !show"
                  type="button"
                  :class="{ 'text-indigo-600': show, 'text-gray-400': !show }"
                  class="focus:text-indigo-500 focus:outline-none"
                >
                  <span v-if="!show">Show</span>
                  <span v-else>Hide</span>
                </button>
              </div>
            </div>
          </div>

          <div>
            <label for="dob" class="block text-sm font-medium text-gray-700">
              Date of Birth
            </label>
            <div class="mt-1">
              <input
                v-model.trim="dob"
                type="date"
                required
                class="appearance-none block w-full px-3 py-2 border rounded-md shadow-sm placeholder-gray-400 border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm bg-gray-100 text-gray-800"
              />
            </div>
          </div>

          <div>
            <label for="age" class="block text-sm font-medium text-gray-700">
              Age
            </label>
            <div class="mt-1">
              <input
                v-model.number="age"
                type="number"
                required
                class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400  focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm bg-gray-100 text-gray-800"
              />
            </div>
          </div>

          <div>
            <label for="gender" class="block text-sm font-medium text-gray-700">
              Gender
            </label>
            <select
              v-model="gender"
              class="mt-1 block w-full py-2 px-3 border border-gray-300 bg-white text-gray-800 rounded-md shadow-sm  focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
            >
              <option value="male">Male</option>
              <option value="female">Female</option>
              <option value="other">Other</option>
            </select>
          </div>

          <div>
            <button
              type="submit"
              class="w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-red-600 hover:bg-red-400 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
            >
              Sign Up
            </button>
          </div>
          <div align="center" class="g-recaptcha" data-sitekey="6LcEiOooAAAAAHPqCjda1gr7oVgGH5kX0IgNPGr_"></div>
          <div class="text-sm">
            <router-link to="/sign-in" class="font-medium text-gray-700 hover:text-blue-500">
              Already have an account?
            </router-link>
          </div>
        </form>
        <!-- <div v-if="message" class="text-green-500 p-2 mx-20 text-xl">{{ message }}</div> -->
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
 data() {
    return {
      formData: {
        firstName: '',
        lastName: '',
        age: '',
        dob: '',
        gender: '',
        email: '',
        password : '',
      },
      // message: '',
      show : false,
    };
  },
  methods: {
  signUp() {
      axios
        .post('http://localhost:3000/api/sign-up', {
          first_name: this.firstName,
          last_name: this.lastName,
          age: this.age,
          dob: this.dob,
          gender: this.gender,
          email: this.email,
          password: this.password,

        })
        .then((response) => {
          this.message = response.data.message;
        })
        .catch((error) => {
          console.error('Error signing up:', error.message);
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
