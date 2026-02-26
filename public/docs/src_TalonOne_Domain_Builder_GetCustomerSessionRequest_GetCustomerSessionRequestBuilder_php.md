# GetCustomerSessionRequestBuilder.php

**Path**: `src\TalonOne\Domain\Builder\GetCustomerSessionRequest\GetCustomerSessionRequestBuilder.php`

## Summary
# Summary

This builder class constructs a `GetCustomerSessionRequest` object for retrieving customer session data from the Talon.One integration API. It takes an `Order` entity as input, generates a session ID using an ID factory, and provides methods to build the request payload and query parameters (though these are currently unimplemented). The class follows the builder pattern to encapsulate the request construction logic for querying customer sessions in the TalonOne integration domain.

## Classes
- `GetCustomerSessionRequestBuilder`

## Function Details

### `__construct`

- **Parameters**: `private readonly Order $order`

### `reset`


### `produceRequestPayload`


### `produceRequestQueryParams`


### `getRequest`


