"""
    main.py
"""


from class_numerical_differentiator import NumericalDifferentiator


def main():
    x = [1, 2, 3, 4, 5, 6]
    y = [0.571, 0.889, 1.091, 1.231, 1.333, 1.412]

    exe = NumericalDifferentiator(x, y)
    exe.printCompletedTable()


if __name__ == "__main__":
    main()