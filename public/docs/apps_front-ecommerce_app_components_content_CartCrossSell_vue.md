# CartCrossSell.vue

**Path**: `apps\front-ecommerce\app\components\content\CartCrossSell.vue`

## Summary
# CartCrossSell Component Summary

This Vue 3 component manages cross-sell product recommendations on the shopping cart page by fetching personalized product suggestions based on cart contents or falling back to classification-based defaults. It computes a dynamic cross-sell identifier from the cart's classification level, attempts to retrieve AI-driven recommendations via the `getCartCrossSellRecommendations` API using cart item details (variant, quantity, price), and gracefully falls back to pre-configured CMS cross-sell content if the recommendation service fails. The resulting product list is then passed to a child `CrossSell` component for rendering with appropriate tracking metadata for analytics.

## Function Details

### `crossSellName`

- **Parameters**: `computed((`

### `cartItemsForRecommendation`

- **Parameters**: `computed((`

### `crossSellParams`

- **Parameters**: `computedAsync(async (`

