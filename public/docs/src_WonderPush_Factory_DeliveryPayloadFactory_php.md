# DeliveryPayloadFactory.php

**Path**: `src\WonderPush\Factory\DeliveryPayloadFactory.php`

## Summary
# Summary

The `DeliveryPayloadFactory` class transforms email parameters into a `DeliveryPayloadDto` object for push notification delivery. It retrieves the customer's associated animal from the repository, constructs a `NotificationParamsDto` with subscription and order details (falling back to translated default text if no animal exists), and returns a formatted delivery payload ready for WonderPush integration.

## Classes
- `DeliveryPayloadFactory`

## Function Details

### `fromEmailParamsArray`

- **Parameters**: `string $customerEmail, string $campaignId, array $params`

