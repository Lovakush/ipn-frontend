# UpdateCoupon.php

**Path**: `src\TalonOne\Domain\UseCase\UpdateCoupon.php`

## Summary
# Summary

The `UpdateCoupon` use case executes an API request to update a coupon in the Talon One marketing platform by using the builder pattern to construct a request, sending it through the management client, and returning the updated coupon data. It handles API errors by catching exceptions and wrapping them in domain-specific exceptions for consistent error handling across the application.

## Classes
- `UpdateCoupon`

## Function Details

### `execute`

- **Parameters**: `Coupon $coupon`

