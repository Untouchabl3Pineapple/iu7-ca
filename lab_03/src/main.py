from myio import read_data
from spline import Spline

def main():
    table = read_data("../data/table.txt")
    if table is None:
        exit(0)
 
    x = float(input("\nInput x: "))

    print("Spline: ", "{:.5f}".format(Spline(table).get_spline(x)))


if __name__ == "__main__":
    main()
    
