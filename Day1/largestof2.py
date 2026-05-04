class largest():
    def __init__(self, a, b):
        self.a = a
        self.b = b
        larger = a if a > b else b
        self.larger = larger
        
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

calc = largest(a, b)
print("Largest is:", calc.larger)