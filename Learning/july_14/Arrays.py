array = [1, 2, 3, 4, 5]

array.append(6)
print(array)

array.insert(6, 7)
print(array)

array_2 = [1, 2, 3, 4, 5]


def check(array_2):
    exist = 7 in array_2
    return True if exist else False


def check2(array_2):
    result = check(array_2)
    print(result)

check2(array_2)

index = array_2.index(2)
print(index)
array_2.remove(1)
print(array_2)

del array_2[2]
print(array_2)

for i in array_2:
    print(i)
