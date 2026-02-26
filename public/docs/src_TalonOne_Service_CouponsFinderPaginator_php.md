# CouponsFinderPaginator.php

**Path**: `src\TalonOne\Service\CouponsFinderPaginator.php`

## Summary
# CouponsFinderPaginator Summary

This service implements a pagination wrapper around the `CouponsFinder` use case to retrieve all coupons matching specified criteria (value, batchId, campaign, creation date filters) from the Talon.One platform. It automatically handles pagination by iterating through pages of results using configurable page sizes and skip offsets until all matching coupons are fetched and aggregated into a single result set.

## Classes
- `CouponsFinderPaginator`

## Function Details

### `fetchAllCoupons`

- **Parameters**: `string $applicationId, CouponsFinderRequest $payload`
- **Description**: Fetch all coupons using pagination

@param string $applicationId
@param CouponsFinderRequest $payload
@return array All coupons found
/

### `fetchPaginatedCoupons`

- **Parameters**: `string $applicationId, CouponsFinderRequest $payload`
- **Description**: Fetch coupons with custom pagination

@param string $applicationId
@param CouponsFinderRequest $payload
@return array Paginated coupons
/

