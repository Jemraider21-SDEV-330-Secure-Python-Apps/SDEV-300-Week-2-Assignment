from typing import Union


class InvalidInputException(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)


def conversion_error_message(exception: Exception, input_name: str, typing: str) -> str:
    error_name = exception.__class__.__name__
    print(f'{error_name}: Cannot convert {input_name} to a {typing}. Try again')


def validate_input_not_blank(input_name: str, additional_info: str = "") -> str:
    looper: bool = True
    user_input: str = ""
    while looper:
        prompt = f'Please enter {input_name}'
        if len(additional_info) != 0:
            prompt = prompt + f' ({additional_info}): '
        else:
            prompt = prompt + ": "
        user_input = input(prompt)
        if not user_input:
            # raise InvalidInputException(f'{input_name} must not be blank')
            print(f'{input_name} must not be blank. Try again')
        else:
            looper = False
    return user_input


def validate_is_boolean(input_name: str, additional_info: str = ""):
    user_input: bool = True
    while True:
        user_input = validate_input_not_blank(input_name, additional_info)
        match user_input.upper():
            case "TRUE":
                user_input = True
                break
            case "FALSE":
                user_input = False
                break
            case _:
                conversion_error_message(
                    InvalidInputException, input_name, "boolean")
    return user_input


def validate_is_number(input_name: str, additional_info: str = "", number_type: str = "int") -> Union[int, float]:
    user_input: int = 0
    looper: bool = True
    match number_type:
        case "int":
            while looper:
                try:
                    user_input = int(validate_input_not_blank(
                        input_name, additional_info))
                    looper = False
                except ValueError as exception:
                    conversion_error_message(exception, input_name, "integer")
        case "float":
            while looper:
                try:
                    user_input = float(validate_input_not_blank(
                        input_name, additional_info))
                    looper = False
                except ValueError as exception:
                    conversion_error_message(exception, input_name, "float")
        case _:
            raise InvalidInputException(
                "Number type must be either int or float")
    return user_input
