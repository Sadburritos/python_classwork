import re


def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is None


with open("email.txt", 'r') as file:
    for line in file:
        emails = line.split()
        for email in emails:
            if validate_email(email):
                print(f"{email} - некорректный адрес")
