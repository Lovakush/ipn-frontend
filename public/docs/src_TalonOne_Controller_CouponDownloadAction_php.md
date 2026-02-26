# CouponDownloadAction.php

**Path**: `src\TalonOne\Controller\CouponDownloadAction.php`

## Summary
# Summary

This Symfony controller action handles secure downloads of CSV export files for the Talon One admin API. It validates incoming requests by restricting file types to `.csv` only and preventing directory traversal attacks via `basename()`, then returns the requested file as a binary attachment from the `var/export` directory.

## Classes
- `CouponDownloadAction`

## Function Details

### `__invoke`

- **Parameters**: `string $filename`

