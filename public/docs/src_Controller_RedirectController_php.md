# RedirectController.php

**Path**: `src\Controller\RedirectController.php`

## Summary
# Summary

The `RedirectController` is a Symfony controller that handles HTTP redirects to configurable URLs (site or backoffice) based on an environment variable parameter. It supports both temporary (302) and permanent (301) redirects, with the target URLs injected from environment configuration at construction time.

## Classes
- `RedirectController`

## Function Details

### `__invoke`

- **Parameters**: `string $envVar, bool $permanent = false`

