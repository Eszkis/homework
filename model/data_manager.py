def read_table_from_file(file_name):
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
        return [element.replace("\n", "") for element in lines][1:]
    except IOError:
        return []


'''
def write_table_to_file(file_name, table, separator=';'):
    """Write tabular data into a CSV file.

    Args:
        file_name: The name of the file to write to.
        table: list of lists containing tabular data.
        separator: The CSV separator character
    """
    with open(file_name, "w") as file:
        for record in table:
            row = separator.join(record)
            file.write(row + "\n")
'''
