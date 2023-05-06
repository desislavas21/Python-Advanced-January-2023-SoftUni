# You will be given some emails until you receive the command "End". Create the following custom exceptions to validate the emails:
#
# · NameTooShortError - raise it when the name in the email is less than or equal to 4 ("peter" will be the name in the email "peter@gmail.com")
#
# · MustContainAtSymbolError - raise it when there is no "@" in the email
#
# · InvalidDomainError - raise it when the domain of the email is invalid (valid domains are: .com, .bg, .net, .org)
#
# When an error is encountered, raise it with an appropriate message:
#
# · NameTooShortError - "Name must be more than 4 characters"
#
# · MustContainAtSymbolError - "Email must contain @"
#
# · InvalidDomainError - "Domain must be one of the following: .com, .bg, .org, .net"
#
# Hint: use the following syntax to add a message to the Exception: MyException("Exception Message")
#
# If the current email is valid, print "Email is valid" and read the next one

import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


def email_slicer(email):
    pattern = r"([\w]+)(@)+([\w]+)(\.[\w]+)"
    grouped_email = (re.findall(pattern, email))[0]
    return grouped_email


def email_checker(email):
    min_length_name = 4
    allowed_domains = [".com", ".bg", ".net", ".org"]
    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")
    grouped = email_slicer(email)
    length_email_name = len(grouped[0])
    domain = grouped[-1]
    if length_email_name <= min_length_name:
        raise NameTooShortError("Name must be more than 4 characters")
    if domain not in allowed_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .net, .org")
    else:
        return "Email is valid"


while True:
    command = input()
    if command == "End":
        break
    current_email = command
    print(email_checker(current_email))
