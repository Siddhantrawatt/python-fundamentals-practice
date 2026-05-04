class number():
    def __init__(self, num):
        self.num = num
num = int(input("Enter a number: "))
num_obj = number(num)
if num_obj.num % 2 == 0:
    print(num_obj.num, "is an even number.")
else:
    print(num_obj.num, "is an odd number.")
    