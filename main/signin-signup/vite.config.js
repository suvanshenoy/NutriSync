import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

//server attribute is used for setting the port number...

export default defineConfig({
  build: {
    base : '/static/js/',
    outDir: "./backend/static/js",
    emptyOutDir : true,
  },
  plugins: [vue()],
  server: {
    port : 5000,
  }
});
