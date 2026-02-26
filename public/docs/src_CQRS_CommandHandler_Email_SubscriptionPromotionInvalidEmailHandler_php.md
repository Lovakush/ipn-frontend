# SubscriptionPromotionInvalidEmailHandler.php

**Path**: `src\CQRS\CommandHandler\Email\SubscriptionPromotionInvalidEmailHandler.php`

## Summary
# Summary

This command handler processes `SubscriptionPromotionInvalidEmailNotification` messages to send transactional emails notifying customers about invalid subscription promotions. It retrieves the subscription order via query bus, validates that associated subscription and customer entities exist, then dispatches an email with customer details and subscription parameters using the transactional email service.

## Classes
- `SubscriptionPromotionInvalidEmailHandler`

## Function Details

### `__invoke`

- **Parameters**: `SubscriptionPromotionInvalidEmailNotification $message`

