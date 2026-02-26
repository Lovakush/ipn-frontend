# CouponsFinderPaginatedAction.php

**Path**: `src\TalonOne\Controller\CouponsFinderPaginatedAction.php`

## Summary
# Summary

This Symfony controller action handles paginated coupon searches via a POST API endpoint (`/api/v2/admin/talon-one/coupons_finder/paginated`). It validates that incoming requests contain at least one search criterion (value, batchId, createdAfter, or createdBefore), then deserializes the JSON payload into a `CouponsFinderRequest` DTO and passes it to the `CouponsFinderPaginator` service to retrieve filtered, paginated coupon results from the TalonOne platform.

## Classes
- `CouponsFinderPaginatedAction`

## Function Details

### `__invoke`

- **Parameters**: `Request $request`

