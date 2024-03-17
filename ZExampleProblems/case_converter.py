# https://docs.google.com/document/d/1JBkEgan03M6dWyfKBQhzHzxu-0TuMLpBSoJxGazA-rc/edit

import json


def convert(input_dict: dict):

    result_dict = {}

    for key in input_dict:

        split_camel = key.split("_")
        split_kebab = key.split("-")
        new_key = key

        if len(split_camel) > 1:
            new_key = convertCase(split_camel)
        elif len(split_kebab) > 1:
            new_key = convertCase(split_kebab)
        elif key[0].isupper():
            new_key = key[0].lower() + key[1:]

        result_dict[new_key] = input_dict[key]

        if type(result_dict[new_key]) is dict:
            converted_value = convert(result_dict[new_key])
            result_dict[new_key] = converted_value

    return result_dict


def convertCase(split_list: list) -> str:
    result = ""
    for each in split_list:

        if result:
            each = each[0].upper() + each[1:]

        result += each

    return result


a = """
{
    "first_name": "John",
    "lastName": "Doe",
    "ContactInfo": {
        "email-address": "john@example.com",
        "phone_number": "123-456-7890",
        "activities": {
            "Cycling":"kuch bhi",
            "allah-akbar":"kuran"
        }
    }
}
"""

print(a)
b = json.loads(a)

print(convert(b))
