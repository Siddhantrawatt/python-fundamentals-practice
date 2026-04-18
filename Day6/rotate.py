nums = list(map(int, input("Enter numbers: ").split()))
k = int(input("Enter k: "))

k = k % len(nums)

result = nums[-k:] + nums[:-k]

print(result)