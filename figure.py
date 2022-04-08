from abc import ABC, abstractclassmethod


class Figure(ABC):  # con (ABC)  decimos que la clase es abstracta
    @abstractclassmethod
    def area(self):
        pass

    @abstractclassmethod
    def perimeter(self):
        pass

    @abstractclassmethod
    def get_type(self):
        pass

    def greet(self):
        print('Hola, soy un '+self.get_type())
