# GetCampaignAction.php

**Path**: `src\TalonOne\Controller\GetCampaignAction.php`

## Summary
# Summary

The `GetCampaignAction` controller retrieves a single campaign from the TalonOne API by extracting the campaign ID from the request, executing the `GetCampaign` use case, and enriching the response with an `isExpired` flag. It handles API exceptions by translating error messages and converting them to HTTP 400 Bad Request responses for client consumption.

## Classes
- `GetCampaignAction`

## Function Details

### `__construct`

- **Parameters**: `private readonly GetCampaign $getCampaign, private readonly TranslatorInterface $translator`

### `__invoke`

- **Parameters**: `Request $request`
- **Description**: @throws TalonOneApiException
/

