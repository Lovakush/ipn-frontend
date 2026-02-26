# CartPromoTag.vue

**Path**: `apps\front-ecommerce\app\components\cart\CartPromoTag.vue`

## Summary
# CartPromoTag.vue Summary

This Vue component renders a promotional code tag that allows users to copy a promotion code to their clipboard and tracks the interaction for analytics. When clicked, it executes the `copyPromotionCode` function which copies the code (if supported by the browser), logs a tracking event with the code and location context, and dynamically updates the UI icon from a copy symbol to a checkmark to confirm the action.

## Function Details

### `copyPromotionCode`


