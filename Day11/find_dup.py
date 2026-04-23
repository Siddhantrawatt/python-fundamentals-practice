nums = [1, 2, 3, 1, 2, 4, 5]

freq = {}
result = []

for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

for key in freq:
    if freq[key] > 1:
        result.append(key)

print(result)