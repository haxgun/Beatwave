<script setup>
import GithubIcon from '@/components/icons/GithubIcon.vue'
import MelodyIcon from '@/components/icons/MelodyIcon.vue'
</script>

<template>
  <nav>
    <div class="nav">
      <router-link :to="{ name: 'index' }">
        <MelodyIcon size="40" />
      </router-link>
      <div class="navigation">
        <router-link :to="{ name: 'settings' }"> Get started </router-link>
        <router-link :to="{ name: 'settings' }"> Customize </router-link>
        <router-link :to="{ name: 'settings' }"> OBS Setup </router-link>
      </div>
      <div class="socials">
        <a href="https://github.com/haxgun/Milady" target="__blank">
          <GithubIcon size="20" />
        </a>
      </div>
    </div>
  </nav>
</template>

<style scoped lang="scss">
nav {
  position: sticky;
  top: 0;
  padding-top: 0.9rem;
  padding-bottom: 0.9rem;
  background-color: hsla(0, 0%, 100%, 0.05);
  border-bottom: 1px solid hsla(0, 0%, 100%, 0.2);
  backdrop-filter: blur(12px);

  .nav {
    max-width: 80rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-left: auto;
    margin-right: auto;

    a {
      &:hover {
        color: #e2e2e2;
      }
      font-size: 1.1rem;
      font-weight: 600;
      color: #fff;
      text-decoration: none;
      transition: 0.2s color;
      line-height: 0;
    }

    .navigation {
      display: flex;
      gap: 26px;
    }

    .socials {
      display: flex;
      gap: 20px;

      a {
        padding: 8px;
        background-color: rgb(255 255 255 / 0.05);
        border: 1px rgb(255 255 255 / 0.25) solid;
        border-radius: 8px;
        transition: 0.2s background-color;
        line-height: 0;

        &:hover {
          background-color: rgb(255 255 255 / 0.1);
        }
      }
    }
  }
}
</style>
