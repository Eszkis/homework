import os
from model.data_manager import read_table_from_file
from model.accountNumber import accountNumber

if __name__ == '__main__':
    os.system('clear')
    lines = read_table_from_file("model/accountNumber/rawData.txt")
    for number in accountNumber.separate_line_number_to_number_list(lines):
        for line in number:
            print(line)

