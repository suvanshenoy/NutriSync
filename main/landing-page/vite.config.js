import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

// https://vitejs.dev/config/
export default defineConfig({
  base: "/nutriSync-landing-page/",
  plugins: [vue()],
  server: {
    port: 5000,
  },
});
