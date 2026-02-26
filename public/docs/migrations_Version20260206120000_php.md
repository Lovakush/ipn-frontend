# Version20260206120000.php

**Path**: `migrations\Version20260206120000.php`

## Summary
# Summary

This Doctrine migration creates a new `upd_origin_customer_lead` table to store customer lead origin information (with name, start/end dates, and timestamps) and establishes a nullable foreign key relationship from the `sylius_customer` table to track which lead origin each customer came from. The migration includes safety checks to ensure idempotent execution by verifying the table and column don't already exist before creation.

## Classes
- `Version20260206120000`

## Function Details

### `getDescription`


### `up`

- **Parameters**: `Schema $schema`

### `down`

- **Parameters**: `Schema $schema`

