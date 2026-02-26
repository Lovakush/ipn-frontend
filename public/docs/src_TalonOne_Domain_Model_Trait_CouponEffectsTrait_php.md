# CouponEffectsTrait.php

**Path**: `src\TalonOne\Domain\Model\Trait\CouponEffectsTrait.php`

## Summary
# Summary

This trait builds human-readable French descriptions of coupon effects by extracting and formatting discount attributes into a structured array. The `buildCouponEffects` method conditionally generates coupon benefit descriptions (order discounts, free items, shipping/payment fee reductions, product discounts), while `humanizeTypeValue` converts discount type codes ('percent', 'amount') into their corresponding symbols (%, €) for display purposes.

## Function Details

### `buildCouponEffects`

- **Parameters**: `?array $attributes`

### `humanizeTypeValue`

- **Parameters**: `string $type`

