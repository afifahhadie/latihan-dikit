"""
CONTOH SOAL:
ada orang mau nabung sebesar 2 juta per bulan dengan bunga tahunan 3%.
buatlah program untuk menghitung berapa tahun yang dibutuhkan agar uangnya
mencapai minimal Rp100.000.000. Cetak tahun dan jumlah akhir.
"""

saldo = 0
target = 100_000_000
nabung_bulanan = 2_000_000
bunga_tahunan = 0.03
tahun = 0

while saldo < target:
    saldo += nabung_bulanan * 12
    saldo += saldo * bunga_tahunan
    tahun += 1

print(f"Membutuhkan {tahun} tahun untuk mencapai minimal Rp{target:,} dengan saldo akhir Rp{int(saldo):,}")