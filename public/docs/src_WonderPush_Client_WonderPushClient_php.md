# WonderPushClient.php

**Path**: `src\WonderPush\Client\WonderPushClient.php`

## Summary
# Summary

The `WonderPushClient` class is a Symfony-integrated HTTP client wrapper that sends push notifications to the WonderPush service by making authenticated POST requests to their deliveries endpoint. It handles request/response serialization, validates successful API responses, and wraps any HTTP or API errors into custom `WonderPushException` exceptions for consistent error handling across the application.

## Classes
- `WonderPushClient`

## Function Details

### `sendPush`

- **Parameters**: `array $payload`
- **Description**: @param array&lt;string, mixed&gt; $payload

@return array&lt;string, mixed&gt;*

@throws WonderPushException
/

