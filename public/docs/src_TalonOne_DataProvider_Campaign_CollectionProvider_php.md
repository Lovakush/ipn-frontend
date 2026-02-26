# CollectionProvider.php

**Path**: `src\TalonOne\DataProvider\Campaign\CollectionProvider.php`

## Summary
# Summary

This is an API Platform state provider that handles HTTP requests for listing Talon One marketing campaigns. It extracts filtering parameters (tag, status, name, pagination) from the request context, delegates to a `ListCampaign` use case to fetch campaigns from the Talon One API, and returns the results while translating any exceptions into user-friendly error responses.

## Classes
- `CollectionProvider`

## Function Details

### `provide`

- **Parameters**: `Operation $operation, array $uriVariables = [], array $context = []`

