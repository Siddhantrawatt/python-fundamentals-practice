nums = list(map(int, input("Enter numbers: ").split()))

largest = nums[0]
second = nums[0]

for num in nums:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print("Second largest:", second)