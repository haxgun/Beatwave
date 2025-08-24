<script setup lang="ts">
// import Silk from '@/components/ui/Silk.vue';
import Configuration from '@/components/dashboard-page/Configuration.vue'
import DefaultOverlay from '@/components/overlays/DefaultOverlay.vue'
import DashboardLayout from '@/layouts/DashboardLayout.vue'
</script>

<template>
  <DashboardLayout>
    <div class="inline-flex size-full">
      <div class="flex-1 h-full flex items-center justify-center relative overflow-hidden">
        <DefaultOverlay />
        <!--      <Silk-->
        <!--        :speed="5"-->
        <!--        :scale="1"-->
        <!--        :color="'#7B7481'"-->
        <!--        :noise-intensity="1.5"-->
        <!--        :rotation="0"-->
        <!--        class="w-full h-full -z-10"-->
        <!--      />-->
      </div>
      <Configuration />
    </div>
  </DashboardLayout>
</template>
