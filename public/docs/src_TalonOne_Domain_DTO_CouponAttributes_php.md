# CouponAttributes.php

**Path**: `src\TalonOne\Domain\DTO\CouponAttributes.php`

## Summary
# CouponAttributes Analysis

The `CouponAttributes` class is a Data Transfer Object (DTO) that encapsulates coupon promotion attributes for the Talon One loyalty/promotion platform, storing configuration details for product discounts, order discounts, shipping/payment fees, free items, and associated analytics metadata. The `toArray()` method serializes these attributes into an array format, with conditional logic to differentiate between master campaigns and standard campaigns for API transmission or data storage.

## Classes
- `CouponAttributes`

## Function Details

### `toArray`

- **Parameters**: `bool $isMasterCampaign = false`

