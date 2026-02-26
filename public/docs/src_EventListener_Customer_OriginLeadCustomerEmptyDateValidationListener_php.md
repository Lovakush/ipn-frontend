# OriginLeadCustomerEmptyDateValidationListener.php

**Path**: `src\EventListener\Customer\OriginLeadCustomerEmptyDateValidationListener.php`

## Summary
# Summary

This event listener validates that date fields (`startDate` and potentially `endDate`) are not submitted as empty strings in API requests for the `OriginLeadCustomer` entity. It intercepts POST, PATCH, and PUT requests at the pre-read stage, decodes the JSON payload, and throws a `ValidationException` with constraint violations if empty date strings are detected, ensuring data integrity before entity processing.

## Classes
- `OriginLeadCustomerEmptyDateValidationListener`

## Function Details

### `getSubscribedEvents`


### `validateEmptyDates`

- **Parameters**: `RequestEvent $event`

