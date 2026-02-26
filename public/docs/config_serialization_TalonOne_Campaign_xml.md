# Campaign.xml

**Path**: `config\serialization\TalonOne\Campaign.xml`

## Summary
# Summary

This Symfony serializer configuration file defines the serialization rules for the `Campaign` DTO class, specifying which attributes can be serialized/deserialized and under which access groups (read/write permissions). It controls API data exposure for campaign management, restricting fields like `isExpired` to read-only operations while allowing most other campaign properties (id, name, description, timing, state, tags, etc.) to be both read and written by admin users.

