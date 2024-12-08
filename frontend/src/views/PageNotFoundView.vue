<script setup lang="ts">
</script>

<template>
  <div class="main">
    <div class="main__body">
      <div class="main__container">
        <div class="blick3"></div>
        <div class="main__container">
          <h1 class="title">
              Oops! It seems you've hit a wrong note.
          </h1>
<!--          <p class="subtitle">This page is missing or you wrote the link incorrectly.</p>-->
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.main {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-wrap: nowrap;
  flex-direction: column;
  height: 100vh;
}

.blick3 {
  position: absolute;
  top: 50%;
  display: flex;
  background-color: rgba(169, 73, 73, 0.2);
  margin: auto;
  width: 50%;
  height: 10rem;
  border-radius: 50%;
  filter: blur(150px);
}

//.title {
//  margin: 0;
//  font-weight: bold;
//  font-size: 24px;
//}
//
//.subtitle {
//  margin: 0;
//  font-weight: 300;
//  font-size: 15px;
//  color: #9f9f9f;
//  position: relative;
//  top: -20px;
//}
</style>
