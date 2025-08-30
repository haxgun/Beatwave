<script lang="ts" setup>
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from '@/components/ui/select'
import { CheckIcon, CopyIcon } from 'lucide-vue-next'
import tinycolor from 'tinycolor2'
import { computed, ref, watch } from 'vue'

const props = defineProps<{
  hex: string
  rgb: { r: number; g: number; b: number }
  alpha: number
}>()

const emit = defineEmits<{
  'update:hex': [value: string]
  'update:rgb': []
  'update:alpha': [value: number]
}>()

const localHex = ref(props.hex)
const localRgb = ref({ ...props.rgb })
const localAlpha = ref(props.alpha)
const colorModel = ref<'hex' | 'rgb' | 'hsl'>('hex')
const isCopied = ref(false)

const localHsl = computed(() => {
  const color = tinycolor(localRgb.value)
  const hsl = color.toHsl()
  return {
    h: Math.round(hsl.h || 0),
    s: Math.round(hsl.s * 100),
    l: Math.round(hsl.l * 100),
  }
})

const editableHsl = ref({ h: 0, s: 0, l: 0 })

const colorString = computed(() => {
  const color = tinycolor(localRgb.value).setAlpha(localAlpha.value / 100)
  switch (colorModel.value) {
    case 'hex':
      return localAlpha.value < 100 ? color.toRgbString() : color.toHexString()
    case 'rgb':
      return color.toRgbString()
    case 'hsl':
      return color.toHslString()
    default:
      return color.toHexString()
  }
})

watch(
  () => props.hex,
  (v) => (localHex.value = v),
)
watch(
  () => props.rgb,
  (v) => {
    localRgb.value = { ...v }
    editableHsl.value = { ...localHsl.value }
  },
  { deep: true },
)
watch(
  () => props.alpha,
  (v) => (localAlpha.value = v),
)
watch(colorModel, (v) => v === 'hsl' && (editableHsl.value = { ...localHsl.value }))

const updateHex = () => emit('update:hex', localHex.value)
const updateRgb = () => emit('update:rgb')
const updateAlpha = () => emit('update:alpha', localAlpha.value)
const updateFromHsl = () => {
  const color = tinycolor({
    h: editableHsl.value.h,
    s: editableHsl.value.s / 100,
    l: editableHsl.value.l / 100,
  })
  const rgb = color.toRgb()
  localRgb.value = { r: rgb.r, g: rgb.g, b: rgb.b }
  localHex.value = color.toHexString()
  emit('update:hex', localHex.value)
  emit('update:rgb')
}

async function copyColor() {
  try {
    await navigator.clipboard.writeText(colorString.value)
    isCopied.value = true
    setTimeout(() => {
      isCopied.value = false
    }, 2000)
  } catch (error) {
    console.error('Ошибка копирования:', error)
    const textArea = document.createElement('textarea')
    textArea.value = colorString.value
    document.body.appendChild(textArea)
    textArea.select()
    document.execCommand('copy')
    document.body.removeChild(textArea)
    isCopied.value = true
    setTimeout(() => {
      isCopied.value = false
    }, 2000)
  }
}

const inputClass =
  'h-8 flex-1 bg-transparent text-xs font-medium transition-colors hover:bg-white/5 [-moz-appearance:textfield] [&::-webkit-inner-spin-button]:appearance-none [&::-webkit-outer-spin-button]:appearance-none'
</script>

