from model.data_manager import read_table_from_file


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
        account_numbers.append(str(account_number))
    return account_numbers
