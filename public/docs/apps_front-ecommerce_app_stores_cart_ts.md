# cart.ts

**Path**: `apps\front-ecommerce\app\stores\cart.ts`

## Summary
Add product variant quantity from query
@example
```
/panier?variantId=12345678&amp;quantity=1&amp;interval=31
```
@returns

## Classes
- `CartError`

## Function Details

### `getCustomerStore`


### `loadCart`


### `getCart`

- **Parameters**: `ensureIfNotExist = true`

### `recoverCart`

- **Parameters**: `cartIri: string`

### `getFrequencies`


### `getFrequencyLabel`

- **Parameters**: `frequencyCode: string | number`

### `addCouponCode`

- **Parameters**: `couponCode: string, checkDate?: Date`

### `removeCouponCode`

- **Parameters**: `couponCode: string`

### `assignCart`

- **Parameters**: `newCart: ICart | null`

### `assignCustomer`

- **Parameters**: `customerId: string`

### `deleteCart`

- **Parameters**: `tokenValue: string`

### `clear`

- **Parameters**: `tokenValue?: string`

### `addProductVariantQuantityFromQuery`


### `useCartStore`

- **Parameters**: `defineStore('cart', (`

