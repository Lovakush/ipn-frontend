# ItemProvider.php

**Path**: `src\TalonOne\DataProvider\Coupon\ItemProvider.php`

## Summary
# Summary

This API Platform state provider retrieves a single coupon by its value from the Talon One management API and enriches it with associated campaign metadata (name and description). It implements the `ProviderInterface` to handle HTTP requests for individual coupon resources, using a builder pattern to construct the API request and gracefully returning null on errors or when the coupon is not found.

## Classes
- `ItemProvider`

## Function Details

### `provide`

- **Parameters**: `Operation $operation, array $uriVariables = [], array $context = []`

