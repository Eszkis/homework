from model.data_manager import read_table_from_file


def separate_line_number_to_number_list(raw_data_lines):
    numbers = []
    for index in range(9):
        number_lines = []
        for line_count in range(3):
            number_lines.append(raw_data_lines[line_count][0+index*3:3+index*3])
        numbers.append(number_lines)
    return numbers

