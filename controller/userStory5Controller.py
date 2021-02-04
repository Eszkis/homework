from model import data_manager
from model.accountNumber.userStory5 import convert_line_account_numbers_to_int_account_numbers


def run():
    input_file = "resource/input/rawData5.txt"
    output_file = "resource/output/output5.txt"
    lines = data_manager.read_table_from_file(input_file)
    int_account_numbers = convert_line_account_numbers_to_int_account_numbers(lines)
    data_manager.write_table_to_file(output_file, int_account_numbers)
