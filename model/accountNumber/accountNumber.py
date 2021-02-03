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
    if line_number[0] == '   ' and line_number[1] == '  |' and line_number[2] == '  |':
        return 1
    elif line_number[0] == ' _ ' and line_number[1] == ' _|' and line_number[2] == '|_ ':
        return 2
    elif line_number[0] == ' _ ' and line_number[1] == ' _|' and line_number[2] == ' _|':
        return 3
    elif line_number[0] == '   ' and line_number[1] == '|_|' and line_number[2] == '  |':
        return 4
    elif line_number[0] == ' _ ' and line_number[1] == '|_ ' and line_number[2] == ' _|':
        return 5
    elif line_number[0] == ' _ ' and line_number[1] == '|_ ' and line_number[2] == '|_|':
        return 6
    elif line_number[0] == ' _ ' and line_number[1] == '  |' and line_number[2] == '  |':
        return 7
    elif line_number[0] == ' _ ' and line_number[1] == '|_|' and line_number[2] == '|_|':
        return 8
    elif line_number[0] == ' _ ' and line_number[1] == '|_|' and line_number[2] == ' _|':
        return 9
    elif line_number[0] == ' _ ' and line_number[1] == '| |' and line_number[2] == '|_|':
        return 0
    else:
        return "?"


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
    if "?" in account_number:
        account_number += " ILL"
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
