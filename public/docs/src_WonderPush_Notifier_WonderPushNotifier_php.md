# WonderPushNotifier.php

**Path**: `src\WonderPush\Notifier\WonderPushNotifier.php`

## Summary
# Summary

The `WonderPushNotifier` class is a wrapper service that sends push notifications through the WonderPush platform by delegating to a `WonderPushClient`. It handles error logging and exception propagation, capturing detailed context (error message, payload, and exception metadata) when push delivery fails, then re-throws the exception for upstream handling.

## Classes
- `WonderPushNotifier`

## Function Details

### `notify`

- **Parameters**: `DeliveryPayloadDto $payload`

