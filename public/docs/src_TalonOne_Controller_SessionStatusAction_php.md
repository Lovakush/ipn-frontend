# SessionStatusAction.php

**Path**: `src\TalonOne\Controller\SessionStatusAction.php`

## Summary
# Summary

This Symfony controller action retrieves and returns the current session status for a customer in the Talon One loyalty/promotion system. It accepts an order token, looks up the corresponding order in the repository, executes a use case to fetch the customer's session data, and returns it as a JSON response with HTTP 200 status.

## Classes
- `SessionStatusAction`

## Function Details

### `__invoke`

- **Parameters**: `Request $request`

