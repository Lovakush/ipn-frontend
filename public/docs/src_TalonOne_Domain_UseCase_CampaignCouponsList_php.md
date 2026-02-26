# CampaignCouponsList.php

**Path**: `src\TalonOne\Domain\UseCase\CampaignCouponsList.php`

## Summary
# Summary

The `CampaignCouponsList` use case executes a request to retrieve coupons for a specific campaign from the TalonOne Management API, using the Builder pattern to construct the request. It handles the API response by either returning formatted coupon data with a count, returning an empty result set if no coupons exist, or throwing appropriate exceptions for API errors and technical failures.

## Classes
- `CampaignCouponsList`

## Function Details

### `execute`

- **Parameters**: `string $applicationId, string $campaignId, CampaignCouponsListRequest $payload`

