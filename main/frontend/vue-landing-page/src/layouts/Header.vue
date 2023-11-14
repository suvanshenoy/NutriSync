<script setup>
    import { ref } from 'vue';

    let mobileNav = ref(false);

    let toggleMobileNav = () => {
        mobileNav.value = !mobileNav.value
    }
</script>

<template>
    <!-- Navbar Start -->
    <div class="container mx-auto px-5">
        <header class="flex justify-between py-12 items-center">
            <div>
                <a href="/"><img src="/images/logo.png" alt="Site Logo" width="250" height="200"></a>
            </div>
            
            <nav class="flex justify-end flex-col md:flex-row">
                <!-- Menu Toggler -->
                <button @click="toggleMobileNav()" type="button" class="flex md:hidden focus:outline-none">
                    <svg viewBox="0 0 24 24" class="h-6 w-6 fill-current">
                        <path fill-rule="evenodd" d="M4 5h16a1 1 0 0 1 0 2H4a1 1 0 1 1 0-2zm0 6h16a1 1 0 0 1 0 2H4a1 1 0 0 1 0-2zm0 6h16a1 1 0 0 1 0 2H4a1 1 0 0 1 0-2z"></path>
                    </svg>
                </button>

                <!-- Desktop Menu -->
                <ul class="space-x-10 font-theme-heading font-medium items-center hidden md:flex  flex-col space-y-7 md:space-y-0 md:flex-row">
                    <li class="uppercase hover:text-theme-secondary transition duration-200"><a href="#plans" v-smooth-scroll>Plans</a></li>
                    <li class="uppercase hover:text-theme-secondary transition duration-200"><a href="#faq" v-smooth-scroll>FAQ</a></li>
                    <li class="uppercase hover:text-theme-secondary transition duration-200"><a href="#about" v-smooth-scroll>About</a></li>
                    <li class="uppercase bg-theme-secondary px-6 py-2 text-white rounded shadow-md hover:bg-white border-2 border-transparent hover:border-theme-secondary hover:text-theme-secondary cursor-pointer transition duration-200">
                        <a href="#contact-section" v-smooth-scroll>Contact</a>
                    </li>
                </ul>
            </nav>
        </header>

        <!-- Desktop Menu End-->
    </div>
    <!-- Navbar End -->
</template>