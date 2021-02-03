def read_table_from_file(file_name):
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
        return [element.replace("\n", "") for element in lines]
    except IOError:
        return []


def write_table_to_file(file_name, table):
    with open(file_name, "w") as file:
        for record in table:
            file.write(record + "\n")
