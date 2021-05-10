"""
    class_numerical_differentiator.py
"""


class NumericalDifferentiator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def __left(y, step, ind):
        return (y[ind] - y[ind - 1]) / step if ind > 0 else "%10s" % "null"

    @staticmethod
    def __center(y, step, ind):
        return (
            (y[ind + 1] - y[ind - 1]) / 2 / step
            if ind > 0 and ind < len(y) - 1
            else "%10s" % "null"
        )

    @staticmethod
    def __secondDiff(y, step, ind):
        return (
            (y[ind - 1] - 2 * y[ind] + y[ind + 1]) / step ** 2
            if ind > 0 and ind < len(y) - 1
            else "%10s" % "null"
        )

    @staticmethod
    def __alignCoeff(y, x, step, ind):
        if ind > len(y) - 2:
            return "%10s" % "null"

        res = (
            (1 / y[ind + 1] - 1 / y[ind])
            / (1 / x[ind + 1] - 1 / x[ind])
            * y[ind]
            * y[ind]
            / x[ind]
            / x[ind]
        )

        return res

    def __rungeLeft(self, y, step, ind):
        if ind < 2:
            return "%10s" % "null"

        f1 = self.__left(y, step, ind)
        f2 = (y[ind] - y[ind - 2]) / 2 / step

        return 2 * f1 - f2

    def __getMethodsLinks(self):
        return [
            self.__left,
            self.__center,
            self.__rungeLeft,
            self.__alignCoeff,
            self.__secondDiff,
        ]

    def printCompletedTable(self):
        methods_links = self.__getMethodsLinks()

        for i in range(len(self.x)):
            print("|", end="")

            for j in range(len(methods_links) - 2):
                res = methods_links[j](self.y, self.x[1] - self.x[0], i)
                print(
                    f"{res:10.5f}" if res != "%10s" % "null" else res,
                    "|",
                    sep="",
                    end="",
                )

            res = self.__alignCoeff(self.y, self.x, self.x[1] - self.x[0], i)
            print(
                f"{res:10.5f}" if res != "%10s" % "null" else res, "|", sep="", end=""
            )

            res = self.__secondDiff(self.y, self.x[1] - self.x[0], i)
            print(f"{res:10.5f}" if res != "%10s" % "null" else res, "|", sep="")
