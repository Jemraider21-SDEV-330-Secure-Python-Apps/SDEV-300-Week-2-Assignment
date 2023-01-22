"""Jared Morris's Lab 2 Submission for SDEV 300

Returns:
    none
"""

from datetime import date, timedelta
import datetime
import math
import random
import string
from validation import validate_is_number, validate_is_boolean


def menu() -> int:
    """Display the menu for user selection, and prompt for input from the user

    Returns:
        int: The user menu selection
    """
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


def adding_characters(characters: str, to_use: bool, to_add: str) -> str:
    """Concatenates a new string to an existing set of characters if the user selects to use them

    Args:
        characters (str): The base set of characters to use
        to_use (bool): User selection for whether to join the two strings together
        to_add (str): the characters to add to the original set of characters

    Returns:
        str: The set of valid characters to use when creating a password
    """
    return characters + to_add if to_use else characters


def generate_password():
    """Generates a random password based on the user selection, and print it out.
    This can include lower case letters, upper case letters, numbers, and special characters.
    """
    print("\nGenerating secure password")
    characters: str = ""
    additional_info = "True/False"
    length = validate_is_number("length of password")
    use_lowercase: bool = validate_is_boolean(
        "boolean for lower case letters", additional_info)
    use_uppercase: bool = validate_is_boolean(
        "boolean for upper case letters", additional_info)
    use_numbers: bool = validate_is_boolean(
        "boolean for numbers", additional_info)
    use_specials = validate_is_boolean(
        "boolean for special characters", additional_info)

    all_false_input = not any(
        [use_lowercase, use_uppercase, use_numbers, use_specials])
    if all_false_input:
        characters = string.ascii_letters
    else:
        characters = adding_characters(
            characters, use_lowercase, string.ascii_lowercase)
        characters = adding_characters(
            characters, use_uppercase, string.ascii_uppercase)
        characters = adding_characters(characters, use_numbers, string.digits)
        characters = adding_characters(
            characters, use_specials, string.punctuation)
    password: str = "".join(random.choice(characters) for i in range(length))
    print(f'Your new generated password: {password}\n')


def calculate_format_percentage():
    """Calculates and print the formatted percentage based on user input.
    Collects a numerator, denominator, and decimal points for formatting.
    """
    print("\nCalculating and formating a percentage")
    numerator: int = validate_is_number("Numerator")
    denominator: int = validate_is_number("Denominator")
    result: float = (numerator/denominator) * 100
    decimal: int = validate_is_number("Number of Decimals")
    print(f'The calculated percentage: {round(result, decimal)} \n')


def days_until_july_4_2025():
    """Calculate how many days between today's date and July 4, 2025
    """
    print("\nDays until july 4 2025")
    today: date = datetime.date.today()
    future: date = datetime.date(2025, 7, 4)
    difference: timedelta = future - today
    print(f'There are {difference.days} days until July 4, 2025\n')


def law_of_cosines():
    """Use the law of cosines to calculate the length of side C of a triangle.
    Collects the length of side A, side B, and angle C from the user.
    """
    print("\nUsing the law of cosine")
    side_a: float = validate_is_number("Side A", number_type="float")
    side_b: float = validate_is_number("Side B", number_type="float")
    angle_c: float = validate_is_number("Angle C", number_type="float")

    power_calcs = math.pow(side_a, 2) + math.pow(side_b, 2)
    cosine_cals = 2 * side_a * side_b * math.cos(angle_c)
    side_c: float = math.sqrt(power_calcs - cosine_cals)
    print(f'The length of Side C: {round(side_c, 2)}\n')


def volume_right_circular_cylinder():
    """Calulates the volume of a right circular cylinder based on user input.
    Collects the radius and the height of the cylinder
    """
    print("\nCalculating Volume of a Right Circular Cylinder")
    radius: float = validate_is_number("Radius", number_type="float")
    height: float = validate_is_number("Height", number_type="float")
    volume: float = math.pi * math.pow(radius, 2) * height
    print(f'The volume of the right circular cylinder: {round(volume, 2)}\n')


def main():
    """Main driver of the program.
    Prompts the user for a menu selection, then performs said menu action.
    Repeats until the user selects to exit the program.
    """
    print("Welcome to the program!\n")
    menu_loop = True
    while menu_loop:
        selection = menu()
        match selection:
            case 1:
                generate_password()
            case 2:
                calculate_format_percentage()
            case 3:
                days_until_july_4_2025()
            case 4:
                law_of_cosines()
            case 5:
                volume_right_circular_cylinder()
            case 6:
                menu_loop = False
    print("\nThank you for using the program!")


if __name__ == "__main__":
    main()
