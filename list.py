list_number = [1, 10, 14, 20, 2, 7, 8, 90, 200, 2, 20]

for i in range(len(list_number)):
    if list_number[i] == 20:
        list_number[i] = 200
        break

for i in range(len(list_number)):
    if list_number[i] == 2:
        list_number[i] = 20

print(list_number)
