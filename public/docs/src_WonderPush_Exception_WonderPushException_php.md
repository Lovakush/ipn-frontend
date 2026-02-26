# WonderPushException.php

**Path**: `src\WonderPush\Exception\WonderPushException.php`

## Summary
# Summary

`WonderPushException` is a custom exception class for the WonderPush integration that extends `RuntimeException` to provide contextual error information. It captures both an error message and an optional context array (containing related data like request details or variable states) along with exception chaining support, enabling better error logging and debugging within the WonderPush notification service.

## Classes
- `WonderPushException`

## Function Details

### `__construct`

- **Parameters**: `string $message, array $context = [], ?\Throwable $previous = null`

### `getContext`


