import fourier_transform as ft
from complex_number import Complex

a = [
    Complex(0.11),
    Complex(0.22),
    Complex(0.33),
    Complex(0.44),
    Complex(0.55),
    Complex(0.66),
    Complex(0.77),
    Complex(0.88)
    ]
b = ft.inverse(ft.transform(a))
for x in b:
    print(x.real, x.imaginer)
