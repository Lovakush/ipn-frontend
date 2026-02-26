# MiniCart.vue

**Path**: `apps\front-ecommerce\app\components\cart\MiniCart.vue`

## Summary
# MiniCart.vue Summary

This Vue 3 component renders a dropdown mini-cart dialog that displays the user's shopping cart items with the ability to remove items. It integrates with Pinia's cart store, handles item removal with tracking events, and manages the dialog's visibility state through show/hide callbacks and mouse events, while supporting multi-language localization for dynamic positioning.

## Function Details

### `removeItemFromCart`

- **Parameters**: `item: ICartItem`

### `tracking`

- **Parameters**: `{ itemRemoved }: { itemRemoved?: ICartItem }`

