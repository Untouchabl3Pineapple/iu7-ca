from pol_funcs import *


def process(table, x_degree, y_degree, x_arg_val, y_arg_val):
    """
    MagicFlow
    """

    x_vals = table[0].copy()
    table.pop(0)

    ptable = [[el] for el in x_vals]

    y_vals = []
    for i in range(len(table)):
        y_vals.append(table[i][0])
        table[i].pop(0)

    x_interval = get_interval(x_vals, x_degree, x_arg_val)
    y_interval = get_interval(y_vals, y_degree, y_arg_val)

    presults = []

    for i in range(y_interval[0], y_interval[1] + 1):
        for j in range(len(table[i])):
            ptable[j].append(table[i][j])
        presults.append(get_val_pol(ptable, x_arg_val, x_interval))
        for j in range(len(table[i])):
            ptable[j].pop(1)

    px_vals = [[x_vals[i]] for i in range(x_interval[0], x_interval[1] + 1)]
    for i in range(len(px_vals)):
        px_vals[i].append(presults[i])

    px_interval = [0, len(px_vals) - 1]

    res = get_val_pol(px_vals, x_arg_val, px_interval)

    return res