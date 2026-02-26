# RedirectController.php

**Path**: `src\Controller\RedirectController.php`

## Summary
# Summary

The `RedirectController` is an invokable Symfony controller that redirects HTTP requests to configured URLs based on an environment variable parameter. It supports both temporary (302) and permanent (301) redirects, routing requests to either a backoffice URL or a default site URL retrieved from environment configuration.

## Classes
- `RedirectController`

## Function Details

### `__invoke`

- **Parameters**: `string $envVar, bool $permanent = false`

