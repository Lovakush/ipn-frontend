# OriginLeadCustomer.php

**Path**: `src\Entity\Customer\OriginLeadCustomer.php`

## Summary
# OriginLeadCustomer Entity Summary

The `OriginLeadCustomer` class is a Doctrine ORM entity that represents a lead origin/source type for customers in a Sylius-based application. It manages metadata about customer lead origins including a unique name, optional start/end date ranges (with validation ensuring start ≤ end), and a default flag, while exposing this data via GraphQL API endpoints with sortable fields and automatic timestamp tracking.

## Classes
- `OriginLeadCustomer`

## Function Details

### `getId`


### `getName`


### `setName`

- **Parameters**: `?string $name`

### `getStartDate`


### `setStartDate`

- **Parameters**: `?\DateTimeInterface $startDate`

### `getEndDate`


### `setEndDate`

- **Parameters**: `?\DateTimeInterface $endDate`

### `isDefault`


### `getIsDefault`


### `setIsDefault`

- **Parameters**: `bool $isDefault`

