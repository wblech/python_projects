class Vector:
    def __init__(self, array):
        self.array = array
        self.__size()

    @property
    def array(self):
        return self._array

    @array.setter
    def array(self, value):
        self._array = []
        try:
            if type(value) == int and len(value) == 1:
                for n in range(value):
                    self._array.append(float(n))
            elif type(value) == tuple and len(value) == 2:
                for n in range(value[0], value[1]):
                    self._array.append(float(n))
            elif type(value) == list:
                for i, n in enumerate(value):
                    if type(n) != float and type(n) != int:
                        raise TypeError
                    elif type(n) is int:
                        value[i] = float(n)
                self._array = value
            else:
                raise ValueError
        except TypeError:
            print("Vector only accepts a floats or int")
        except ValueError:
            print(
                "To make an object use one of this options:\n.Vector()a list \
of floats: Vector([0.0, 1.0, 2.0, 3.0])\n.A size Vector(3) -> the vector will \
have values = [0.0, 1.0, 2.0]\n.A range or Vector((10,15)) -> the vector will \
have values = [10.0, 11.0, 12.0, 13.0, 14.0]")

    @property
    def size(self):
        return self._size

    def __size(self):
        self._size = len(self.array)

    def __add__(self, other):
        for i, n in enumerate(self.array):
            self._array[i] = n + other
        return self.array

    def __radd__(self, other):
        for i, n in enumerate(self.array):
            self._array[i] = n + other
        return self.array

    def __sub__(self, other):
        for i, n in enumerate(self.array):
            self._array[i] = n - other
        return self.array

    def __rsub__(self, other):
        for i, n in enumerate(self.array):
            self._array[i] = n - other
        return self.array

    def __truediv__(self, other):
        try:
            for i, n in enumerate(self.array):
                self._array[i] = n / other
        except ZeroDivisionError as e:
            print(e)
        else:
            return self.array

    def __rtruediv__(self, other):
        try:
            for i, n in enumerate(self.array):
                self._array[i] = n / other
        except ZeroDivisionError as e:
            print(e)
        else:
            return self.array

    def __mul__(self, other):
        for i, n in enumerate(self.array):
            self._array[i] = n * other
        return self.array

    def __rmul__(self, other):
        for i, n in enumerate(self.array):
            self._array[i] = n * other
        return self.array

    def __str__(self):
        msg = f"{self.array}"
        return msg
