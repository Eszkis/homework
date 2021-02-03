import os
from model.data_manager import read_table_from_file
from model.accountNumber import accountNumber

if __name__ == '__main__':
    os.system('clear')
    lines = read_table_from_file("model/accountNumber/rawData.txt")
    int_account_numbers = accountNumber.convert_line_account_numbers_to_int_account_numbers(lines)
    for number in int_account_numbers:
        print(number)

