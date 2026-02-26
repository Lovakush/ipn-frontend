# ReopenCustomerSession.php

**Path**: `src\TalonOne\Domain\UseCase\ReopenCustomerSession.php`

## Summary
# Summary

This use case class reopens a closed Talon.One customer session associated with a given Order by building a request through the RequestDirector pattern, executing it via the IntegrationClient, and returning the API response containing promotional effects. It handles API errors by converting technical exceptions into domain-specific exceptions (TalonOneApiErrorException or TalonOneApiException).

## Classes
- `ReopenCustomerSession`

## Function Details

### `execute`

- **Parameters**: `Order $order`
- **Description**: Réouvre une session Talon fermée.

@param Order $order La commande associée à la session à réouvrir

@return array La réponse de l'API contenant les effets (effects)

@throws TalonOneApiException
/