<template>
  <div class="flex items-center gap-2 w-full">
    <!-- Селектор модели -->
    <Select v-model="colorModel">
      <SelectTrigger size="sm" class="text-xs shrink-0">
        <SelectValue />
      </SelectTrigger>
      <SelectContent>
        <SelectItem value="hex" class="text-xs">HEX</SelectItem>
        <SelectItem value="rgb" class="text-xs">RGB</SelectItem>
        <SelectItem value="hsl" class="text-xs">HSL</SelectItem>
      </SelectContent>
    </Select>

    <!-- HEX -->
    <div v-if="colorModel === 'hex'" class="flex -space-x-px flex-1">
      <Input
        v-model="localHex"
        :class="[inputClass, 'uppercase rounded-r-none border-r-0']"
        placeholder="HEX"
        @blur="updateHex"
        @keydown.enter="updateHex"
      />
      <div class="relative flex-1">
        <Input
          v-model.number="localAlpha"
          type="number"
          min="0"
          max="100"
          placeholder="A"
          :class="[inputClass, 'rounded-l-none pr-5']"
          @blur="updateAlpha"
          @keydown.enter="updateAlpha"
        />
        <span
          class="absolute right-2 top-1/2 -translate-y-1/2 text-xs text-muted-foreground pointer-events-none"
          >%</span
        >
      </div>
    </div>

    <!-- RGB -->
    <div v-else-if="colorModel === 'rgb'" class="flex -space-x-px flex-1">
      <Input
        v-model.number="localRgb.r"
        type="number"
        min="0"
        max="255"
        placeholder="R"
        :class="[inputClass, 'rounded-r-none border-r-0']"
        @blur="updateRgb"
        @keydown.enter="updateRgb"
      />
      <Input
        v-model.number="localRgb.g"
        type="number"
        min="0"
        max="255"
        placeholder="G"
        :class="[inputClass, 'rounded-none border-r-0']"
        @blur="updateRgb"
        @keydown.enter="updateRgb"
      />
      <Input
        v-model.number="localRgb.b"
        type="number"
        min="0"
        max="255"
        placeholder="B"
        :class="[inputClass, 'rounded-none border-r-0']"
        @blur="updateRgb"
        @keydown.enter="updateRgb"
      />
      <div class="relative flex-1">
        <Input
          v-model.number="localAlpha"
          type="number"
          min="0"
          max="100"
          placeholder="A"
          :class="[inputClass, 'rounded-l-none pr-5']"
          @blur="updateAlpha"
          @keydown.enter="updateAlpha"
        />
        <span
          class="absolute right-2 top-1/2 -translate-y-1/2 text-xs text-muted-foreground pointer-events-none"
          >%</span
        >
      </div>
    </div>

    <!-- HSL -->
    <div v-else-if="colorModel === 'hsl'" class="flex -space-x-px flex-1">
      <Input
        v-model.number="editableHsl.h"
        type="number"
        min="0"
        max="360"
        placeholder="H"
        :class="[inputClass, 'border-r-0 rounded-r-none']"
        @blur="updateFromHsl"
        @keydown.enter="updateFromHsl"
      />
      <div class="relative flex-1">
        <Input
          v-model.number="editableHsl.s"
          type="number"
          min="0"
          max="100"
          placeholder="S"
          :class="[inputClass, 'border-r-0 rounded-none pr-5']"
          @blur="updateFromHsl"
          @keydown.enter="updateFromHsl"
        />
        <span
          class="absolute right-2 top-1/2 -translate-y-1/2 text-xs text-muted-foreground pointer-events-none"
          >%</span
        >
      </div>
      <div class="relative flex-1">
        <Input
          v-model.number="editableHsl.l"
          type="number"
          min="0"
          max="100"
          placeholder="L"
          :class="[inputClass, 'border-r-0 rounded-none pr-5']"
          @blur="updateFromHsl"
          @keydown.enter="updateFromHsl"
        />
        <span
          class="absolute right-2 top-1/2 -translate-y-1/2 text-xs text-muted-foreground pointer-events-none"
          >%</span
        >
      </div>
      <div class="relative flex-1">
        <Input
          v-model.number="localAlpha"
          type="number"
          min="0"
          max="100"
          placeholder="A"
          :class="[inputClass, 'rounded-l-none pr-5']"
          @blur="updateAlpha"
          @keydown.enter="updateAlpha"
        />
        <span
          class="absolute right-2 top-1/2 -translate-y-1/2 text-xs text-muted-foreground pointer-events-none"
          >%</span
        >
      </div>
    </div>

    <!-- Кнопка копирования -->
    <Button
      @click="copyColor"
      size="icon"
      variant="outline"
      class="h-8 w-8 shrink-0"
      :class="{ 'bg-green-50 border-green-200': isCopied }"
    >
      <CheckIcon v-if="isCopied" class="h-3 w-3 text-green-600" />
      <CopyIcon v-else class="h-3 w-3" />
    </Button>
  </div>
</template>
