import vue from '@vitejs/plugin-vue'
import {defineConfig} from "vite";
import {fileURLToPath, URL} from "node:url";
import autoprefixer from "autoprefixer";
import Components from 'unplugin-vue-components/vite';
import { AntDesignVueResolver } from 'unplugin-vue-components/resolvers';

export default defineConfig({
  devServer: {
    port: 5000
  },
  plugins: [
    vue(), 
    Components({
      resolvers: [
        AntDesignVueResolver({
          importStyle: false, // css in js
        }),
      ],
    })
  ],
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

