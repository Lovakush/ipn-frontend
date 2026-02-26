# Version20251212145130.php

**Path**: `migrations\Version20251212145130.php`

## Summary
# Summary

This Doctrine database migration adds a nullable `checkDate` DATETIME column to the `sylius_order_talon_one_coupon` table, likely to track when coupon validity was last verified in a Sylius e-commerce system integrated with Talon.One promotion engine. The migration includes a reversible `down()` method to drop the column if the migration needs to be rolled back.

## Classes
- `Version20251212145130`

## Function Details

### `getDescription`


### `up`

- **Parameters**: `Schema $schema`

### `down`

- **Parameters**: `Schema $schema`

