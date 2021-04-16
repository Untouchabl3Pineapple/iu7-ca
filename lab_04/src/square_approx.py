"""
    square_approx.py
"""

from random import randint
import matplotlib.pyplot as plt
from copy import deepcopy


class RootMeanSquareApproximation:
    def __init__(self):
        self.table = self.__gen_table()
        self.__flag_changed = False

    @staticmethod
    def print_menu():
        print(
            "\n\nMenu\n\
        \n1. Print the table\
        \n2. Change the point weight\
        \n3. Print the results\
        \n0. Exit"
        )

    @staticmethod
    def __gen_table(size=7, default_weight=1):

        table = [
            [randint(1.0, 100.0), randint(1.0, 100.0), default_weight]
            for _ in range(size)
        ]

        table.sort()

        return table

    @staticmethod
    def get_slau_matrix(table, power):
        size = len(table)

        matrix = [[0 for i in range(power + 2)] for i in range(power + 1)]

        for i in range(power + 1):
            for j in range(power + 1):
                a_coeff = 0.0
                rs_coeff = 0.0

                for k in range(size):
                    weight = table[k][2]
                    x = table[k][0]
                    y = table[k][1]

                    a_coeff += weight * pow(x, i + j)
                    rs_coeff += weight * y * pow(x, i)

                matrix[i][j] = a_coeff
                matrix[i][power + 1] = rs_coeff

        return matrix

    @staticmethod
    def gauss(matrix):
        size = len(matrix)

        for i in range(size):
            for j in range(i + 1, size):
                if i == j:
                    continue

                k = matrix[j][i] / matrix[i][i]

                for q in range(i, size + 1):
                    matrix[j][q] -= k * matrix[i][q]

        result = [0 for i in range(size)]

        for i in range(size - 1, -1, -1):
            for j in range(size - 1, i, -1):
                matrix[i][size] -= result[j] * matrix[i][j]

            result[i] = matrix[i][size] / matrix[i][i]

        return result

    @staticmethod
    def get_coords(table):
        x_arr = []
        y_arr = []

        for i in range(len(table)):
            x_arr.append(table[i][0])
            y_arr.append(table[i][1])

        return x_arr, y_arr

    @staticmethod
    def set_default_weights(table):
        for i in range(len(table)):
            table[i][2] = 1

    def print_table(self):
        print("\nGenerated table\n")

        print("  №    |     x      |     y      |   w   ")
        print("--------------------------------------")

        for i in range(len(self.table)):
            print(
                "  %-3d  |   %-6.2f   |   %-6.2f   |   %-6.2f   "
                % (i + 1, self.table[i][0], self.table[i][1], self.table[i][2])
            )

    def change_weight(self):
        self.__flag_changed = True

        try:
            position = int(input("\nInput the point number in the table: "))
            new_weight = float(input("\nInput the new point weight: "))
        except:
            print("\n\nInvalid data\n\n")
            return

        if position < 1 or position > len(self.table):
            print("\n\nInvalid data\n\n")
            return

        self.table[position - 1][2] = new_weight

    def get_dots(self, table, cur_power, eps=0.01):
        matrix = self.get_slau_matrix(table, cur_power)
        result = self.gauss(matrix)

        x, y = [], []
        k = table[0][0] - eps

        while k <= table[len(table) - 1][0] + eps:
            y_cur = 0
            for j in range(0, cur_power + 1):
                y_cur += result[j] * pow(k, j)

            x.append(k)
            y.append(y_cur)

            k += eps

        return x, y

    def draw(self):
        try:
            power = int(input("\nInput the degree of the approximating polynomial: "))
        except:
            print("\n\nInvalid data\n\n")
            return

        if self.__flag_changed:
            changed_table = deepcopy(self.table)
            self.set_default_weights(self.table)

        for cur_power in range(1, power + 1):
            if cur_power > 2 and cur_power < power:
                continue

            x, y = self.get_dots(self.table, cur_power)

            plt.plot(x, y, label="Equal weights:\nn = %d" % (cur_power))

            if self.__flag_changed:
                x, y = self.get_dots(changed_table, cur_power)

                plt.plot(x, y, label="Diff weights:\nn = %d" % (cur_power))

        x_arr, y_arr = self.get_coords(self.table)

        plt.plot(x_arr, y_arr, "o", label="Date")
        plt.legend()
        plt.grid()
        plt.xlabel("Axis X")
        plt.ylabel("Axis Y")
        plt.show()

        if self.__flag_changed:
            self.table = changed_table
