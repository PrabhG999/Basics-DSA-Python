"""for i in range(1, 11):
    if i % 2 == 0:
        break
    print(i)"""

nums = [1, 2, 3, 4, 5, 7, 8, 9, 10]

for num in range(len(nums)):
    if num == 6:
        print(nums[num])
        break
    else:
        continue
