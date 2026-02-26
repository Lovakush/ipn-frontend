# UpdateCouponAction.php

**Path**: `src\TalonOne\Controller\UpdateCouponAction.php`

## Summary
# Summary

This Symfony controller handles PUT requests to update a specific coupon within a TalonOne campaign via REST API (`/api/v2/admin/talon_one/campaigns/{campaignId}/coupons/{couponId}`). It deserializes the incoming JSON request into a Coupon DTO, injects the campaign and coupon IDs, executes the update use case, and returns the result as a JSON response with HTTP 200 status.

## Classes
- `UpdateCouponAction`

## Function Details

### `__invoke`

- **Parameters**: `int $campaignId, int $couponId, Request $request`

