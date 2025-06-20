# bikin segitiga terbalik

n = int(input("Masukkan angka untuk segitiga: "))
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()