import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

//server attribute is used for setting the port number...

export default defineConfig({
  plugins: [vue()],
  server :{
	  port : 3000,
	  },
});
