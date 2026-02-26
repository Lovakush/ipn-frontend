# Version20260210145311.php

**Path**: `migrations\Version20260210145311.php`

## Summary
# Summary

This is a Doctrine database migration that adds an `is_default` boolean column (TINYINT default 0) to the `upd_origin_customer_lead` table, with safety checks to verify the table and column existence before executing the alteration. The migration is reversible—the `up()` method adds the column while the `down()` method removes it, ensuring idempotent operations that won't fail if the schema state is uncertain.

## Classes
- `Version20260210145311`

## Function Details

### `getDescription`


### `up`

- **Parameters**: `Schema $schema`

### `down`

- **Parameters**: `Schema $schema`

