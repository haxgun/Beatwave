<template>
  <Header />
  <div class="main">
    <div class="main__body">
      <div class="blick"></div>
      <div style="align-items: flex-start; gap: 1rem;" class="main__container">
        <div class="settings__header">
            <h1>Settings</h1>
            <h2>Customize the appearance of the music display. Customize everything to your liking.</h2>
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
                <Overlay
                  class="widget"
                  :showMaxWidth="settings.showMaxWidth"
                  :showBorder="settings.showBorder"
                  :trimArtist="settings.trimArtist"
                  :bgOpacity="settings.bgOpacity"
                  :borderSize="settings.borderSize"
                  :fakeTitle="'Track name'"
                  :fakeArtist="'Artist name'"
                  :accessToken="accessToken"
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
              <div @click="copy(browserSourceUrl)" class="settings__input__block">
                <span class="copy">
                  <span>
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path d="M8 8V5.2C8 4.0799 8 3.51984 8.21799 3.09202C8.40973 2.71569 8.71569 2.40973 9.09202 2.21799C9.51984 2 10.0799 2 11.2 2H18.8C19.9201 2 20.4802 2 20.908 2.21799C21.2843 2.40973 21.5903 2.71569 21.782 3.09202C22 3.51984 22 4.0799 22 5.2V12.8C22 13.9201 22 14.4802 21.782 14.908C21.5903 15.2843 21.2843 15.5903 20.908 15.782C20.4802 16 19.9201 16 18.8 16H16M5.2 22H12.8C13.9201 22 14.4802 22 14.908 21.782C15.2843 21.5903 15.5903 21.2843 15.782 20.908C16 20.4802 16 19.9201 16 18.8V11.2C16 10.0799 16 9.51984 15.782 9.09202C15.5903 8.71569 15.2843 8.40973 14.908 8.21799C14.4802 8 13.9201 8 12.8 8H5.2C4.0799 8 3.51984 8 3.09202 8.21799C2.71569 8.40973 2.40973 8.71569 2.21799 9.09202C2 9.51984 2 10.0799 2 11.2V18.8C2 19.9201 2 20.4802 2.21799 20.908C2.40973 21.2843 2.71569 21.5903 3.09202 21.782C3.51984 22 4.07989 22 5.2 22Z" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                    Click To Copy Widget URL</span>
                </span>
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
            <!-- <span>
              <label for="showMaxWidth">Choosing a preset</label>
              <a-space>
                <a-select v-model:value="value3" style="width: 120px" loading :options="options3"></a-select>
              </a-space>
            </span> --> 
            
              <span>
                <a-tooltip>
                  <template #title>Widget output with no width limit</template>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M9.09 9C9.3251 8.33167 9.78915 7.76811 10.4 7.40913C11.0108 7.05016 11.7289 6.91894 12.4272 7.03871C13.1255 7.15849 13.7588 7.52152 14.2151 8.06353C14.6713 8.60553 14.9211 9.29152 14.92 10C14.92 12 11.92 13 11.92 13M12 17H12.01M22 12C22 17.5228 17.5228 22 12 22C6.47715 22 2 17.5228 2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12Z" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </a-tooltip>
                <label for="showMaxWidth">Show max width</label>
                <a-switch v-model:checked="settings.showMaxWidth" />
              </span>
            <span>
              <a-tooltip>
                  <template #title>Turn off/on the outline of the widget</template>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M9.09 9C9.3251 8.33167 9.78915 7.76811 10.4 7.40913C11.0108 7.05016 11.7289 6.91894 12.4272 7.03871C13.1255 7.15849 13.7588 7.52152 14.2151 8.06353C14.6713 8.60553 14.9211 9.29152 14.92 10C14.92 12 11.92 13 11.92 13M12 17H12.01M22 12C22 17.5228 17.5228 22 12 22C6.47715 22 2 17.5228 2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12Z" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </a-tooltip>
              <label for="showBorder">Show Border</label>
              <a-switch v-model:checked="settings.showBorder" />
            </span>
            <span>
              <a-tooltip>
                  <template #title>Only shows the primary artist for the song.</template>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M9.09 9C9.3251 8.33167 9.78915 7.76811 10.4 7.40913C11.0108 7.05016 11.7289 6.91894 12.4272 7.03871C13.1255 7.15849 13.7588 7.52152 14.2151 8.06353C14.6713 8.60553 14.9211 9.29152 14.92 10C14.92 12 11.92 13 11.92 13M12 17H12.01M22 12C22 17.5228 17.5228 22 12 22C6.47715 22 2 17.5228 2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12Z" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </a-tooltip>
              <label for="trimArtist">Trim Artist</label>
              <a-switch v-model:checked="settings.trimArtist" />
            </span>
            <!-- <span>
              <label for="showMaxWidth">Adaptive Color</label>
              <a-switch v-model:checked="settings.showMaxWidth" />
            </span> -->
          </div>
          <div class="settings__sliders">
            <span>
              <a-tooltip>
                <template #title>Changes the opacity of the background color. Default is 60%.</template>
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M9.09 9C9.3251 8.33167 9.78915 7.76811 10.4 7.40913C11.0108 7.05016 11.7289 6.91894 12.4272 7.03871C13.1255 7.15849 13.7588 7.52152 14.2151 8.06353C14.6713 8.60553 14.9211 9.29152 14.92 10C14.92 12 11.92 13 11.92 13M12 17H12.01M22 12C22 17.5228 17.5228 22 12 22C6.47715 22 2 17.5228 2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12Z" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </a-tooltip>
              <label for="showMaxWidth">Opacity <b>({{ settings.bgOpacity }}%)</b></label>
              <a-slider :tip-formatter="null" style="width: 100px;" v-model:value="settings.bgOpacity" />
            </span>
            <span>
              <a-tooltip>
                <template #title>Changes how rounded the corners of the component and album art are. Default is Medium.</template>
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M9.09 9C9.3251 8.33167 9.78915 7.76811 10.4 7.40913C11.0108 7.05016 11.7289 6.91894 12.4272 7.03871C13.1255 7.15849 13.7588 7.52152 14.2151 8.06353C14.6713 8.60553 14.9211 9.29152 14.92 10C14.92 12 11.92 13 11.92 13M12 17H12.01M22 12C22 17.5228 17.5228 22 12 22C6.47715 22 2 17.5228 2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12Z" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </a-tooltip>
              <label for="showMaxWidth">Border Radius <b>({{ settings.borderSize }})</b></label>
              <a-slider :tip-formatter="null" style="width: 100px;" v-model:value="settings.borderSize"  :min="0" :max="5"/>
            </span>
          </div>
          <!-- <div class="settings__description">
            <p class="settings__description__title">
              Options
            </p>
            <ul>
              <li><span>Choosing a preset</span> - Choose the preset that suits you</li>
              <li><span>Adaptive Color</span> - Changes the background color of the song display to match the album art.</li>
            </ul>
          </div> -->
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Overlay from '@/components/Overlay.vue'
import copy from 'copy-to-clipboard'
import queryString from 'query-string'
import Header from '@/components/Header.vue'

export default {
  components: { Overlay, Header },

  computed: {
    copy() {
      return copy
    },
    accessToken() {
      const parsed = queryString.parse(this.$route.hash)
      return parsed['access_token']
    },

    browserSourceUrl() {
      const nowPlayingPage = this.$router.resolve({ name: 'overlay' }),
        base = `${location.origin}${nowPlayingPage.href}`

      const query = queryString.stringify({
        accessToken: this.accessToken,
        ...this.settings
      })

      return `${base}?${query}`
    }
  },

  data: () => ({
    settings: {
      showMaxWidth: false,
      showBorder: true,
      trimArtist: false,
      bgOpacity: 60,
      borderSize: 3,
    }
  })
}
</script>

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
