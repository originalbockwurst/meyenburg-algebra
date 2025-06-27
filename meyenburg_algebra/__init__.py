class MeyenburgNumber:
    """
    Erweiterte Meyenburg-Algebra: 0 wird als i interpretiert.
    Multiplikation mit 0 ergibt i * x statt 0.
    """

    def __init__(self, real=0.0, imag=0.0):
        self.value = complex(real, imag)

    @staticmethod
    def from_real_or_zero(val):
        if val == 0:
            return MeyenburgNumber(0, 1)
        return MeyenburgNumber(val, 0)

    def __str__(self):
        return str(self.value)

    def __add__(self, other):
        result = self.value + other.value
        return MeyenburgNumber(result.real, result.imag)

    def __sub__(self, other):
        result = self.value - other.value
        return MeyenburgNumber(result.real, result.imag)

    def __truediv__(self, other):
        if other.value == 0:
            other = MeyenburgNumber(0, 1)
        result = self.value / other.value
        return MeyenburgNumber(result.real, result.imag)

    def __mul__(self, other):
        if self.value == 0:
            self = MeyenburgNumber(0, 1)
        if other.value == 0:
            other = MeyenburgNumber(0, 1)
        result = self.value * other.value
        return MeyenburgNumber(result.real, result.imag)
