<script lang="ts" setup>
const modelValue = defineModel<boolean>({
  default: false,
})

const props = withDefaults(
  defineProps<{
    disabled?: boolean
    id?: string
  }>(),
  {
    disabled: false,
    id: () => `ui-switch-${Math.random().toString(36).slice(2, 9)}`,
  },
)

const updateValue = () => {
  if (!props.disabled) {
    modelValue.value = !modelValue.value
  }
}
</script>

<template>
  <button
    type="button"
    :id="id"
    :aria-checked="modelValue"
    class="inline-flex h-8 cursor-pointer min-w-24 items-center justify-between rounded-md border border-white/10 p-1 font-mono text-sm transition-all duration-200 hover:border-white/15 hover:bg-white/5"
    :disabled="disabled"
    @click="updateValue"
    :style="{ opacity: disabled ? '0.5' : '1' }"
  >
    <span
      class="flex h-full w-1/2 flex-col items-center justify-center rounded transition-colors"
      :class="{
        'bg-switch-checked text-switch-checked-foreground shadow-inner drop-shadow-[0_0_10px_#ffffff4f]':
          modelValue,
        'text-switch-foreground': !modelValue,
      }"
    >
      ON
    </span>
    <span
      class="flex h-full w-1/2 flex-col items-center justify-center rounded transition-colors"
      :class="{
        'bg-switch-checked text-switch-checked-foreground shadow-inner drop-shadow-[0_0_10px_#ffffff4f]':
          !modelValue,
        'text-switch-foreground': modelValue,
      }"
    >
      OFF
    </span>
  </button>
</template>
