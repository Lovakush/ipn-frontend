# CouponExportAction.php

**Path**: `src\TalonOne\Controller\CouponExportAction.php`

## Summary
# Summary

This Symfony controller action handles POST requests to export coupons from the Talon One loyalty platform by accepting search criteria (value, batchId, createdAfter, createdBefore) and initiating an export process via the `CouponExportService`. It validates that at least one search criterion is provided, constructs a `CouponsFinderRequest` DTO with the filtered parameters, and returns a JSON response containing the download URL for the exported coupon data.

## Classes
- `CouponExportAction`

## Function Details

### `__invoke`

- **Parameters**: `Request $request`

### `generateDownloadUrl`

- **Parameters**: `string $filename`

