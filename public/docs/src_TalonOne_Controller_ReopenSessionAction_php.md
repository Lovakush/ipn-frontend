# ReopenSessionAction.php

**Path**: `src\TalonOne\Controller\ReopenSessionAction.php`

## Summary
# Summary

This Symfony controller action handles reopening customer sessions for subscription orders in a Talon One integration. It retrieves an order by its token value from the request, validates it's a `SubscriptionOrder`, and executes the `ReopenCustomerSession` use case to restore the session state, returning the result as a JSON response or throwing a `BadRequestException` if the order type is invalid.

## Classes
- `ReopenSessionAction`

## Function Details

### `__invoke`

- **Parameters**: `Request $request`

