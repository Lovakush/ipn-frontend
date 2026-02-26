# OriginLeadCustomerDefaultListener.php

**Path**: `src\EventListener\Customer\OriginLeadCustomerDefaultListener.php`

## Summary
# Summary

This Doctrine event listener enforces a single-default constraint on `OriginLeadCustomer` entities by intercepting the `onFlush` event to ensure only one customer can have `isDefault = true` at any time. When multiple entities are being inserted or updated with `isDefault = true`, it automatically reverts all but the first one to `false`, maintaining data integrity at the ORM level.

## Classes
- `OriginLeadCustomerDefaultListener`

## Function Details

### `onFlush`

- **Parameters**: `OnFlushEventArgs $event`

### `unsetOtherDefaults`

- **Parameters**: `EntityManagerInterface $entityManager, OriginLeadCustomer $keepDefault`

