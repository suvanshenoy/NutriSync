<script setup></script>

<template>
    <!-- Hero Section Start -->
    <div class="container mx-auto px-5 overflow-x-hidden lg:overflow-x-visible">
        <section class="grid grid-cols-none lg:grid-cols-2 pb-16 pt-8 items-center">
            <div class="lg:w-5/6 order-2 lg:order-none">
                <h1 class="text-4xl xl:text-5xl font-bold font-theme-heading text-center lg:text-left">Welcome to NutriSync: Your Health Companion</h1>
                <p class="lg:text-xl mt-10 font-theme-content text-theme-grayish-blue text-center lg:text-left">Are you ready to take charge of your health and transform your lifestyle for the better? Look no further than NutriSync, your comprehensive health app designed to help you achieve your wellness goals. </p>
                <div class="flex justify-center lg:justify-start mt-10">
                    <LinkButton btn-type="primary" link="">Sign up</LinkButton>
                    <LinkButton btn-type="muted" link="">Log in</LinkButton>
                </div>
            </div>
            <div class="relative order-1 lg:order-none mb-20 lg:mt-0 lg:mb-0 lg:-mr-10">
                <img class="z-10 w-full" src="/images/illustration-hero.svg" />
               
            </div>
        </section>
    </div>
    <!-- Hero Section End -->
</template>
