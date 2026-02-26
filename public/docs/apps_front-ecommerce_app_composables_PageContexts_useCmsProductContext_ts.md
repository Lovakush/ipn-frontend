# useCmsProductContext.ts

**Path**: `apps\front-ecommerce\app\composables\PageContexts\useCmsProductContext.ts`

## Summary
Valeur numérique depuis i18n schema.config.
Accepte soit une clé i18n (ex. 'schema.config.shipping.freeShippingThreshold'),
soit une valeur déjà résolue (ex. this.t('schema.config.shipping.shippingRateValue')).
Si key est une clé existante, on utilise t(key) ; sinon on parse key comme valeur brute (évite le warning intlify).

## Classes
- `CmsProductContext`

## Function Details

### `useCmsProductContext`


### `load`

- **Parameters**: `slug: string`

### `createContext`

- **Parameters**: `slug: string`

### `audiences`

- **Parameters**: `keys.map((key`

### `isDisableShopping`

- **Parameters**: `p?: IStrapiProduct`

### `variantKey`

- **Parameters**: `v: (typeof product.ProductVariants)[0]`

### `variants`

- **Parameters**: `product.ProductVariants.filter((v`

### `sorted`

- **Parameters**: `[...productMetadata.Reviews].sort((a, b`

