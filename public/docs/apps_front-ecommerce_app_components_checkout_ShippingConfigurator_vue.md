# ShippingConfigurator.vue

**Path**: `apps\front-ecommerce\app\components\checkout\ShippingConfigurator.vue`

## Summary
# ShippingConfigurator.vue Summary

This Vue 3 component manages the shipping method selection and configuration during checkout, handling both home delivery and pickup point options. It integrates with Google Maps to display pickup locations, manages shipping address selection/persistence, and coordinates between shipping methods, pickup points, and delivery type preferences through v-model bindings for reactive state management.

## Function Details

### `markerInfoContentBuilder`

- **Parameters**: `marker: IPickupPoint`

### `normalizeCarrierCode`

- **Parameters**: `code: string`

### `getPickupPointIcon`

- **Parameters**: `point: IPickupPoint`

### `activePickupShippingType`


### `getMinPrice`

- **Parameters**: `marker: IMarker`

