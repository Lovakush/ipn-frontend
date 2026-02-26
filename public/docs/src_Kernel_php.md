# Kernel.php

**Path**: `src\Kernel.php`

## Summary
# Kernel.php Summary

This file defines the application's **Symfony Kernel**, which bootstraps and configures the Sylius e-commerce framework. It manages bundle registration, dependency injection compilation (including custom passes for cart rules, payment gateways, and shipping methods), and sets up cache/log directories while configuring Doctrine ORM to use a custom SQL walker for consistent ORDER BY identifier behavior in queries.

## Classes
- `Kernel`

## Function Details

### `boot`


### `getCacheDir`


### `getLogDir`


### `registerBundles`


### `configureContainer`

- **Parameters**: `ContainerBuilder $container, LoaderInterface $loader`

### `getContainerBaseClass`


### `isTestEnvironment`


### `build`

- **Parameters**: `ContainerBuilder $container`

### `setDefaultOutputWalker`

- **Parameters**: `string $outputWalkerClass`

