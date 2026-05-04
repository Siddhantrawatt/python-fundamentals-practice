class addition():
    def __init__(self ,a,b):
        self.a = a
        self.b = b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

calc = addition(a, b)
print("The sum of", calc.a, "and", calc.b, "is", calc.a + calc.b)
