def separate_line_number_to_number_list(raw_data_lines):
    account_numbers = []
    for line_index in range(len(raw_data_lines) // 4):
        numbers = []
        for index in range(9):
            number_lines = []
            for line_count in range(1, 4):
                number_lines.append(raw_data_lines[line_count + line_index * 4][0 + index * 3:3 + index * 3])
            numbers.append(number_lines)
        account_numbers.append(numbers)
    return account_numbers


def convert_line_number_to_integer(line_number):
    number = line_number[0] + line_number[1] + line_number[2]
    if number == '     |  |':
        return 1
    elif number == ' _  _||_ ':
        return 2
    elif number == ' _  _| _|':
        return 3
    elif number == '   |_|  |':
        return 4
    elif number == ' _ |_  _|':
        return 5
    elif number == ' _ |_ |_|':
        return 6
    elif number == ' _   |  |':
        return 7
    elif number == ' _ |_||_|':
        return 8
    elif number == ' _ |_| _|':
        return 9
    elif number == ' _ | ||_|':
        return 0
    else:
        return "?" + number + "?"


def convert_line_account_numbers_to_int_account_numbers(raw_data_lines):
    line_account_numbers = separate_line_number_to_number_list(raw_data_lines)
    account_numbers = []
    for line_account_number in line_account_numbers:
        account_number = ""
        for number in line_account_number:
            account_number += str(convert_line_number_to_integer(number))
        validated_account_number = validate_account_number(str(account_number))
        account_numbers.append(validated_account_number)
    return account_numbers


def calculate_check_sum(account_number):
    sum = 0
    for index in range(len(account_number)):
        sum += int(account_number[index]) * (9 - index)
    return sum % 11


def validate_account_number(account_number):
    if len(account_number) > 9:
        account_number = guess_wrong_scan(account_number)
    elif calculate_check_sum(account_number) != 0:
        valid_account_numbers = change_number(account_number)
        if len(valid_account_numbers) == 0:
            account_number += " ERR"
        elif len(valid_account_numbers) == 1:
            account_number = valid_account_numbers[0]
        else:
            account_number += " AMB ['"
            for alternative in valid_account_numbers:
                account_number += alternative + "', '"
            account_number = account_number[:-4] + "']"
    return account_number


def guess_wrong_scan(invalid_scan_input):
    valid_numbers = {
        '     |  |': 1,
        ' _  _||_ ': 2,
        ' _  _| _|': 3,
        '   |_|  |': 4,
        ' _ |_  _|': 5,
        ' _ |_ |_|': 6,
        ' _   |  |': 7,
        ' _ |_||_|': 8,
        ' _ |_| _|': 9,
        ' _ | ||_|': 0
    }

    splited_number = invalid_scan_input.split("?")
    new_number = ""
    possible_numbers = []
    for element in splited_number:
        if " " in element:
            for valid in valid_numbers.keys():
                if calculate_difference(valid, element) == 1:
                    possible_numbers.append(valid_numbers[valid])
            new_number += "?"
        else:
            new_number += element
    new_number = possible_new_number_guesser(new_number, possible_numbers)
    return new_number


def possible_new_number_guesser(invalid_number, possible_numbers):
    index = invalid_number.find("?")
    valid_number = 0
    for number in possible_numbers:
        possible_number = str(invalid_number[0:index]) + str(number) + str(invalid_number[index + 1:])
        if calculate_check_sum(possible_number) == 0:
            valid_number = possible_number
    return valid_number


def change_number(account_number):
    valid_account_numbers = []
    changeable_values = {
        "0": ["8"],
        "1": ["7"],
        "3": ["9"],
        "5": ["6", "9"],
        "6": ["5", "8"],
        "7": ["1"],
        "8": ["0", "6", "9"],
        "9": ["3", "5", "8"]
    }
    for index in range(len(account_number)):
        char = account_number[index]
        if char in changeable_values.keys():
            for changed in changeable_values[char]:
                new_account = account_number[0:index] + changed + account_number[index + 1:]
                if calculate_check_sum(new_account) == 0:
                    valid_account_numbers.append(new_account)
    return valid_account_numbers


def calculate_difference(original_string, new_string):
    difference = 0
    for index in range(len(original_string)):
        if original_string[index] != new_string[index]:
            difference += 1
    return difference
