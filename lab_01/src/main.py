from myio import *
from process_funcs import *
from aux_funcs import get_extend_table, swap_clms


def main():
    """
    new_table - table with rearranged columns for reverse interpolation
    """

    inform = input_inf()
    table, degree, arg_val = inform[0], inform[1], inform[2]
    ext_table = get_extend_table(table)
    new_table = swap_clms(table)

    newton = get_val_pol(table, degree, arg_val)
    hermite = get_val_pol(ext_table, degree, arg_val)
    root = get_val_pol(new_table, degree, 0)

    print_results(newton, hermite, root)


if __name__ == "__main__":
    main()
