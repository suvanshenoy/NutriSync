<script>
import LinkButton from "../components/LinkButton.vue";

export default {
  components: {
    LinkButton,
  },
  data() {
    return {
      primaryLink: "http://localhost:5001/sign-up",
      mutedLink: "http://localhost:5001/sign-in",
    };
  },
};
</script>

<template>
  <!-- Hero Section Start -->
  <div class="container overflow-x-hidden px-5 mx-auto lg:overflow-x-visible">
    <section class="grid grid-cols-none items-center pt-8 pb-16 lg:grid-cols-2">
      <div class="order-2 lg:order-none lg:w-5/6">
        <h1 class="text-4xl font-bold text-center lg:text-left xl:text-5xl font-theme-heading">
          Welcome to NutriSync: Your Health Companion
        </h1>
        <p class="mt-10 text-center lg:text-xl lg:text-left font-theme-content text-theme-grayish-blue">
          Are you ready to take charge of your health and transform your
          lifestyle for the better? Look no further than NutriSync, your
          comprehensive health app designed to help you achieve your wellness
          goals.
        </p>
        <div class="flex justify-center mt-10 lg:justify-start">
          <LinkButton btn-type="primary" label="Sign up" :link="primaryLink" />
          <LinkButton btn-type="muted" label="Sign in" :link="mutedLink" />
        </div>
      </div>
      <div class="relative order-1 mb-20 lg:order-none lg:mt-0 lg:mb-0 lg:-mr-10">
        <img class="z-10 w-full" src="/images/illustration-hero.svg" />
      </div>
    </section>
  </div>
  <!-- Hero Section End -->
</template>
