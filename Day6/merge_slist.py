a = list(map(int, input("Enter first sorted list: ").split()))
b = list(map(int, input("Enter second sorted list: ").split()))

i = 0
j = 0
result = []

while i < len(a) and j < len(b):
    if a[i] < b[j]:
        result.append(a[i])
        i += 1
    else:
        result.append(b[j])
        j += 1

while i < len(a):
    result.append(a[i])
    i += 1

while j < len(b):
    result.append(b[j])
    j += 1

print(result)