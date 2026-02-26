# CreateBulkCoupons.php

**Path**: `src\TalonOne\Domain\UseCase\CreateBulkCoupons.php`

## Summary
# Summary

This use case class handles bulk coupon creation via the Talon.One Management API, with intelligent routing between synchronous and asynchronous processing based on batch size (&gt;20,000 coupons triggers async processing). It retrieves the target campaign, validates against a master campaign tag, and orchestrates the appropriate request builder to execute the coupon generation command while managing potential API errors.

## Classes
- `CreateBulkCoupons`

## Function Details

### `execute`

- **Parameters**: `CreateBulkCouponsCommand $command`
- **Description**: Crée des coupons en masse via l'API Management de Talon.One

@param CreateBulkCouponsCommand $command
@return Coupon[] Liste des coupons créés
@throws TalonOneApiException
@throws TalonOneApiErrorException
/

### `getCampaign`

- **Parameters**: `int $campaignId`

