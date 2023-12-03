import SigninForm from '../components/SigninForm.vue';
import SignupForm from '../components/SignupForm.vue';
import TestFlask from '../tests/TestFlask.vue';

export default [
  { path: '/sign-in', component: SigninForm }, // Route for SigninForm
  { path: '/sign-up', component: SignupForm }, // Route for SignupForm
  { path: '/api/test', component : TestFlask },
];
