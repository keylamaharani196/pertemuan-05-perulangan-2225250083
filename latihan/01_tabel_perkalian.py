
# Latihan 1: Tabel Perkalian
# Input: satu bilangan bulat n.
# Proses: mengalikan n dengan angka 1 sampai 10.
# Kondisi berhenti: perulangan selesai saat i mencapai 10.
# Output: tabel perkalian sebanyak 10 baris.

n = int(input("Bilangan: "))

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
    