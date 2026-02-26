# SubscriptionProductOfStockEmailNotification.php

**Path**: `src\CQRS\Command\Email\SubscriptionProductOfStockEmailNotification.php`

## Summary
# Summary

This class is a CQRS command that encapsulates a request to send an email notification when a subscribed product becomes available in stock. It serves as a message object that carries the subscription order ID through the command bus to trigger the corresponding email notification handler.

## Classes
- `SubscriptionProductOfStockEmailNotification`

## Function Details

### `__construct`

- **Parameters**: `public int $subscriptionOrderId`

