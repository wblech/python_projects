class Vector:

    def __init__(self, values):
        self.values = values

    @staticmethod
    def itol(value):
        i = 0
        ret = []
        while i < value:
            ret.append(float(i))
            i += 1
        return ret

    @staticmethod
    def ttol(value):
        ret = []
        for i in range(value[0], value[1]):
            ret.append(float(i))
        return ret

    @staticmethod
    def is_float_list(value):
        for nbr in value:
            if not(isinstance(nbr, float)):
                return False
        return True

    @property
    def values(self):
        return self._values

    @property
    def size(self):
        return len(self._values)

    @values.setter
    def values(self, value):
        try:
            if not value:
                raise ValueError
            elif isinstance(value, int):
                self._values = self.itol(value)
            elif isinstance(value, tuple):
                self._values = self.ttol(value)
            elif isinstance(value, list):
                if not(self.is_float_list(value)):
                    raise TypeError
                self._values = value
            else:
                raise TypeError
        except ValueError:
            print("Error:\nNo argument found")
        except TypeError:
            print("Error:\n\
You should be able to initialize the object with:\n\
• a list of floats: Vector([0.0, 1.0, 2.0, 3.0])\n\
• a size Vector(3) -> the vector will have values = [0.0, 1.0, 2.0]\n\
• a range or Vector((10,15)) -> the vector will have values = [10.0, 11.0, \
12.0, 13.0, 14.0]\
                ")

    def __str__(self):
        txt = f"Vector {self.values}"
        return txt

    def __add__(self, other):
        ret = []
        try:
            if not(isinstance(other, (Vector, int, float))):
                raise TypeError
            elif isinstance(other, Vector):
                if self.size != other.size:
                    raise ValueError
                for i in range(0, self.size):
                    ret.append(self.values[i] + other.values[i])
            else:
                for t in range(0, self.size):
                    ret.append(self.values[t] + other)
        except TypeError:
            print("Error:\nVector instance can only be sum with another \
Vector instance or with a scalar(int, float)")
        except ValueError:
            print("Error:\nVector instance can only be sum with the same \
dimension")
        return ret

    def __radd__(self, other):
        ret = []
        try:
            if not(isinstance(other, (int, float))):
                raise TypeError
            else:
                for t in range(0, self.size):
                    ret.append(self.values[t] + other)
        except TypeError:
            print("Error:\nVector instance can only be sum with another \
Vector instance or with a scalar(int, float)")
        return ret

    def __sub__(self, other):
        ret = []
        try:
            if not(isinstance(other, (Vector, int, float))):
                raise TypeError
            elif isinstance(other, Vector):
                if self.size != other.size:
                    raise ValueError
                for i in range(0, self.size):
                    ret.append(self.values[i] - other.values[i])
            else:
                for t in range(0, self.size):
                    ret.append(self.values[t] - other)
        except TypeError:
            print("Error:\nVector instance can only be sub with another \
Vector instance or with a scalar(int, float)")
        except ValueError:
            print("Error:\nVector instance can only be sub with the same \
dimension")
        return ret

    def __rsub__(self, other):
        ret = []
        try:
            if not(isinstance(other, (int, float))):
                raise TypeError
            else:
                for t in range(0, self.size):
                    ret.append(self.values[t] - other)
        except TypeError:
            print("Error:\nVector instance can only be sub with another \
Vector instance or with a scalar(int, float)")
        return ret

    def __truediv__(self, other):
        ret = []
        try:
            if not(isinstance(other, (int, float))):
                raise TypeError
            else:
                for t in range(0, self.size):
                    ret.append(self.values[t] / other)
        except TypeError:
            print("Error:\nVector instance can only be div with a \
scalar(int, float)")
        return ret

    def __rtruediv__(self, other):
        ret = []
        try:
            if not(isinstance(other, (int, float))):
                raise TypeError
            else:
                for t in range(0, self.size):
                    ret.append(self.values[t] / other)
        except TypeError:
            print("Error:\nVector instance can only be div with a \
scalar(int, float)")
        return ret

    def __mul__(self, other):
        try:
            if not(isinstance(other, (Vector, int, float))):
                raise TypeError
            elif isinstance(other, Vector):
                ret = 0
                if self.size != other.size:
                    raise ValueError
                for i in range(0, self.size):
                    ret += self.values[i] * other.values[i]
            else:
                ret = []
                for t in range(0, self.size):
                    ret.append(self.values[t] * other)
        except TypeError:
            print("Error:\nVector instance can only be multiplication \
with another Vector instance or with a scalar(int, float)")
        except ValueError:
            print("Error:\nVector instance can only be multiplicated with \
the same dimension")
        return ret

    def __rmul__(self, other):
        ret = []
        try:
            if not(isinstance(other, (int, float))):
                raise TypeError
            else:
                for t in range(0, self.size):
                    ret.append(self.values[t] * other)
        except TypeError:
            print("Error:\nVector instance can only be multiplicated with \
another Vector instance or with a scalar(int, float)")
        return ret
