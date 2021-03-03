from aux_funcs import table_args_convert_to_float


def input_inf():
    filename = input("Input the filename: ")

    try:
        with open(filename) as file:
            table = [row.split() for row in file.readlines()]

        degree = int(input("Input the degree of the polynomial: "))
        arg_val = float(input("Input the value of the argument: "))

    except:
        print("Error, check that the data is correct")
        exit()

    table_args_convert_to_float(table)

    return table, degree, arg_val


def print_results(newton, hermite, root):
    print("Newton: {:.6f}".format(newton))
    print("Hermite: {:.6f}".format(hermite))
    print("Root: {:.6f}".format(root))
