# CampaignCouponsPaginator.php

**Path**: `src\TalonOne\Service\CampaignCouponsPaginator.php`

## Summary
# Summary

The `CampaignCouponsPaginator` class provides pagination utilities for retrieving coupons from Talon.One campaigns. It implements two methods: `fetchAllCoupons()` iterates through all paginated results to aggregate complete coupon datasets, while `fetchPaginatedCoupons()` handles single-page retrieval with configurable offset and limit parameters.

## Classes
- `CampaignCouponsPaginator`

## Function Details

### `fetchAllCoupons`

- **Parameters**: `string $applicationId, string $campaignId, int $pageSize = 1000`
- **Description**: Fetch all coupons from a campaign using pagination

@param string $applicationId
@param string $campaignId
@param int $pageSize Maximum items per page (max 1000)
@return array All coupons from the campaign
/

### `fetchPaginatedCoupons`

- **Parameters**: `string $applicationId, string $campaignId, int $pageSize = 1000, int $skip = 0`
- **Description**: Fetch coupons with custom pagination

@param string $applicationId
@param string $campaignId
@param int $pageSize
@param int $skip
@return array Paginated coupons
/

