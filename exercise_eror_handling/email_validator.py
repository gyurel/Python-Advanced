import sys
from io import StringIO
from errors import NameTooShortError, MustContainAtSymbolError, InvalidDomainError

test_intput1 = """abc@abv.bg
"""

test_intput2 = """peter@gmail.com
petergmail.com
"""

test_intput3 = """peter@gmail.hotmail
"""

sys.stdin = StringIO(test_intput1)
# sys.stdin = StringIO(test_intput2)
# sys.stdin = StringIO(test_intput3)

valid_domains_list = ['.com', '.bg', '.org', '.net']

while True:
    email = input()

    if email == 'End':
        break

    email = email.split('@')

    if len(email) == 1:
        raise MustContainAtSymbolError("Email must contain @")

    name, subdomain_domain = email

    if len(name) < 4:
        raise NameTooShortError("Name must be more than 4 characters")

    subdomain, domain = subdomain_domain.split('.')

    if f".{domain}" not in valid_domains_list:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")
