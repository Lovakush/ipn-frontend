# ClearCacheAction.php

**Path**: `src\TalonOne\Controller\ClearCacheAction.php`

## Summary
# Summary

This Symfony controller provides a REST API endpoint (`DELETE /api/v2/admin/talon-one/cache`) that clears all cached data related to Talon One campaigns by invalidating the 'talon_one' cache tag in the filesystem adapter. The `ClearCacheAction` class serves as a cache invalidation mechanism for campaign-related data, ensuring that stale campaign information (from `GetCampaign` and `ListCampaign` use cases) is refreshed on demand.

## Classes
- `ClearCacheAction`

## Function Details

### `__invoke`

- **Parameters**: `Request $request`

### `clearAllCache`


