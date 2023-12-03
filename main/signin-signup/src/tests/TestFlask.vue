<template>
  <div>
    <h1 class="text-2xl p-2 text-red-500 "> {{ message }}</h1>
    <button @click="sendDataToFlask" class = "border border-white text-white bg-black rounded-md absolute  mx-[40%] my-[40%]  px-20 py-2 mt-0 hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-offset-2">send</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      message: "",
    };
  },
  mounted(){
     document.body.style.backgroundColor = 'black'; 
  },
  beforeDestroy(){
     document.body.style.backgroundColor = '';
  
  },

  methods: {
   async sendDataToFlask() {
      try {
        const axiosResponse = await axios.post('http://localhost:3000/api/test', {
          data: 'Hello from Vue!!',
        });

        this.message = axiosResponse.data.message;
        console.log(this.message)
      } catch (error) {
        console.error('Error sending data to Flask:', error.message);
      }
    },
  },
};
</script>
