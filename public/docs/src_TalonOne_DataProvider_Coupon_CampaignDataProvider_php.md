# CampaignDataProvider.php

**Path**: `src\TalonOne\DataProvider\Coupon\CampaignDataProvider.php`

## Summary
# Summary

The `CampaignDataProvider` class retrieves and transforms campaign data from the TalonOne API for a given application. It executes a `ListCampaign` use case, validates the response, and returns a keyed array of campaigns indexed by their IDs, with comprehensive error handling and logging for API failures or malformed data.

## Classes
- `CampaignDataProvider`

## Function Details

### `getCampaignsData`

- **Parameters**: `string $applicationId`

