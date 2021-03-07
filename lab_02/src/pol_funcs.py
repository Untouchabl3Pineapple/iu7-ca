def get_interval(obj, degree, arg_val):
    try:  # for vector
        for upper_arg_ind in range(len(obj)):
            if obj[upper_arg_ind] >= arg_val:
                break
    except:  # for matrix
        for upper_arg_ind in range(len(obj)):
            if obj[0][upper_arg_ind] >= arg_val:
                break

    lower_arg_ind = upper_arg_ind

    while upper_arg_ind - lower_arg_ind < degree:
        if lower_arg_ind > 0:
            lower_arg_ind -= 1
        if upper_arg_ind - lower_arg_ind >= degree:
            break
        if upper_arg_ind < len(obj) - 1:
            upper_arg_ind += 1

    return lower_arg_ind, upper_arg_ind


def get_diffs_table(table, interval):
    """
    interval[0] - the lower index of the argument
    interval[1] - the upper index of the argument
    """

    diffs_table = [[], []]

    for i in range(interval[0], interval[1] + 1):
        diffs_table[0].append(table[i][0])
        diffs_table[1].append(table[i][1])

    for i in range(1, len(diffs_table[0])):
        row = []
        for j in range(len(diffs_table[0]) - i):
            if diffs_table[0][j] - diffs_table[0][j + i] == 0:
                continue

            row.append(
                (diffs_table[i][j] - diffs_table[i][j + 1])
                / (diffs_table[0][j] - diffs_table[0][j + i])
            )
        diffs_table.append(row)

    return diffs_table


def get_val_pol(table, arg_val, interval):
    table.sort()

    diffs_table = get_diffs_table(table, interval)

    mul = 1
    val = diffs_table[1][0]

    for i in range(2, len(diffs_table)):
        mul *= arg_val - diffs_table[0][i - 2]
        val += diffs_table[i][0] * mul

    return val