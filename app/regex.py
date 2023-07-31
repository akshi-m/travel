import re


def check_email(email):
    regex = re.compile(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')
    if re.fullmatch(regex, email):
        return True


def check_name(name):
    regex = re.compile(r'(^[a-zA-Z0-9@_]+$)')
    if re.fullmatch(regex, name):
        return True








