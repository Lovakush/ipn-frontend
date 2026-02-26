# CollectionProvider.php

**Path**: `src\TalonOne\DataProvider\Coupon\CollectionProvider.php`

## Summary
# Summary

This `CollectionProvider` is an API Platform state provider that retrieves and enriches coupon data for a specific customer by fetching their coupons from the Talon One loyalty platform and augmenting each coupon with its associated campaign name and description. It acts as a data aggregator between the customer repository, the Talon One API integration, and campaign metadata to provide a complete coupon collection response via the API endpoint.

## Classes
- `CollectionProvider`

## Function Details

### `provide`

- **Parameters**: `Operation $operation, array $uriVariables = [], array $context = []`

