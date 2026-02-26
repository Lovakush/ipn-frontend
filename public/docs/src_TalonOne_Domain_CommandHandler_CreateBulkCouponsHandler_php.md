# CreateBulkCouponsHandler.php

**Path**: `src\TalonOne\Domain\CommandHandler\CreateBulkCouponsHandler.php`

## Summary
# Summary

This is a Symfony message handler that processes `CreateBulkCouponsCommand` messages by delegating to a `CreateBulkCoupons` use case and returning an array of `Coupon` objects. It wraps any exceptions that occur during bulk coupon creation into a domain-specific `TalonOneApiException` for consistent error handling within the TalonOne integration module.

## Classes
- `CreateBulkCouponsHandler`

## Function Details

### `__invoke`

- **Parameters**: `CreateBulkCouponsCommand $command`
- **Description**: @param CreateBulkCouponsCommand $command
@return Coupon[]
@throws TalonOneApiException
/

