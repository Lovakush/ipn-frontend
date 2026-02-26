# CartUpsell.vue

**Path**: `apps\front-ecommerce\app\components\cart\CartUpsell.vue`

## Summary
# CartUpsell.vue Summary

This Vue component manages the addition of upsell and cross-sell products to the shopping cart. It handles product variant selection, cart store integration, and GTM (Google Tag Manager) tracking events, with type-guarding logic to differentiate between Strapi-sourced upsells and Pixie ad-based cross-sell promotions.

## Function Details

### `addToCart`


### `upsellAdded`

- **Parameters**: `orderResponse.value?.items?.filter((item`

