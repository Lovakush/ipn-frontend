# Version20251209094309.php

**Path**: `migrations\Version20251209094309.php`

## Summary
# Summary

This Doctrine database migration adds a `hight_priority` boolean column (TINYINT(1)) to the `sylius_order` table with a default value of 0, allowing orders in the Sylius e-commerce platform to be flagged with priority status. The migration includes both forward (`up`) and rollback (`down`) methods to support version control of database schema changes.

## Classes
- `Version20251209094309`

## Function Details

### `getDescription`


### `up`

- **Parameters**: `Schema $schema`

### `down`

- **Parameters**: `Schema $schema`

