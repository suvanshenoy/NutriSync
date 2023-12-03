<script>
export default{
     props:{

        btnType:{
           type : String,
        },
        link:{
            type :  String,
            required : true,
        },
        label:{
            type : String,
            required : true,
        },
        class:{
            type:String,
            default:"text-sm sm:text-md md:text-base",
        },
    },
    
};
</script>

<template>
    <a  v-if="btnType === 'primary'" :href="link" :class="class"   class="font-theme-heading font-medium bg-red-500 px-6 py-2 text-white rounded shadow-md hover:bg-white border-2 border-transparent hover:border-theme-primary hover:text-theme-primary cursor-pointer transition duration-200 mr-5">
        {{ label }}
    </a>
    <a v-if="btnType === 'muted'" :href="link" :class="class" class="font-theme-heading font-medium bg-gray-100 text-gray-500 px-6 py-2 rounded shadow-md hover:bg-white border-2 border-transparent hover:border-theme-grayish-blue hover:text-theme-grayish-blue cursor-pointer transition duration-200">
        {{ label }}
    </a>
</template>
