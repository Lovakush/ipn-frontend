# CouponsFinder.php

**Path**: `src\TalonOne\Domain\UseCase\CouponsFinder.php`

## Summary
# Summary

The `CouponsFinder` class is a use case handler that searches for coupons through the Talon One Management API and enriches the results with associated campaign data. It constructs API requests using the builder pattern, executes them via the management client, handles errors appropriately, and optimizes performance by caching campaign data to avoid redundant API calls when enriching multiple coupons.

## Classes
- `CouponsFinder`

## Function Details

### `execute`

- **Parameters**: `string $applicationId, CouponsFinderRequest $payload`

### `enrichCouponsWithCampaignData`

- **Parameters**: `string $applicationId, array $coupons`
- **Description**: Enrich coupons with campaign data, caching campaigns to avoid duplicate API calls
/

