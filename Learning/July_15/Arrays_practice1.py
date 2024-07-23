array = [1, 2, 3, 4, 5]
print(array)

array.append(6)
print(array)

array.insert(0, 0)
print(array)

print(array.index(2))
array[1] = 12
print(array)
print(len(array))

print(array[:3])  # print first three
for i in range(len(array) - 4):  # print First Three using a loop
    print(array[i])

for element in array:
    print(element)

