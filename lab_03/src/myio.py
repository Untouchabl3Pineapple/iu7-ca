def read_data(filename):
    try:
        file = open(filename, "r")
    except:
        print("Invalid filename")
        return
    
    table = []
    x_arr = []
    y_arr = []
    
    for line in file:
        try:
            arr = [float(numb) for numb in line.split()]
    
            x_arr.append(arr[0])
            y_arr.append(arr[1])
        except:
            print("Invalid line data")
            file.close()
            return
    
    table.append(x_arr)
    table.append(y_arr)
    
    file.close()
    
    return table
