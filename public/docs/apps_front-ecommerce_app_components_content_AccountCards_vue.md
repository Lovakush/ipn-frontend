# AccountCards.vue

**Path**: `apps\front-ecommerce\app\components\content\AccountCards.vue`

## Summary
# Summary

This Vue 3 component manages the display of account cards on an e-commerce dashboard, aggregating customer order and subscription data to show their current status. It retrieves and processes orders and subscriptions through composables, filtering for the most recent valid items (non-expired subscriptions, pending/completed orders) and organizing them for UI rendering with helper functions like `isNotValidPeriod`, `getClosestSubscription`, and `getOrderCardsData`.

## Function Details

### `isNotValidPeriod`

- **Parameters**: `order: IOrder | null = null`

### `getClosestSubscription`

- **Parameters**: `acc: ISubscription, sub: ISubscription`

### `getOrderCardsData`


