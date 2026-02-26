# useCheckout.ts

**Path**: `apps\front-ecommerce\app\composables\useCheckout.ts`

## Interfaces
- `IComposablePaymentMethod`

## Type Aliases
- `WindowWithGTagData`

## Function Details

### `useCheckout`

- **Parameters**: `orderRef: string`

### `getAvailablePaymentMethods`


### `initialize`


### `loadCart`


### `saveAddress`

- **Parameters**: `address: ICustomerAddress`

### `submitShippingAddress`

- **Parameters**: `loading = true`

### `refreshAvailableShippingMethod`

- **Parameters**: `loading = true`

### `submitShippingMethod`


### `patchShipmentWithMethod`

- **Parameters**: `jwtToken?: string`

### `submitPaymentMethod`


### `submitPayment`

- **Parameters**: `method: IPaymentMethod, ...args: any[]`

### `submitFreePayment`

- **Parameters**: `freePaymentMethod: IPaymentMethod`

### `completeCheckout`


### `rollbackToAddress`


### `redirectToConfirmation`


### `detectExistingPaymentRedirect`


### `shippingStep`

- **Parameters**: `computed((`

### `stepOpened`

- **Parameters**: `computed((`

### `maySubmitShipping`

- **Parameters**: `computed((`

### `paymentFormConfiguration`

- **Parameters**: `computed((`

### `paymentFeesAdjustment`

- **Parameters**: `computed((`

### `hasPaymentFees`

- **Parameters**: `computed((`

### `isCartValid`

- **Parameters**: `computed((`

