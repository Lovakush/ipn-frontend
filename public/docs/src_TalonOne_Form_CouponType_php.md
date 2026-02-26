# CouponType.php

**Path**: `src\TalonOne\Form\CouponType.php`

## Summary
# Summary

This Symfony form type defines the structure for creating and configuring coupons in a Talon One integration, enabling users to specify coupon generation parameters such as quantity, naming patterns (prefix/suffix/pattern), usage limits, validity dates, and custom attributes. The form disables CSRF protection and uses an empty block prefix to allow flexible rendering of its fields.

## Classes
- `CouponType`

## Function Details

### `buildForm`

- **Parameters**: `FormBuilderInterface $builder, array $options`

### `configureOptions`

- **Parameters**: `OptionsResolver $resolver`

### `getBlockPrefix`


