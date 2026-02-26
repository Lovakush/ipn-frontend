# SubscriptionShipmentInvalidEmailNotification.php

**Path**: `src\CQRS\Command\Email\SubscriptionShipmentInvalidEmailNotification.php`

## Summary
# Summary

This file defines a CQRS command class that encapsulates a request to notify about an invalid email address associated with a subscription shipment order. The command carries only the subscription order ID as a parameter, which will be used by a corresponding command handler to trigger email notification logic for the affected subscription order.

## Classes
- `SubscriptionShipmentInvalidEmailNotification`

## Function Details

### `__construct`

- **Parameters**: `public int $subscriptionOrderId`

