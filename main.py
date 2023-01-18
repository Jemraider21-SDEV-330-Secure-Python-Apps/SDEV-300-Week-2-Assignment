
from validation import InvalidInputException, validate_is_number, validate_input_not_blank


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


def main():
    print("Welcome to the program!\n")
    menu_loop = True
    while menu_loop:
        try:
            selection = menu()
            match selection:
                case 1:
                    print("Generating secure password\n")
                case 2:
                    print("Calculating and formating a percentage\n")
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


main()
