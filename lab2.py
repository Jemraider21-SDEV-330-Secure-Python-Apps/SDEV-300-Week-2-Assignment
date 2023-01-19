from datetime import date, timedelta
import datetime
import math
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


def days_until_july_4_2025() -> int:
    today: date = datetime.date.today()
    future: date = datetime.date(2025, 7, 4)
    difference: timedelta = future - today
    return difference.days


def law_of_cosines():
    side_a: float = validate_is_number("Side A", number_type="float")
    side_b: float = validate_is_number("Side B", number_type="float")
    angle_c: float = validate_is_number("Angle C", number_type="float")

    power_calcs = math.pow(side_a, 2) + math.pow(side_b, 2)
    cosine_cals = 2 * side_a * side_b * math.cos(angle_c)
    side_c: float = math.sqrt(power_calcs - cosine_cals)
    return side_c


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
                    print("\nDays until july 4 2025")
                    print(
                        f'There are {days_until_july_4_2025()} days until July 4, 2025\n')
                case 4:
                    print("\nUsing the law of cosine")
                    print(f'The length of Side C: {law_of_cosines()}\n')
                case 5:
                    print("\nCalculating volume\n")
                case 6:
                    menu_loop = False
        except InvalidInputException as exception:
            print(f'{exception.__class__.__name__}: {exception}\n')
    print("\nThank you for using the program!")


if __name__ == "__main__":
    main()
