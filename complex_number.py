class Complex:
    def __init__(self, real_part=0, imaginer_part=0):
        self.real = real_part
        self.imaginer = imaginer_part

    @staticmethod
    def add(a, b):
        real = a.real + b.real
        imaginer = a.imaginer + b.imaginer
        return Complex(real, imaginer)

    @staticmethod
    def sub(a, b):
        real = a.real - b.real
        imaginer = a.imaginer - b.imaginer
        return Complex(real, imaginer)

    @staticmethod
    def mult(a, b):
        real = a.real * b.real - a.imaginer * b.imaginer
        imaginer = a.imaginer * b.real + a.real * b.imaginer
        return Complex(real, imaginer)
