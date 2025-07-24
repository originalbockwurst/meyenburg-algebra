import math
import cmath

class MeyenburgNumber:
    def __init__(self, real: int, imag: int = 0, substituted=False, non_recursive=False):
        self.real = real & 0xF
        self.imag = imag & 0xF
        self.substituted = substituted
        self.non_recursive = non_recursive

    def __repr__(self):
        flags = []
        if self.substituted:
            flags.append("SUB")
        if self.non_recursive:
            flags.append("NONREC")
        flag_str = f" [{'|'.join(flags)}]" if flags else ""
        return f"<MeyenburgNumber {self.real}+{self.imag}i{flag_str}>"

    def multiply(self, other):
        a_real = self.real if self.real != 0 or self.substituted or self.non_recursive else 0
        a_imag = self.imag if self.imag != 0 else (1 if not self.substituted and self.real == 0 else self.imag)
        b_real = other.real if other.real != 0 or other.substituted or other.non_recursive else 0
        b_imag = other.imag if other.imag != 0 else (1 if not other.substituted and other.real == 0 else other.imag)

        real_part = (a_real * b_real - a_imag * b_imag) & 0xF
        imag_part = (a_real * b_imag + a_imag * b_real) & 0xF

        new_sub = self.substituted or other.substituted or (self.real == 0 and other.real == 0)
        return MeyenburgNumber(real_part, imag_part, substituted=new_sub, non_recursive=True)

    def to_tuple(self):
        return (self.real, self.imag, self.substituted, self.non_recursive)

    def log_derivative(self, epsilon=1e-6):
        x = complex(self.real, self.imag)
        x_perturbed = x + complex(0, epsilon)
        try:
            df = (cmath.log(x_perturbed) - cmath.log(x)) / (1j * epsilon)
            return df
        except:
            return complex(float('nan'), float('nan'))