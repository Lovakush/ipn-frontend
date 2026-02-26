# MiniCartHeader.vue

**Path**: `apps\front-ecommerce\app\components\cart\MiniCartHeader.vue`

## Summary
# MiniCartHeader Component Summary

This Vue 3 component displays a conditional message in the mini-cart header informing users of the remaining amount needed to qualify for free shipping. It accepts a cart object as a prop, checks if `amountUntilFreeShipping` exists, and renders an internationalized message with the formatted currency amount, with plural handling to show different text depending on whether the threshold has been reached (amount &gt; 0 vs. amount ≤ 0).

