# CreateCouponSchemaAction.php

**Path**: `src\TalonOne\Controller\Schemas\CreateCouponSchemaAction.php`

## Summary
# Summary

This Symfony controller action generates and returns a JSON schema for coupon creation forms via an API endpoint. It uses the `SchemaSerializer` to convert a `CouponType` form definition into a serialized schema structure, which is then returned as a JSON response at `/api/v2/schemas/create-coupon`. This allows frontend applications to dynamically understand the form structure and validation requirements for creating coupons without hardcoding form definitions.

## Classes
- `CreateCouponSchemaAction`

## Function Details

### `__construct`

- **Parameters**: `private readonly SchemaSerializer $serializer`

### `__invoke`


