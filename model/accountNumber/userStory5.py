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
    valid_numbers = {
        ' _ | ||_|': 0,
        '     |  |': 1,
        ' _  _||_ ': 2,
        ' _  _| _|': 3,
        '   |_|  |': 4,
        ' _ |_  _|': 5,
        ' _ |_ |_|': 6,
        ' _   |  |': 7,
        ' _ |_||_|': 8,
        ' _ |_| _|': 9,
        ' _ |_|| |': 10,
        ' _ |_\|_/': 11,
        ' _ |  |_ ': 12,
        ' _ | \|_/': 13,
        ' _ |_ |_ ': 14,
        ' _ |_ |  ': 15
    }

    if number in valid_numbers.keys():
        return valid_numbers[number]
    else:
        return "?" + number + "?"


def convert_line_account_numbers_to_int_account_numbers(raw_data_lines):
    line_account_numbers = separate_line_number_to_number_list(raw_data_lines)
    account_numbers = []
    for line_account_number in line_account_numbers:
        account_number = []
        for number in line_account_number:
            account_number.append(str(convert_line_number_to_integer(number)))
        validated_account_number = validate_account_number(account_number)
        account_numbers.append(validated_account_number)
    return account_numbers


def calculate_check_sum(account_number):
    sum = 0
    for index in range(len(account_number)):
        sum += int(account_number[index]) * (9 - index)
    return sum % 11


def validate_account_number(account_number):
    if "?" in list_to_string(account_number):
        account_number = guess_wrong_scan(account_number)
    elif calculate_check_sum(account_number) != 0:
        valid_account_numbers = change_number(account_number)
        if len(valid_account_numbers) == 0:
            account_number = account_number_to_string(account_number) + " ERR"
        elif len(valid_account_numbers) == 1:
            account_number = account_number_to_string(valid_account_numbers[0])
        else:
            account_number = account_number_to_string(account_number) + " AMB ['"
            for alternative in valid_account_numbers:
                account_number += account_number_to_string(alternative) + "', '"
            account_number = account_number[:-4] + "']"
    else:
        account_number = account_number_to_string(account_number)
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
        ' _ | ||_|': 0,
        ' _ |_|| |': 10,
        ' _ |_\|_/': 11,
        ' _ |  |_ ': 12,
        ' _ | \|_/': 13,
        ' _ |_ |_ ': 14,
        ' _ |_ |  ': 15
    }

    splited_number = list_to_string(invalid_scan_input).split("?")
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
        "8": ["0", "6", "9", "10"],
        "9": ["3", "5", "8"],
        "10": ["8"],
        "11": ["13"],
        "12": ["14"],
        "13": ["11"],
        "14": ["12", "15"],
        "15": ["14"]
    }
    for index in range(len(account_number)):
        char = account_number[index]
        if char in changeable_values.keys():
            for changed in changeable_values[char]:
                new_account = account_number.copy()
                new_account[index] = changed
                if calculate_check_sum(new_account) == 0:
                    valid_account_numbers.append(new_account)
    return valid_account_numbers


def calculate_difference(original_string, new_string):
    difference = 0
    for index in range(len(original_string)):
        if original_string[index] != new_string[index]:
            difference += 1
    return difference


def list_to_string(s):
    string = ""
    for element in s:
        string += element
    return string


def account_number_to_string(s):
    valid_numbers = {
        '0': '0',
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9',
        '10': 'a',
        '11': 'b',
        '12': 'c',
        '13': 'd',
        '14': 'e',
        '15': 'f'
    }
    string = ""
    for element in s:
        string += valid_numbers[element]
    return string
