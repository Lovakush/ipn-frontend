# ListCouponAttribute.php

**Path**: `src\TalonOne\Domain\UseCase\ListCouponAttribute.php`

## Summary
# ListCouponAttribute Use Case Summary

This use case class retrieves a list of coupon attributes from the Talon.One management API by orchestrating a request-building process and executing it through the management client. It implements error handling by catching technical exceptions and re-throwing them as domain-specific `TalonOneApiException` instances, ensuring consistent exception handling across the application layer.

## Classes
- `ListCouponAttribute`

## Function Details

### `execute`


