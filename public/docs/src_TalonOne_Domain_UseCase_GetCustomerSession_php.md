# GetCustomerSession.php

**Path**: `src\TalonOne\Domain\UseCase\GetCustomerSession.php`

## Summary
# Summary

The `GetCustomerSession` class is a use case that retrieves customer session data from the TalonOne integration API for a given order. It constructs a request using the builder pattern, executes it through the integration client, and returns the customer session data while handling API errors and technical exceptions appropriately.

## Classes
- `GetCustomerSession`

## Function Details

### `execute`

- **Parameters**: `Order $order`

