import streamlit as st

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

# Streamlit UI
st.title("Meyenburg-Algebra Webdemo")
st.markdown("**Alternative Arithmetik:** `0 → i`, Division durch Null erlaubt und wohldefiniert.")

a = st.number_input("Erste Zahl (a)", value=1.0)
b = st.number_input("Zweite Zahl (b)", value=0.0)
operation = st.selectbox("Operation", ["Addition", "Subtraktion", "Multiplikation", "Division"])

x = MeyenburgNumber.from_real_or_zero(a)
y = MeyenburgNumber.from_real_or_zero(b)

if operation == "Addition":
    result = x + y
elif operation == "Subtraktion":
    result = x - y
elif operation == "Multiplikation":
    result = x * y
elif operation == "Division":
    result = x / y

st.markdown(f"**Ergebnis:** `{result}`")
