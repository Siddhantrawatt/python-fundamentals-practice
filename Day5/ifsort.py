nums = list(map(int, input("Enter numbers: ").split()))
sort_num = sorted(nums)

if nums == sort_num:
    print("The numbers are in sorted")
else:
    print("The numbers are not sorted.")
