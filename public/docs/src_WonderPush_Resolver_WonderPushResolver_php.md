# WonderPushResolver.php

**Path**: `src\WonderPush\Resolver\WonderPushResolver.php`

## Summary
# Summary

The `WonderPushResolver` class is a Symfony service that resolves WonderPush campaign IDs based on environment context (production or staging), template slug, and locale. It retrieves the appropriate campaign ID from environment-specific configuration arrays, enabling dynamic campaign identification for push notification templates across different deployment environments and languages.

## Classes
- `WonderPushResolver`

## Function Details

### `resolveCampaignId`

- **Parameters**: `string $templateSlug, string $locale`

