"""
    integral_class.py
"""

from numpy import arange
from numpy.polynomial.legendre import leggauss
from math import pi, cos, sin, exp
import matplotlib.pyplot as plt

""" Calculation of the two-fold integral using the quadrature formulas of Gauss and Simpson """

class Integral:
    
    def __init__(self):
        self.choice = 1

    """ __________________________________METHODS_______________________________________ """


    @staticmethod
    def gauss(func, a, b, numb):
        args, coeffs = leggauss(numb)
        res = 0

        for i in range(numb):
            res += (b - a) / 2 * coeffs[i] * func((b + a) / 2 + (b - a) * args[i] / 2)

        return res


    @staticmethod
    def simpson(func, a, b, numb):
        h = (b - a) / (numb - 1)
        x = a
        res = 0

        for _ in range((numb - 1) // 2):
            res += func(x) + 4 * func(x + h) + func(x + 2 * h)
            x += 2 * h

        return res * (h / 3)


    """ _________________________________________________________________________________ """


    @staticmethod
    def __getMainFuncLink(param):
        subfunc = lambda x, y: 2 * cos(x) / (1 - (sin(x) ** 2) * (cos(y) ** 2))
        func = lambda x, y: (4 / pi) * (1 - exp(-param * subfunc(x, y))) * cos(x) * sin(x)

        return func


    @staticmethod
    def __wrapperFunc2(func2, value):
        return lambda x: func2(value, x)


    def __integrate(self, func, limits, num_of_nodes, integrators):
        inner = lambda x: integrators[1](self.__wrapperFunc2(func, x), limits[1][0], limits[1][1], num_of_nodes[1])

        return integrators[0](inner, limits[0][0], limits[0][1], num_of_nodes[0])


    @staticmethod
    def __taoConstructor(integrate_func, ar_params, label):
        x, y = [], []

        for i in arange(ar_params[0], ar_params[1] + ar_params[2], ar_params[2]):
            x.append(i)
            y.append(integrate_func(i))

        plt.plot(x, y, label=label)


    def __getLabel(self, n, m, func1, func2):
        label = "N=" + str(n) + ", M=" + str(m) + "\nMethods="

        if func1 == self.simpson: label += "Simpson"
        else: label += "Gauss"

        if func2 == self.simpson: label += "--Simpson"
        else: label += "--Gauss"

        return label


    @staticmethod
    def drawData():
        plt.title("Graph")
        plt.legend()
        plt.ylabel("Result")
        plt.xlabel("Tao value")
        plt.show()


    def fillData(self):
        self.choice = 1

        while self.choice:
            N = int(input("N: "))
            M = int(input("M: "))
            param = float(input("Tao: "))

            mode = int(input("Select a method:\n1 - Simpson\n0 - Gauss\n"))
            if mode: func1 = self.simpson
            else: func1 = self.gauss

            mode = int(input())
            if mode: func2 = self.simpson
            else: func2 = self.gauss

            param_integrate = lambda tao: self.__integrate(self.__getMainFuncLink(tao), [[0, pi / 2], [0, pi / 2]], [N, M], [func1, func2])
            print("Result:", param_integrate(param))
            self.__taoConstructor(param_integrate, [0.05, 10, 0.05], self.__getLabel(N, M, func1, func2))

            self.choice = int(input("1 - Continue\n0 - End\n"))