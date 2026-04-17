nums = list(map(int, input("Enter numbers: ").split()))

n = len(nums)+1

total = n * (n+1) // 2
actual = sum(nums)

print("Missing number:", total - actual)