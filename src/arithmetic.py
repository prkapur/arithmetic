class Arithmetic():
    """ A Class for simple math operations """
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        """ Adding two variables """
        self.add = self.a + self.b
        return self.add

    def subtraction(self):
        """ Subtracting two variables """
        self.sub = self.a - self.b
        return self.sub
    
    def multiplication(self):
        """ Multiplying two variables """
        self.mul = self.a * self.b
        return self.mul

    def division(self):
        """ Dividing two variables """
        try:
            self.div = self.a / self.b
            return self.div
        except ZeroDivisionError:
            pass
        
if __name__ == "__main__":
    arith = Arithmetic(3,5)
    print(f"Add:{arith.addition()}")
    print(f"Sub:{arith.subtraction()}")
    print(f"Mul:{arith.multiplication()}")
    print(f"Div:{arith.division()}")
