<script setup lang="ts">
import { Menu, X } from 'lucide-vue-next'

const props = defineProps<{
  isOpen: boolean
}>()

const emit = defineEmits(['click'])

function handleClick() {
  emit('click')
}
</script>

<template>
  <div class="cursor-pointer" @click="handleClick">
    <X v-if="isOpen" class="text-white" />
    <Menu v-else class="text-white" />
  </div>
</template>
