str1 = input("Enter a string: ")
vow = 'aeiouAEIOU'
count = 0
for i in str1:
    if i in vow :
        count += 1
print("Number of vowels in the string: ", count)
