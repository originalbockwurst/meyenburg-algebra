class MeyenburgNumber:
    def __init__(self, real=0.0, imag=0.0):
        self.value = complex(real, imag)

    @staticmethod
    def from_real_or_zero(val):
        if val == 0:
            return MeyenburgNumber(0, 1)  # 0 wird zu i
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

x = float(input("Erste Zahl:"))
y = float(input("Zweite Zahl:"))
operation = input("Operation (Addition, etc...")

x = MeyenburgNumber.from_real_or_zero(x)
y = MeyenburgNumber.from_real_or_zero(y)

if operation == "Addition":
    result = x + y
elif operation == "Subtraktion":
    result = x - y
elif operation == "Multiplikation":
    result = x * y
elif operation == "Division":
    result = x / y

print(result)
