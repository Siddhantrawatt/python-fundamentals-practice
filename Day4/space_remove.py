s = input("Enter a string: ")
no_space = ""
for ch in s :
    if ch != " ":
        no_space += ch
print("String without spaces:", no_space)