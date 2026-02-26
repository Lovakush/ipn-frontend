# CampaignCouponsListPaginatedAction.php

**Path**: `src\TalonOne\Controller\CampaignCouponsListPaginatedAction.php`

## Summary
# Summary

This Symfony controller action handles paginated retrieval of campaign coupons from the TalonOne API, accepting POST requests with pagination parameters (pageSize, skip, fetchAll) and validating them before processing. It extracts the campaignId from the route, parses JSON request body for pagination options, and enforces constraints (pageSize between 1-1000) to ensure valid API requests to the TalonOne integration service.

## Classes
- `CampaignCouponsListPaginatedAction`

## Function Details

### `__invoke`

- **Parameters**: `Request $request`

