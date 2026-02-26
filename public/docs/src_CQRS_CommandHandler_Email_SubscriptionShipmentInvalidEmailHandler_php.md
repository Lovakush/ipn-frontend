# SubscriptionShipmentInvalidEmailHandler.php

**Path**: `src\CQRS\CommandHandler\Email\SubscriptionShipmentInvalidEmailHandler.php`

## Summary
# Summary

This command handler processes `SubscriptionShipmentInvalidEmailNotification` messages to send transactional emails when a subscription shipment encounters transport errors. It retrieves the related subscription order and customer details via the query bus, then dispatches a notification email to the customer with their subscription information and the channel-specific locale.

## Classes
- `SubscriptionShipmentInvalidEmailHandler`

## Function Details

### `__invoke`

- **Parameters**: `SubscriptionShipmentInvalidEmailNotification $message`

