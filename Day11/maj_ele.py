nums = [3, 3, 4, 2, 3, 3, 5]

freq = {}

for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

n = len(nums)

for key in freq:
    if freq[key] > n // 2:
        print(key)