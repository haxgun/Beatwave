<script lang="ts" setup>
import HeaderItem from '@/components/HeaderItem.vue'
import OverlayItem from '@/components/OverlayItem.vue'
import queryString from 'query-string'
import { computed, ref } from 'vue'

const settings = ref({
  showMaxWidth: false,
  showBorder: true,
  trimArtist: false,
  bgOpacity: 60,
  borderSize: 3
})

const browserSourceUrl = computed(() => {
  const nowPlayingPage = { href: '/overlay/' }
  const base = `${location.origin}${nowPlayingPage.href}`
  const query = queryString.stringify({
    ...settings.value
  })
  return `${base}?${query}`
})
</script>

<template>
  <HeaderItem />
  <div class="main">
    <div class="main__body">
      <div class="blick"></div>
      <div style="align-items: flex-start; gap: 1rem" class="main__container">
        <div class="settings__header">
          <h1>Settings</h1>
          <h2>
            Customize the appearance of the music display. Customize everything to your liking.
          </h2>
        </div>
        <div class="settings">
          <div class="settings__preview">
            <div class="preview">
              <div
                :style="{
                  width: settings.showMaxWidth ? '' : '100%',
                  alignItems: settings.showMaxWidth ? '' : 'center'
                }"
                class="preview__content"
              >
                <OverlayItem
                  class="widget"
                  :showMaxWidth="settings.showMaxWidth"
                  :showBorder="settings.showBorder"
                  :trimArtist="settings.trimArtist"
                  :bgOpacity="settings.bgOpacity"
                  :borderSize="settings.borderSize"
                  :fakeTitle="'Track name'"
                  :fakeArtist="'Artist name'"
                />
              </div>
              <div class="preview__background">
                <img src="@/assets/preview_bg.webp" alt="" />
              </div>
            </div>
            <div class="settings__input">
              <div class="settings__input__left">
                <label>URL</label>
              </div>
              <div class="settings__input__block">
                <span class="input">
                  <InputText
                    id="linkOBS"
                    rows="5"
                    cols="82"
                    class="textarea"
                    readonly
                    v-model="browserSourceUrl"
                  />
                </span>
              </div>
            </div>
          </div>
          <div class="settings__content">
            <span>
              <a-tooltip>
                <template #title>Widget output with no width limit</template>
                <svg
                  width="18"
                  height="18"
                  viewBox="0 0 24 24"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    d="M9.09 9C9.3251 8.33167 9.78915 7.76811 10.4 7.40913C11.0108 7.05016 11.7289 6.91894 12.4272 7.03871C13.1255 7.15849 13.7588 7.52152 14.2151 8.06353C14.6713 8.60553 14.9211 9.29152 14.92 10C14.92 12 11.92 13 11.92 13M12 17H12.01M22 12C22 17.5228 17.5228 22 12 22C6.47715 22 2 17.5228 2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12Z"
                    stroke="white"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                  />
                </svg>
              </a-tooltip>
              <label for="showMaxWidth">Show max width</label>
              <a-switch v-model:checked="settings.showMaxWidth" />
            </span>
            <span>
              <a-tooltip>
                <template #title>Turn off/on the outline of the widget</template>
                <svg
                  width="18"
                  height="18"
                  viewBox="0 0 24 24"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    d="M9.09 9C9.3251 8.33167 9.78915 7.76811 10.4 7.40913C11.0108 7.05016 11.7289 6.91894 12.4272 7.03871C13.1255 7.15849 13.7588 7.52152 14.2151 8.06353C14.6713 8.60553 14.9211 9.29152 14.92 10C14.92 12 11.92 13 11.92 13M12 17H12.01M22 12C22 17.5228 17.5228 22 12 22C6.47715 22 2 17.5228 2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12Z"
                    stroke="white"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                  />
                </svg>
              </a-tooltip>
              <label for="showBorder">Show Border</label>
              <a-switch v-model:checked="settings.showBorder" />
            </span>
            <span>
              <a-tooltip>
                <template #title>Only shows the primary artist for the song.</template>
                <svg
                  width="18"
                  height="18"
                  viewBox="0 0 24 24"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    d="M9.09 9C9.3251 8.33167 9.78915 7.76811 10.4 7.40913C11.0108 7.05016 11.7289 6.91894 12.4272 7.03871C13.1255 7.15849 13.7588 7.52152 14.2151 8.06353C14.6713 8.60553 14.9211 9.29152 14.92 10C14.92 12 11.92 13 11.92 13M12 17H12.01M22 12C22 17.5228 17.5228 22 12 22C6.47715 22 2 17.5228 2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12Z"
                    stroke="white"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                  />
                </svg>
              </a-tooltip>
              <label for="trimArtist">Trim Artist</label>
              <a-switch v-model:checked="settings.trimArtist" />
            </span>
          </div>
          <div class="settings__sliders">
            <span>
              <a-tooltip>
                <template #title
                  >Changes the opacity of the background color. Default is 60%.</template
                >
                <svg
                  width="18"
                  height="18"
                  viewBox="0 0 24 24"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    d="M9.09 9C9.3251 8.33167 9.78915 7.76811 10.4 7.40913C11.0108 7.05016 11.7289 6.91894 12.4272 7.03871C13.1255 7.15849 13.7588 7.52152 14.2151 8.06353C14.6713 8.60553 14.9211 9.29152 14.92 10C14.92 12 11.92 13 11.92 13M12 17H12.01M22 12C22 17.5228 17.5228 22 12 22C6.47715 22 2 17.5228 2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12Z"
                    stroke="white"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                  />
                </svg>
              </a-tooltip>
              <label for="showMaxWidth"
                >Opacity <b>({{ settings.bgOpacity }}%)</b></label
              >
              <a-slider
                :tip-formatter="null"
                style="width: 100px"
                v-model:value="settings.bgOpacity"
              />
            </span>
            <span>
              <a-tooltip>
                <template #title
                  >Changes how rounded the corners of the component and album art are. Default is
                  Medium.</template
                >
                <svg
                  width="18"
                  height="18"
                  viewBox="0 0 24 24"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    d="M9.09 9C9.3251 8.33167 9.78915 7.76811 10.4 7.40913C11.0108 7.05016 11.7289 6.91894 12.4272 7.03871C13.1255 7.15849 13.7588 7.52152 14.2151 8.06353C14.6713 8.60553 14.9211 9.29152 14.92 10C14.92 12 11.92 13 11.92 13M12 17H12.01M22 12C22 17.5228 17.5228 22 12 22C6.47715 22 2 17.5228 2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12Z"
                    stroke="white"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                  />
                </svg>
              </a-tooltip>
              <label for="showMaxWidth"
                >Border Radius <b>({{ settings.borderSize }})</b></label
              >
              <a-slider
                :tip-formatter="null"
                style="width: 100px"
                v-model:value="settings.borderSize"
                :min="0"
                :max="5"
              />
            </span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.code-box-demo .ant-slider {
  margin-bottom: 16px;
}

.settings__sliders {
  display: flex;
  flex-direction: column;
  width: max-content;

  span {
    display: flex;
    align-items: center;
  }
}
</style>
