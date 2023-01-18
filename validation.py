from typing import Union


class InvalidInputException(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)


def validate_input_not_blank(input_name: str, additional_info: str = "") -> str:
    prompt = f'Please enter {input_name}'
    if len(additional_info) != 0:
        prompt = prompt + f' ({additional_info}): '
    else:
        prompt = prompt + ": "
    user_input = input(prompt)
    if not user_input:
        raise InvalidInputException(f'{input_name} must not be blank')
    return user_input


def validate_is_number(input_name: str, additional_info: str = "", number_type: str = "int") -> Union[int, float]:
    user_input = 0
    match number_type:
        case "int":
            try:
                user_input = int(validate_input_not_blank(
                    input_name, additional_info))
            except ValueError as exception:
                raise InvalidInputException(
                    f'Cannot convert {input_name} into a {number_type}') from exception
        case "float":
            try:
                user_input = float(validate_input_not_blank(
                    input_name, additional_info))
            except ValueError as exception:
                raise InvalidInputException(
                    f'Cannot convert {user_input} into a {number_type}') from exception
        case _:
            raise InvalidInputException(
                "Number type must be either int or float")
    return user_input
