import typing

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    
    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real + other.real, self.imaginary + other.imaginary)

        elif isinstance(other, (int, float)):
            return Complex(self.real + other, self.imaginary)
        
        else:
            raise TypeError("Invalid operation '+' for class '{self.__class__.__name__}' and '{other.__class__.__name__}")
     

def complex(real, imaginary) -> Complex:
    return Complex(real, imaginary)