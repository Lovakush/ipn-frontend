# Kernel.php

**Path**: `src\Kernel.php`

## Summary
/*' . self::CONFIG_EXTS, 'glob');
$loader-&gt;load($confDir . '/{services}' . self::CONFIG_EXTS, 'glob');
$loader-&gt;load($confDir . '/{services}_' . $this-&gt;environment . self::CONFIG_EXTS, 'glob');
$loader-&gt;load($confDir . '/{services}/*

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

