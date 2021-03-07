def table_args_convert_to_float(table):
    for row in table:
        for i in range(len(row)):
            row[i] = float(row[i])


def input_inf():
    filename = input("Input the filename: ")

    try:
        with open(filename) as file:
            table = [row.split() for row in file.readlines()]

        x_degree = int(input("Input nx: "))
        y_degree = int(input("Input ny: "))

        x_arg_val = float(input("Input x: "))
        y_arg_val = float(input("Input y: "))

    except:
        print("Error, check that the data is correct")
        exit()

    table_args_convert_to_float(table)

    return table, x_degree, y_degree, x_arg_val, y_arg_val


def print_res(res):
    print("Result: {:.4f}".format(res))
