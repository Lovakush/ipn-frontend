# SubscriptionPromotionInvalidEmailNotification.php

**Path**: `src\CQRS\Command\Email\SubscriptionPromotionInvalidEmailNotification.php`

## Summary
# Summary

This class is a CQRS command that encapsulates a notification event when a subscription promotion fails due to an invalid email address. It serves as a message object that carries the `subscriptionOrderId` through the command bus to trigger email notification handling for the failed promotion scenario.

## Classes
- `SubscriptionPromotionInvalidEmailNotification`

## Function Details

### `__construct`

- **Parameters**: `public int $subscriptionOrderId`

