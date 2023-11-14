<script>
import GoogleLogin from "./GoogleLogin.vue";
import FacebookLogin from "./FacebookLogin.vue";
import InstagramLogin from "./InstagramLogin.vue";
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
			show: false,
		};
	},
	methods: {
		login() {
			console.warn(this.email, this.password);
		},
	},
};
</script>

<template>
	<div
		class="flex flex-col justify-center py-12 min-h-screen bg-gradient-to-r from-red-600 via-red-500 to-red-400 sm:px-6 lg:px-8">
		<div class="sm:mx-auto sm:w-full sm:max-w-md">
			<h2 class="mt-6 text-3xl font-extrabold text-center text-gray-100">
				SIGN IN TO YOUR ACCOUNT
			</h2>
		</div>
		<div class="mt-8 sm:mx-auto sm:w-full sm:max-w-md">
			<div class="py-8 px-4 bg-gray-800 shadow sm:px-10 sm:rounded-lg">
				<form action="http://localhost:3000/api/v1/index" method="POST" class="space-y-6">
					<div>
						<label for="email" class="block text-sm font-medium text-gray-300">
							Email address
						</label>
						<div class="mt-1">
							<input v-model.trim="email" type="email" autocomplete="email" required
								class="block py-2 px-3 w-full placeholder-gray-400 text-gray-100 bg-gray-700 rounded-md border border-gray-300 shadow-sm appearance-none sm:text-sm focus:border-indigo-500 focus:ring-indigo-500 focus:outline-none" />
						</div>
					</div>
					<div>
						<label for="password" class="block text-sm font-medium text-gray-300">
							Password
						</label>
						<div class="relative mt-1">
							<input v-model="password" :type="show ? 'text' : 'password'" autocomplete="current-password" required
								class="block py-2 px-3 w-full placeholder-gray-400 text-gray-100 bg-gray-700 rounded-md border border-gray-300 shadow-sm appearance-none sm:text-sm focus:border-indigo-500 focus:ring-indigo-500 focus:outline-none" />
							<div class="flex absolute inset-y-0 right-0 items-center pr-3 text-sm leading-5">
								<button @click="show = !show" type="button" :class="{ 'text-indigo-600': show, 'text-gray-400': !show }"
									class="focus:text-indigo-500 focus:outline-none">
									<span v-if="!show">Show</span>
									<span v-else>Hide</span>
								</button>
							</div>
						</div>
					</div>

					<div class="flex justify-between items-center">
						<div class="flex items-center">
							<input id="remember_me" name="remember_me" type="checkbox"
								class="w-4 h-4 text-indigo-600 rounded border-gray-300 focus:ring-indigo-500" />
							<label for="remember_me" class="block ml-2 text-sm text-gray-300">
								Remember me
							</label>
						</div>
						<div class="text-sm">
							<router-link to="/signup" class="font-medium text-white hover:white">
								Doesn't have an account?
							</router-link>
						</div>
					</div>
					<div>
						<button v-on:click="login" type="submit"
							class="flex relative justify-center py-2 px-4 w-full text-sm font-medium text-white bg-red-600 rounded-md border border-transparent hover:bg-red-400 focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 focus:outline-none group">
							Sign in
						</button>
					</div>

					<div align="center" class="g-recaptcha" data-sitekey="6LcEiOooAAAAAHPqCjda1gr7oVgGH5kX0IgNPGr_"></div>
				</form>
				<div class="mt-6">
					<div class="relative">
						<div class="flex absolute inset-0 items-center" aria-hidden="true">
							<div class="w-full border-t border-gray-700"></div>
						</div>
						<div class="flex relative justify-center text-sm">
							<span class="px-2 text-gray-400 bg-gray-800">Or continue with</span>
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
