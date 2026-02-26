# WebMethodCharacterNormalizerTrait.php

**Path**: `src\Api\Serializer\Normalizer\WebMethodCharacterNormalizerTrait.php`

## Summary
# Summary

This trait provides character normalization functionality for web API serialization, specifically designed to clean and standardize personal/address data fields (names, company, street, city, postcode). It normalizes typographic apostrophes, removes diacritical marks/accents, and strips invalid characters—retaining only letters, numbers, spaces, hyphens, and standard apostrophes to ensure data consistency across API inputs.

## Function Details

### `characterNormalization`

- **Parameters**: `array $data`

### `removeAccents`

- **Parameters**: `string $value`

