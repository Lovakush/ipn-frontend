# CreateAsyncBulkCouponsRequestBuilder.php

**Path**: `src\TalonOne\Domain\Builder\PostCreateCouponsRequest\CreateAsyncBulkCouponsRequestBuilder.php`

## Summary
# Summary

This builder class constructs async bulk coupon creation requests for the TalonOne management API by implementing the builder pattern. It takes a `CreateBulkCouponsCommand` containing coupon parameters (numberOfCoupons, usageLimit, etc.) and transforms them into a properly formatted `PostCreateAsyncCouponsRequest` with predefined coupon character sets and optional prefix/suffix patterns for the specified application and campaign.

## Classes
- `CreateAsyncBulkCouponsRequestBuilder`

## Function Details

### `reset`


### `produceRequestPayload`


### `produceRequestQueryParams`


### `getRequest`


