a = list(map(int, input("Enter first list: ").split()))
b = list(map(int, input("Enter second list: ").split()))

common = []

for num in a:
    if num in b and num not in common:
        common.append(num)

print(common)