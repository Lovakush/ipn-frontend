# Newsletter.vue

**Path**: `apps\front-ecommerce\app\components\content\Newsletter.vue`

## Summary
# Newsletter.vue Summary

This Vue 3 component manages newsletter subscription functionality for an e-commerce frontend, providing a form interface that collects user email data and submits it to a contact management system. The `handleSubmit` function orchestrates the subscription flow by obtaining a reCAPTCHA token, enriching the form data with metadata (country, origin, source), submitting it via the Cloud Contact API, and tracking the subscription event for analytics purposes.

## Function Details

### `handleSubmit`

- **Parameters**: `form: TNewsletterRequest, source: string`

