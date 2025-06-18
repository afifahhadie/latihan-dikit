# mengubah nilai dalam list dan hitung jumlah

data = [4, 6, 2, 6, 7, 6, 10]
for i in range(len(data)):
    if data[i] == 6:
        data[i] = 0
print("List setelah diubah:", data)
print("Total:", sum(data))
