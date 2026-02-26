# OriginLeadCustomerNormalizer.php

**Path**: `src\Api\Serializer\Normalizer\Customer\OriginLeadCustomerNormalizer.php`

## Summary
# Summary

This normalizer serializes `OriginLeadCustomer` entities for API responses within specific Sylius admin serialization groups (customer show/create/update operations). It converts customer objects into normalized data structures using API Platform's IRI converter and resource metadata factory, while preventing recursive normalization through a guard flag.

## Classes
- `OriginLeadCustomerNormalizer`

## Function Details

### `normalize`

- **Parameters**: `$object, ?string $format = null, array $context = []`
- **Description**: @throws \Symfony\Component\Serializer\Exception\ExceptionInterface
/

### `supportsNormalization`

- **Parameters**: `$data, ?string $format = null, $context = []`

