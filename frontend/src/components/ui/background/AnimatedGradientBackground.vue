<template>
  <div :class="`absolute inset-0 overflow-hidden ${containerClassName}`" :style="motionStyle">
    <div ref="containerRef" :style="containerStyle" class="absolute inset-0 transition-transform" />
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted, onUnmounted, ref, watch, type CSSProperties } from 'vue'

interface Props {
  /**
   * Initial size of the radial gradient, defining the starting width.
   * @default 125
   */
  startingGap?: number

  /**
   * Enables or disables the breathing animation effect.
   * @default false
   */
  breathing?: boolean

  /**
   * Array of colors to use in the radial gradient.
   * Each color corresponds to a stop percentage in `gradientStops`.
   * @default ["#0A0A0A", "#2979FF", "#FF80AB", "#FF6D00", "#FFD600", "#00E676", "#3D5AFE"]
   */
  gradientColors?: string[]

  /**
   * Array of percentage stops corresponding to each color in `gradientColors`.
   * The values should range between 0 and 100.
   * @default [35, 50, 60, 70, 80, 90, 100]
   */
  gradientStops?: number[]

  /**
   * Speed of the breathing animation.
   * Lower values result in slower animation.
   * @default 0.02
   */
  animationSpeed?: number

  /**
   * Maximum range for the breathing animation in percentage points.
   * Determines how much the gradient "breathes" by expanding and contracting.
   * @default 5
   */
  breathingRange?: number

  /**
   * Additional inline styles for the gradient container.
   * @default {}
   */
  containerStyle?: CSSProperties

  /**
   * Additional class names for the gradient container.
   * @default ""
   */
  containerClassName?: string

  /**
   * Additional top offset for the gradient container from the top to have a more flexible control over the gradient.
   * @default 0
   */
  topOffset?: number
}

const props = withDefaults(defineProps<Props>(), {
  startingGap: 125,
  breathing: false,
  gradientColors: () => [
    '#0A0A0A',
    '#2979FF',
    '#FF80AB',
    '#FF6D00',
    '#FFD600',
    '#00E676',
    '#3D5AFE',
  ],
  gradientStops: () => [35, 50, 60, 70, 80, 90, 100],
  animationSpeed: 0.02,
  breathingRange: 5,
  containerStyle: () => ({}),
  containerClassName: '',
  topOffset: 0,
})

// Validation
if (props.gradientColors.length !== props.gradientStops.length) {
  throw new Error(
    `GradientColors and GradientStops must have the same length.
     Received gradientColors length: ${props.gradientColors.length},
     gradientStops length: ${props.gradientStops.length}`,
  )
}

const containerRef = ref<HTMLDivElement | null>(null)
const opacity = ref(0)
const scale = ref(1.5)

// Motion animation для входа
const motionStyle = computed(() => ({
  opacity: opacity.value,
  transform: `scale(${scale.value})`,
  transition:
    'opacity 2s cubic-bezier(0.25, 0.1, 0.25, 1), transform 2s cubic-bezier(0.25, 0.1, 0.25, 1)',
}))

let animationFrame: number
let width = props.startingGap
let directionWidth = 1

const animateGradient = () => {
  if (width >= props.startingGap + props.breathingRange) directionWidth = -1
  if (width <= props.startingGap - props.breathingRange) directionWidth = 1
  if (!props.breathing) directionWidth = 0

  width += directionWidth * props.animationSpeed

  const gradientStopsString = props.gradientStops
    .map((stop, index) => `${props.gradientColors[index]} ${stop}%`)
    .join(', ')

  const gradient = `radial-gradient(${width}% ${width + props.topOffset}% at 50% 20%, ${gradientStopsString})`

  if (containerRef.value) {
    containerRef.value.style.background = gradient
  }

  animationFrame = requestAnimationFrame(animateGradient)
}

const startAnimation = () => {
  animationFrame = requestAnimationFrame(animateGradient)
}

const stopAnimation = () => {
  if (animationFrame) {
    cancelAnimationFrame(animationFrame)
  }
}

// Restart animation when props change
watch(
  () => [
    props.startingGap,
    props.breathing,
    props.gradientColors,
    props.gradientStops,
    props.animationSpeed,
    props.breathingRange,
    props.topOffset,
  ],
  () => {
    stopAnimation()
    width = props.startingGap
    directionWidth = 1
    startAnimation()
  },
  { deep: true },
)

onMounted(() => {
  // Start entrance animation
  setTimeout(() => {
    opacity.value = 1
    scale.value = 1
  }, 50)

  startAnimation()
})

onUnmounted(() => {
  stopAnimation()
})
</script>
