from vector import Vector


class Matrix:

    def __init__(self, data, shape=None):
        self.data = data
        self.shape = shape

    @staticmethod
    def is_matrix(matrix):
        if not(isinstance(matrix, list)):
            return False
        for i, value in enumerate(matrix):
            if not(value[i], list):
                return False
        return True

    @staticmethod
    def __shape_to_data(value):
        ret = []
        nbr = 0.0
        for row in range(value[0]):
            ret.append([])
            for col in range(value[1]):
                ret[row].append(nbr)
        return ret

    @staticmethod
    def __count_data(value):
        row = len(value)
        col = len(value[0])
        return (row, col)

    @property
    def data(self):
        return self._data

    @property
    def shape(self):
        return self._shape

    @data.setter
    def data(self, value):
        try:
            if not value:
                raise ValueError
            elif not(isinstance(value, tuple)):
                if not(self.is_matrix(value)):
                    raise TypeError
                else:
                    self._data = value
            elif isinstance(value, tuple):
                self._data = self.__shape_to_data(value)
                self.shape = value
        except ValueError:
            print("valueerror")
        except TypeError:
            print("typeerror")

    @shape.setter
    def shape(self, value):
        try:
            if value is None:
                self._shape = self.__count_data(self.data)
            elif not(isinstance(value, tuple)):
                raise TypeError
            elif len(value) > 2:
                raise ValueError
            else:
                self._shape = value
        except TypeError:
            print("typeerror")
        except ValueError:
            print("valueerror")

    def __str__(self):
        txt = f"Matrix: {self.data}"
        return txt

#     def __mul__(self, other):
#         try:
#             if isinstance(other, Vector):
#                 return self.__calc_mul_vector(other)
#             elif isinstance(other, Matrix):
#                 return self.__calc_mul_matrix(other)
#             elif isinstance(other, (int, float)):
#                 return self.__calc_mul_scalar(other)
#             else:
#                 raise TypeError
#         except TypeError:
#             print("Error:\nMatriz can be multiplied by vector, matrix or \
# scalar(int, float)")

    def __calc_add_matrix(self, other):
        new_matrix = []
        for i in range(0, self.shape[0]):
            new_matrix.append([])
            for t in range(0, self.shape[1]):
                new_matrix[i].append(self.data[i][t] + other.data[i][t])
        return new_matrix

    def __calc_sub_matrix(self, other):
        new_matrix = []
        for i in range(0, self.shape[0]):
            new_matrix.append([])
            for t in range(0, self.shape[1]):
                new_matrix[i].append(self.data[i][t] - other.data[i][t])
        return new_matrix

    def __calc_truediv_matrix(self, other):
        new_matrix = []
        for i in range(0, self.shape[0]):
            new_matrix.append([])
            for t in range(0, self.shape[1]):
                new_matrix[i].append(self.data[i][t] / other)
        return new_matrix

    def __add__(self, other):
        try:
            if not isinstance(other, Matrix):
                raise TypeError
            if self.shape[0] != other.shape[0] or self.shape[1] != other.shape[1]:
                raise ValueError
            else:
                return self.__calc_add_matrix(other)
        except TypeError:
            print("Error:\nOnly matrix can be add with other matrix")
        except ValueError:
            print("Error:\nThe matrix must have the same dimension")

    def __sub__(self, other):
        try:
            if not isinstance(other, Matrix):
                raise TypeError
            if self.shape[0] != other.shape[0] or self.shape[1] != other.shape[1]:
                raise ValueError
            else:
                return self.__calc_sub_matrix(other)
        except TypeError:
            print("Error:\nOnly matrix can be sub with other matrix")
        except ValueError:
            print("Error:\nThe matrix must have the same dimension")

    def __truediv__(self, other):
        try:
            if not isinstance(other, (int, float)):
                raise TypeError
            else:
                return self.__calc_truediv_matrix(other)
        except TypeError:
            print("Error:\nOnly scalar can be use to divide a Matrix.")
        except ValueError:
            print("Error:\nThe matrix must have the same dimension")

    def __rtruediv__(self, other):
        try:
            if not isinstance(other, (int, float)):
                raise TypeError
            else:
                return self.__calc_truediv_matrix(other)
        except TypeError:
            print("Error:\nOnly scalar can be use to divide a Matrix.")
        except ValueError:
            print("Error:\nThe matrix must have the same dimension")


matrix = Matrix([[0.0, 1.0, 2.0, 3.0], [4.0, 5.0, 6.0, 7.0]])
matrix_add = Matrix([[0.0, 1.0, 2.0, 3.0], [4.0, 5.0, 6.0, 7.0]])
print("Matrix1", matrix)
print(matrix.shape)
matrix2 = Matrix((3, 3))
print("Matrix2", matrix2)
print(matrix2.shape)
matrix3 = Matrix([[0.0, 1.0, 2.0], [3.0, 4.0, 5.0], [6.0, 7.0, 8.0]], (3, 3))
print("Matrix3", matrix3)
print(matrix3.shape)
print("")
print("SUM")
matrix_sum = Matrix(matrix + matrix_add)
print(matrix_sum)

print("SUB")
matrix_sub = Matrix(matrix - matrix_add)
print(matrix_sub)

print("DIV")
matrix_div = Matrix(matrix / 2)
print(matrix_div)
vector = Vector(5)
