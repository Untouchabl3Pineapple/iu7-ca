from myio import input_inf, print_res
from process import process


def main():
    inform = input_inf()
    table, x_degree, y_degree, x_arg_val, y_arg_val = (
        inform[0],
        inform[1],
        inform[2],
        inform[3],
        inform[4],
    )

    res = process(table, x_degree, y_degree, x_arg_val, y_arg_val)
    print_res(res)


if __name__ == "__main__":
    main()