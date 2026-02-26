# BulkCouponsRequest.php

**Path**: `src\TalonOne\Domain\DTO\BulkCouponsRequest.php`

## Summary
# Summary

This is a Data Transfer Object (DTO) that encapsulates parameters for bulk coupon creation via the Talon.One API, providing a type-safe way to construct and serialize coupon generation requests. The `toArray()` method converts the DTO into an API-compatible array format, conditionally including optional fields like expiry dates, discount limits, and custom attributes while formatting dates in ISO 8601 format.

## Classes
- `BulkCouponsRequest`

## Function Details

### `toArray`


