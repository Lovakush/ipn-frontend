# CampaignCouponsListAction.php

**Path**: `src\TalonOne\Controller\CampaignCouponsListAction.php`

## Summary
# Summary

This Symfony controller action handles POST requests to list coupons for a specific TalonOne campaign, accepting pagination parameters (pageSize and skip) from the request body with validation (pageSize: 1-1000, skip: ≥0). It constructs a `CampaignCouponsListRequest` DTO and delegates to the `CampaignCouponsList` use case to retrieve the filtered coupon data, returning results as a JSON response.

## Classes
- `CampaignCouponsListAction`

## Function Details

### `__invoke`

- **Parameters**: `Request $request`

