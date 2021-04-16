class Spline:
    def __init__(self, table):
        self.table = table
        self.x_arr = table[0]
        self.y_arr = table[1]
        self.size = len(self.y_arr)

    def __get_a_coeff(self):
        return self.y_arr[:-1]

    def __get_b_coeff(self, c_coeff):
        b_coeff = []
        
        for i in range(1, self.size - 1):
            h = self.x_arr[i] - self.x_arr[i - 1]
        
            b_cur = (self.y_arr[i] - self.y_arr[i - 1]) / h - (h * (c_coeff[i] + 2 * c_coeff[i - 1])) / 3
        
            b_coeff.append(b_cur)

        h = self.x_arr[self.size - 1] - self.x_arr[self.size - 2]
        b_coeff.append((self.y_arr[self.size - 1] - self.y_arr[self.size - 2]) / h - (h * 2 * c_coeff[i]) / 3)

        return b_coeff

    def __get_c_coeff(self):
        c_coeff = [0] * (self.size - 1)
        
        ksi_arr = [0, 0]
        teta_arr = [0, 0]
        
        for i in range(2, self.size):
            h1 = self.x_arr[i] - self.x_arr[i - 1]
            h2 = self.x_arr[i - 1] - self.x_arr[i - 2]
        
            fi = 3 * ((self.y_arr[i] - self.y_arr[i - 1]) / h1 - (self.y_arr[i - 1] - self.y_arr[i - 2]) / h2)
        
            ksi_cur = - h1 / (h2 * ksi_arr[i - 1] + 2 * (h2 + h1))
            teta_cur = (fi - h1 * teta_arr[i - 1]) / (h1 * ksi_arr[i - 1] + 2 * (h2 + h1))
        
            ksi_arr.append(ksi_cur)
            teta_arr.append(teta_cur)
        
        c_coeff[self.size - 2] = teta_arr[len(teta_arr) - 1]
        
        for i in range(self.size - 2, 0, -1):
            c_coeff[i - 1] = ksi_arr[i] * c_coeff[i] + teta_arr[i]

        return c_coeff

    def __get_d_coeff(self, c_coeff):
        d_coeff = []
        
        for i in range(1, len(self.x_arr) - 1):
            h = self.x_arr[i] - self.x_arr[i - 1]
        
            d_cur = (c_coeff[i] - c_coeff[i - 1]) / (3 * h)
        
            d_coeff.append(d_cur)
        
        h = self.x_arr[self.size - 1] - self.x_arr[self.size - 2]
        d_coeff.append((- c_coeff[i]) / (3 * h))

        return d_coeff

    def get_spline_coeffs(self): 
        a_coeff = self.__get_a_coeff()
        c_coeff = self.__get_c_coeff()
        b_coeff = self.__get_b_coeff(c_coeff)
        d_coeff = self.__get_d_coeff(c_coeff)

        return a_coeff, b_coeff, c_coeff, d_coeff

    def get_spline(self, x):
        coeffs = self.get_spline_coeffs()
        
        pos = 1
        while (pos < len(self.x_arr) and self.x_arr[pos] < x):
            pos += 1
        pos -= 1
        
        h = x - self.x_arr[pos]

        result = 0
        for i in range(len(coeffs)):
            result += coeffs[i][pos] * pow(h, i)
        
        return result   