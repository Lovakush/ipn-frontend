# ContactForm.vue

**Path**: `apps\front-ecommerce\app\components\content\ContactForm.vue`

## Summary
# ContactForm.vue Summary

This Vue component manages a contact form submission workflow for an e-commerce application. It validates submissions using reCAPTCHA, formats form data (including arrays) into FormData, sends the request to a backend contact service, and tracks the submission outcome (success/error) for analytics purposes.

## Function Details

### `handleSubmit`

- **Parameters**: `form: { [key: string]: any }`

