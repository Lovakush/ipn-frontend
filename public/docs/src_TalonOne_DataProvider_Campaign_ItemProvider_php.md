# ItemProvider.php

**Path**: `src\TalonOne\DataProvider\Campaign\ItemProvider.php`

## Summary
# Summary

This `ItemProvider` class is an API Platform state provider that fetches a single campaign from the Talon One marketing platform by ID. It executes a `GetCampaign` use case with the application ID and campaign ID, enriches the response with an `isExpired` flag, and wraps any exceptions as HTTP 400 errors for API responses.

## Classes
- `ItemProvider`

## Function Details

### `provide`

- **Parameters**: `Operation $operation, array $uriVariables = [], array $context = []`

