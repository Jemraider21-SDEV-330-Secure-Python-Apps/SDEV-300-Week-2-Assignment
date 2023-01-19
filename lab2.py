import random
import string
from validation import InvalidInputException, validate_is_number, validate_is_boolean


def menu() -> int:
    print("1. Generate Secure Password")
    print("2. Calculate And Format A Percentage")
    print("3. How Many Days Until July 4, 2025?")
    print("4. Use The Law Of Cosine To Calculate The Leg Of A Triangle")
    print("5. Calculate The Volume Of A Right Circular Cylindar")
    print("6. Exit Program")
    user_input_looper = True
    while user_input_looper:
        user_input = validate_is_number("Menu Selection")
        if user_input not in range(1, 7):
            print("Error - User Input out of range. Please try again")
        else:
            user_input_looper = False
    return user_input


def generate_password() -> str:
    characters: str = ""
    additional_info = "True/False"
    length = validate_is_number("length of password")
    use_lowercase: bool = validate_is_boolean(
        "boolean for lower case letters", additional_info)
    if use_lowercase:
        characters += string.ascii_lowercase
    use_uppercase: bool = validate_is_boolean(
        "boolean for upper case letters", additional_info)
    if use_uppercase:
        characters += string.ascii_uppercase
    use_numbers: bool = validate_is_boolean(
        "boolean for numbers", additional_info)
    if use_numbers:
        characters += string.digits
    use_specials = validate_is_boolean(
        "boolean for special characters", additional_info)
    if use_specials:
        characters += string.punctuation
    return "".join(random.choice(characters) for i in range(length))


def calculate_format_percentage() -> float:
    numerator: int = validate_is_number("Numerator")
    denominator: int = validate_is_number("Denominator")
    result: float = (numerator/denominator) * 100
    decimal: int = validate_is_number("Number of Decimals")
    return round(result, decimal)


def main():
    print("Welcome to the program!\n")
    menu_loop = True
    while menu_loop:
        try:
            selection = menu()
            match selection:
                case 1:
                    print("\nGenerating secure password")
                    print(
                        f'Your new generated password: {generate_password()}\n')
                case 2:
                    print("\nCalculating and formating a percentage")
                    print(
                        f'The calculated percentage: {calculate_format_percentage()} \n')
                case 3:
                    print("Days until july 4 2025\n")
                case 4:
                    print("Using the law of cosine\n")
                case 5:
                    print("calculating volume\n")
                case 6:
                    menu_loop = False
        except InvalidInputException as exception:
            print(f'{exception.__class__.__name__}: {exception}\n')
    print("\nThank you for using the program!")


if __name__ == "__main__":
    main()
