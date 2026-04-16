s = input("Enter a string: ")
letter = 0
digit = 0
special = 0
for ch in s:
    if ch.isalpha():
        letter += 1
    elif ch.isdigit():
        digit += 1
    else:
        special += 1
print("Letters:", letter)
print("Digits:", digit)
print("Special characters:", special)