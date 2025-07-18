import dns.resolver
import re

def validate_email_domain(email):
    if not email:
        return (False, "Email is None or empty")
    
    if not isinstance(email, str):
        return (False, f"Invalid type: expected str, got {type(email)}")

    if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
        return (False, "Invalid email syntax")

    try:
        domain = email.split('@')[1]
    except IndexError:
        return (False, "Cannot extract domain")

    try:
        dns.resolver.resolve(domain, 'MX')
        return (True, f"Domain '{domain}' is valid and has MX records.")
    except dns.resolver.NoAnswer:
        try:
            dns.resolver.resolve(domain, 'A')
            return (True, f"Domain '{domain}' is valid (has A record, but no MX record).")
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
            return (False, f"Domain '{domain}' has no MX or A records.")
    except dns.resolver.NXDOMAIN:
        return (False, f"Domain '{domain}' does not exist (NXDOMAIN).")
    except dns.exception.Timeout:
        return (False, f"DNS query for '{domain}' timed out.")
    except Exception as e:
        return (False, f"An error occurred: {e}")