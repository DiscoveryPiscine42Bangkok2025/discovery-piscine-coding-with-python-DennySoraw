array =  [2, 8, 9, 48, 8, 22,-12, 2]
new_array = []

for i in array:
    if i > 5:
        new_array.append(i + 2)

set_1 = set(array)
set_2 = set(new_array)
new_set = set.union(set_2)
print(new_set)
