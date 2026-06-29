# Auth and Permissions Safety Checklist

Use this when the change touches identity, authentication, authorization, tenancy, secrets, or privileged workflows.

## Design coverage

- actors and trust boundaries
- authentication mechanism and token assumptions
- authorization rules and ownership model
- tenant isolation and data scoping
- privilege escalation and abuse cases
- auditability and security logging
- failure behavior for denied, expired, missing, or malformed credentials

## Requirement coverage

- explicit allow and deny behavior
- negative-path and abuse-case requirements
- audit or security signal requirements

## Task coverage

- auth tests
- tenant-boundary tests
- security logging or alert updates
- rollout safeguards for privileged behavior
