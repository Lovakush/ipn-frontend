# DeleteCouponAction.php

**Path**: `src\TalonOne\Controller\DeleteCouponAction.php`

## Summary
# Summary

This Symfony controller action handles HTTP requests to delete a coupon by accepting a campaign ID and coupon ID, constructing a Coupon DTO with these identifiers, and delegating the deletion logic to the `DeleteCoupon` use case. It includes error handling that logs any exceptions that occur during the deletion process without propagating them to the caller.

## Classes
- `DeleteCouponAction`

## Function Details

### `__invoke`

- **Parameters**: `int $campaignId, int $couponId`

