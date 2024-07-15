from Arrays_practice1 import array

print(array)


def check (array):
    return 4 in array

print(check(array))
count = array.count(4)
print(count)
array.remove(3)
print(array)
squared = [x**2 for x in array]
print(squared)