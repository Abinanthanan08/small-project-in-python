import re

def email_valid(mail):
    pattern=r'^[^\s@]+@[^\s@]+\.[^\s@]+$'

    if re.match(pattern,mail):
        return True

    else:
        return False


print(email_valid("abbi@domain.com"))
print(email_valid("ram@ domain.com"))
print(email_valid("ram@domain.c"))