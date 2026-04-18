nums = list(map(int, input("Enter numbers: ").split()))

result = []
for num in nums:
    if num not in result:
        result.append(num)

print(result)