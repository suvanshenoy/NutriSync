<template>
  <div class="bg-gray-900 min-h-screen flex flex-col justify-center py-12 bg-gradient-to-r from-red-600 via-red-500 to-red-400 sm:px-6 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-md">
      <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-100">
        CREATE AN ACCOUNT
      </h2>
    </div>
    <div class="mt-8 sm:mx-auto sm:w-full sm:max-w-md">
      <div class="bg-gray-800 py-8 px-4 shadow sm:rounded-lg sm:px-10">
        <form @submit.prevent="submitForm" class="space-y-6">
          <div>
            <label for="first_name" class="block text-sm font-medium text-gray-300">
              First Name
            </label>
            <div class="mt-1">
              <input
                v-model.trim="firstName"
                type="text"
                autocomplete="given-name"
                required
                class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm bg-gray-700 text-gray-100"
              />
            </div>
          </div>

          <div>
            <label for="last_name" class="block text-sm font-medium text-gray-300">
              Last Name
            </label>
            <div class="mt-1">
              <input
                v-model.trim="lastName"
                type="text"
                autocomplete="family-name"
                required
                class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm bg-gray-700 text-gray-100"
              />
            </div>
          </div>

          <div>
            <label for="email" class="block text-sm font-medium text-gray-300">
              Email address
            </label>
            <div class="mt-1">
              <input
                v-model.trim="email"
                type="email"
                autocomplete="email"
                required
                class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm bg-gray-700 text-gray-100"
              />
            </div>
          </div>

          <div>
            <label for="dob" class="block text-sm font-medium text-gray-300">
              Date of Birth
            </label>
            <div class="mt-1">
              <input
                v-model.trim="dob"
                type="date"
                required
                class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm bg-gray-700 text-gray-100"
              />
            </div>
          </div>

          <div>
            <label for="age" class="block text-sm font-medium text-gray-300">
              Age
            </label>
            <div class="mt-1">
              <input
                v-model.number="age"
                type="number"
                required
                class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm bg-gray-700 text-gray-100"
              />
            </div>
          </div>

          <div>
            <label for="gender" class="block text-sm font-medium text-gray-300">
              Gender
            </label>
            <select v-model="gender" class="mt-1 block w-full py-2 px-3 border border-gray-300 bg-gray-700 text-gray-100 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm">
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
            <div class="text-gray-900">
              <h1>
              .
              </h1>
            </div>
            <div align="center" class="g-recaptcha" data-sitekey="6LcEiOooAAAAAHPqCjda1gr7oVgGH5kX0IgNPGr_"></div>
            <div class="text-sm">

							<router-link to="/signin" class="font-medium text-white hover:white align-baseline">
								Already have an account?
							</router-link>
						</div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      firstName: '',
      lastName: '',
      email: '',
      dob: '',
      age: null,
      gender: 'male', // Default value for gender
    };
  },
  methods: {
    submitForm() {
      // Implement your form submission logic here
    },
  },
};
</script>
