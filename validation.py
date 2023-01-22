"""A module that contains common validation functions and exceptions

Raises:
    InvalidInputException: User entered something not expected, so throw an exception
"""
from typing import Union


class InvalidInputException(Exception):
    """An exception to throw in the case an unexpected user input was given

    Args:
        Exception (string): The message of the exception
    """

    def __init__(self, message) -> None:
        super().__init__(message)


def conversion_error_message(exception: Exception, input_name: str, typing: str) -> str:
    """Create an error message explaining that
    converting a given input to a given type was not successful

    Args:
        exception (Exception): the thrown exception to generate the message
        input_name (str): The name of the input (ex: First Name)
        typing (str): The type used for conversion (ex: string, int)

    Returns:
        str: The error message
    """
    error_name = exception.__class__.__name__
    print(f'{error_name}: Cannot convert {input_name} to a {typing}. Try again')


def validate_input_not_blank(input_name: str, additional_info: str = "") -> str:
    """Collect input from the user and ensure it was not blank or empty

    Args:
        input_name (str): Name of the input (ex: First Name)

        additional_info (str, optional):
        Any additional information for prompt (ex: units of measurement).Defaults to "".

    Returns:
        str: the validated and correct user input
    """
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


def validate_is_boolean(input_name: str, additional_info: str = "") -> bool:
    """Validate that the collected user input is both not blank and can be converted to a boolean

    Args:
        input_name (str): Name of the input (ex: First Name)

        additional_info (str, optional):
        Any additional information for prompt (ex: units of measurement).Defaults to "".

    Returns:
        bool: The user input
    """
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


def validate_is_number(input_name: str, additional_info: str = "",
                       number_type: str = "int") -> Union[int, float]:
    """Validate that the user input is not blank and it can be converted to a number, being an int or a float

    Args:
        input_name (str): Name of the input (ex: First Name)

        additional_info (str, optional):
        Any additional information for prompt (ex: units of measurement).Defaults to "".

        number_type (str, optional): The number data type to convert to. Defaults to "int".

    Raises:
        InvalidInputException: Incorrect or unexpected user input

    Returns:
        Union[int, float]: The user input
    """
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
