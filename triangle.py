from figure import Figure


class Triangle (Figure):  # triangulo equilatero
    def __init__(self, base, high):
        self.base = base
        self.high = high

    def area(self):
        return self.base * self.high / 2

    def perimeter(self):
        return 3 * self.base

    def get_type(self):
        return 'Triangulo'
