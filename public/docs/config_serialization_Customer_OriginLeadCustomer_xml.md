# OriginLeadCustomer.xml

**Path**: `config\serialization\Customer\OriginLeadCustomer.xml`

## Summary
# Summary

This Symfony serializer configuration file defines serialization rules for the `OriginLeadCustomer` entity, specifying which attributes (id, name, startDate, endDate, isDefault, createdAt, updatedAt) can be serialized and in which contexts. The file uses serialization groups to control attribute visibility across different API endpoints and operations—specifically for admin CRUD operations (read, create, update) and webmethod customer read operations—enabling role-based and context-aware JSON/XML output formatting.

