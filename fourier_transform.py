from complex_number import Complex
import numpy as np
import math

def __fft(a, inverse=False):
    n = len(a)
    if n == 1:
        return a

    w = []
    sin_alpha = lambda x: -math.sin(x) if inverse else math.sin(alpha)
    for i in range(n):
        alpha = 2 * math.pi * i / n
        w.append(Complex(math.cos(alpha), sin_alpha(alpha)))

    even_part = []
    odd_part = []
    for i in range(n // 2):
        even_part.append(a[i * 2])
        odd_part.append(a[i * 2 + 1])

    even_part = __fft(even_part, inverse)
    odd_part = __fft(odd_part, inverse)

    result = []
    for k in range(n // 2):
        temp = Complex.mult(w[k], odd_part[k])
        result.insert(k, Complex.add(even_part[k], temp))
        result.append(Complex.sub(even_part[k], temp))
    return result

def transform(a):
    b = [Complex(i) for i in a]
    return __fft(b)

def inverse(a):
    result = []
    n = len(a)
    for i in __fft(a, inverse=True):
        result.append(i.real/ n)
    return result
