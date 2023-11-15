import vue from '@vitejs/plugin-vue'
import {defineConfig} from "vite";
import {fileURLToPath, URL} from "node:url";
import autoprefixer from "autoprefixer";

export default defineConfig({
  devServer: {
    port: 5000
  },
  plugins: [vue()],
  css: {
    postcss: {
      plugins: [autoprefixer({})],
    },
  },
  clearScreen: false,
  resolve: {
    alias: {
      "@": fileURLToPath(new URL('./src', import.meta.url)),
    },
  },
  build: {
    target: "esnext",
  },
});

