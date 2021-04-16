"""
    main.py
"""

from square_approx import RootMeanSquareApproximation


def main():
    app = RootMeanSquareApproximation()

    while True:
        app.print_menu()

        try:
            option = int(input("\n\nInput the menu command: "))
        except:
            print("\n\nInvalid command\n\n")
            continue

        if option == 0:
            break
        elif option == 1:
            app.print_table()
        elif option == 2:
            app.change_weight()
        elif option == 3:
            app.draw()


if __name__ == "__main__":
    main()
