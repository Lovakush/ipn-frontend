# CheckCouponForCart.xml

**Path**: `config\serialization\Commands\Cart\CheckCouponForCart.xml`

## Summary
# Summary

This Symfony serializer configuration file defines how the `CheckCouponForCart` command object should be serialized/deserialized for cart coupon application operations. It specifies that the `couponCode` and `checkDate` attributes are serializable in both shop and admin contexts under the `apply_coupon` serialization groups, enabling controlled data mapping between API requests and the command object.

