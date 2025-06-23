# Belanja buah pake dictionary

harga_buah = {
    "apel": 5000,
    "jeruk": 7000,
    "mangga": 10000
}
total = 0
for i in range(3):
    buah = input(f"Masukkan buah ke-{i+1}: ").lower()
    jumlah = int(input(f"Jumlah {buah}: "))
    if buah in harga_buah:
        total += harga_buah[buah] * jumlah
    else:
        print(f"Buah {buah} tidak tersedia!")
print("Total belanja: Rp" + str(total))