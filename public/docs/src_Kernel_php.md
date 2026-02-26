# Kernel.php

**Path**: `src\Kernel.php`

## Summary
# Summary

This is the main **Symfony application kernel for a Sylius-based e-commerce system** that bootstraps the application, configures dependency injection, and registers bundles. It extends Symfony's BaseKernel using MicroKernelTrait and registers custom compiler passes for domain-specific features like cart rule checkers, payment gateways, shipping methods, and Doctrine ORM query walkers, while setting up cache/log directories and configuring service loading from environment-specific configuration files.

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

