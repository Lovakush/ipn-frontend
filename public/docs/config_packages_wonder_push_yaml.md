# wonder_push.yaml

**Path**: `config\packages\wonder_push.yaml`

## Summary
# WonderPush Configuration Summary

This Symfony configuration file sets up integration with WonderPush, a push notification service, by configuring an HTTP client with the management API endpoint and defining locale-specific campaign IDs for various transactional notifications (order confirmations, shipments, subscription events, etc.) across multiple regions (France, Belgium, Netherlands) in both production and staging environments. The file maps business events to their corresponding WonderPush campaign identifiers, enabling the application to send targeted push notifications in the appropriate language based on the triggered event type and user locale.

