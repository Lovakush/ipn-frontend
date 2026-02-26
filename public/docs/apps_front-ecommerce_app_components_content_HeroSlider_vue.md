# HeroSlider.vue

**Path**: `apps\front-ecommerce\app\components\content\HeroSlider.vue`

## Summary
# HeroSlider Component Summary

This Vue 3 component manages a responsive hero image carousel/slider for an e-commerce front-end, with primary responsibilities including: (1) dynamically rendering active slides with responsive images optimized for mobile and desktop via ImageKit, and (2) tracking user interactions (impressions and clicks) on promotional content through analytics hooks for conversion measurement.

The component leverages intersection observer to detect when slides enter the viewport, manages carousel state (current slide index), and applies CSS custom properties for background images at multiple resolutions to support different device pixel densities.

## Function Details

### `setCurrentIndexImage`

- **Parameters**: `index: number`

### `getBackgroundImageStyle`

- **Parameters**: `index: number, slide: IHeroSlide`

### `initializeIntersectionObserver`


### `trackingPromotion`

- **Parameters**: `pushIndex: number, clicked?: boolean`

### `clearPixieSlides`


### `activeSlides`

- **Parameters**: `computed((`

### `sliderImage`

- **Parameters**: `computed((`

### `isInIndexRange`

- **Parameters**: `index: number`

