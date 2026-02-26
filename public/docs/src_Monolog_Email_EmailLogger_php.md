# EmailLogger.php

**Path**: `src\Monolog\Email\EmailLogger.php`

## Summary
# Summary

The `EmailLogger` class is a specialized wrapper around PSR-3's LoggerInterface that formats and logs email-related events with a consistent `[ EMAIL ... ]` prefix. It provides a convenient interface for recording email operations (such as "SENT") at configurable log levels, configured to use the 'email' Monolog channel via the `WithMonologChannel` attribute.

## Classes
- `EmailLogger`

