def print_menu(title, list_options):
    index = 1
    menu = title + "\n"
    while index < len(list_options):
        menu = menu + "(" + str(index) + ") " + list_options[index] + "\n"
        index += 1
    menu = menu + "(0) " + list_options[0]
    print(menu)


def print_message(message):
    print(message)


def print_general_results(result):
    for element in result:
        print(element)


def get_input(label):
    """Gets single string input from the user.

    Args:
        label: str - the label before the user prompt
    """
    valid_input = "012345"
    label = label.lower()
    single_input = input(label + "\n")
    while single_input not in valid_input:
        print_message("Invalid input. Please give a number between 1-5!")
        single_input = input(label + "\n")
    return single_input


def print_error_message(message):
    """Prints an error message to the terminal.

    Args:
        message: str - the error message
    """
    print(message)
