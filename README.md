# Email Domain Validator

A simple Python library to validate if an email's domain exists and is configured to receive emails by checking its DNS (MX and A) records.

## Installation

Install directly from GitHub:
```bash
pip install git+https://github.com/your-username/email_domain_validator_project.git

# Usage
from email_domain_validator import validate_email_domain

is_valid, message = validate_email_domain("contact@google.com")
print(is_valid, message)
# Output: True, Domain 'google.com' is valid and has MX records.

is_valid, message = validate_email_domain("test@nonexistent-domain123.com")
print(is_valid, message)
# Output: False, Domain 'nonexistent-domain123.com' does not exist (NXDOMAIN).