'''
OOP és dunder példa
HUN: https://youtu.be/JfEy2w5OdiU
'''

class Unit:
    def __init__(self, value, unit):
        self._value = value
        self._unit = unit

    @property
    def value(self):
        return self._value

    def __int__(self):
        return int(self._value)
    
    def __float__(self):
        return float(self._value)

    def __complex__(self):
        return complex(self._value)

    def __str__(self) -> str:
        self._magnitude = abs(self._value)
        if self._magnitude > 0:
            if self._magnitude < 0.000000000000000001:
                return f"{self._value * 1000000000000000000000:.3f}z{self._unit}"
            elif self._magnitude < 0.000000000000001:
                return f"{self._value * 1000000000000000000:.3f}a{self._unit}"
            elif self._magnitude < 0.000000000001:
                return f"{self._value * 1000000000000000:.3f}f{self._unit}"
            elif self._magnitude < 0.000000001:
                return f"{self._value * 1000000000000:.3f}p{self._unit}"
            elif self._magnitude < 0.000001:
                return f"{self._value * 1000000000:.3f}n{self._unit}"
            elif self._magnitude < 0.001:
                return f"{self._value * 1000000:.3f}µ{self._unit}"
            elif self._magnitude < 1:
                return f"{self._value * 1000:.3f}m{self._unit}"
            elif self._magnitude < 1000:
                return f"{self._value:.3f}{self._unit}"
            elif self._magnitude < 1000000:
                return f"{self._value / 1000:.3f}k{self._unit}"
            elif self._magnitude < 1000000000:
                return f"{self._value / 1000000:.3f}M{self._unit}"
            elif self._magnitude < 1000000000000:
                return f"{self._value / 1000000000:.3f}G{self._unit}"
            elif self._magnitude < 1000000000000000:
                return f"{self._value / 1000000000000:.3f}T{self._unit}"
            elif self._magnitude < 1000000000000000000:
                return f"{self._value / 1000000000000000:.3f}P{self._unit}"
            else:
                return f"{self._value / 1000000000000000000:.0f}E{self._unit}"

class Current(Unit):
    def __init__(self, value):
         super().__init__(value, "A")

    def __add__(self, other):
        if type(other) == Current:
            return Current(self._value + other.value)
        elif type(other) == int or type(other) == float:
            return Current(self._value + other)

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if type(other) == Current:
            return Current(self._value - other.value)
        elif type(other) == int or type(other) == float:
            return Current(self._value - other)
    
    def __rsub__(self, other):
        if type(other) == Current:
            return Current(other.value - self._value)
        elif type(other) == int or type(other) == float:
            return Current(other - self._value)

    def __isub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        if type(other) == Voltage:
            return Power(self._value * other.value)
        elif type(other) == int or type(other) == float:
            return Current(self._value * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __imul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if type(other) == int or type(other) == float:
            return Current(self._value / other)

    def __rtruediv__(self, other):
        if type(other) == Power:
            return Voltage(other.value / self._value)

    def __itruediv__(self, other):
        return self.__truediv__(other)
    
    def __floordiv__(self, other):
        if type(other) == int or type(other) == float:
            return Current(self._value // other)
    
    def __ifloordiv__(self, other):
        return self.__floordiv__(other)

    def __rfloordiv__(self, other):
        if type(other) == Power:
            return Voltage(other.value // self._value)

class Voltage(Unit):
    def __init__(self, value):
        super().__init__(value, "V")

    def __add__(self, other):
        if type(other) == Voltage:
            return Voltage(self._value + other.value)
        elif type(other) == int or type(other) == float:
            return Voltage(self._value + other)

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if type(other) == Voltage:
            return Voltage(self._value - other.value)
        elif type(other) == int or type(other) == float:
            return Voltage(self._value - other)
    
    def __rsub__(self, other):
        if type(other) == Voltage:
            return Voltage(other.value - self._value)
        elif type(other) == int or type(other) == float:
            return Voltage(other - self._value)

    def __isub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        if type(other) == Current:
            return Power(self._value * other.value)
        elif type(other) == int or type(other) == float:
            return Voltage(self._value * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __imul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if type(other) == int or type(other) == float:
            return Voltage(self._value / other)

    def __rtruediv__(self, other):
        if type(other) == Power:
            return Current(other.value / self._value)

    def __itruediv__(self, other):
        return self.__truediv__(other)
    
    def __floordiv__(self, other):
        if type(other) == int or type(other) == float:
            return Voltage(self._value // other)
    
    def __ifloordiv__(self, other):
        return self.__floordiv__(other)

    def __rfloordiv__(self, other):
        if type(other) == Power:
            return Current(other.value // self._value)

class Power(Unit):
    def __init__(self, value):
        super().__init__(value, "W")


