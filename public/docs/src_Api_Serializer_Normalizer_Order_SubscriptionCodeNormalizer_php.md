# SubscriptionCodeNormalizer.php

**Path**: `src\Api\Serializer\Normalizer\Order\SubscriptionCodeNormalizer.php`

## Summary
# Summary

This normalizer serializes `Order` objects for API responses, conditionally including the `subscriptionCode` field only when the order is a subscription order. It integrates with Symfony's serialization system and applies to specific serialization groups (shop order reads, cart displays, etc.) to control when subscription codes are exposed in the normalized output.

## Classes
- `SubscriptionCodeNormalizer`

## Function Details

### `normalize`

- **Parameters**: `$object, ?string $format = null, array $context = []`
- **Description**: @throws \Symfony\Component\Serializer\Exception\ExceptionInterface
/

### `supportsNormalization`

- **Parameters**: `$data, ?string $format = null, $context = []`

