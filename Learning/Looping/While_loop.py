"""
Syntax

while (condition):
    #code
"""
import time

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

num = 0
length = len(nums)
print("The length of nums array is " + str(length))


while num <= length:
    time.sleep(5.00)
    print(num)
    num += 1
