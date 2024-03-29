#!/usr/local/bin/python3
import re
# Design a regular expression pattern to validate a password that must contain
# at least one uppercase letter, one lowercase letter, and one digit,
# with a minimum length of 8 characters.

# Example strings:

# "Passw0rd"
# "SecurePa55"
# "weakpassword"

def is_valid(text):
    pattern = re.compile(r'[A-Za-z][0-9]')
    match = pattern.findall(text)

    if match:
        print("strong password {}".format(match.group()))
    else:
        print("Weak password {}".format(match.group()))


is_valid("Passw0rd")
is_valid("SecurePa55")
is_valid("weakpassword")