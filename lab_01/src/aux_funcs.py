import copy


def table_args_convert_to_float(table):
    for row in table:
        for i in range(len(row)):
            row[i] = float(row[i])


def swap_clms(table):
    new_table = copy.deepcopy(table)

    for row in new_table:
        row[0], row[1] = row[1], row[0]

    return new_table


def get_extend_table(table):
    ext_table = []

    for row in table:
        ext_table.append(row)
        ext_table.append(row)

    return ext_table
