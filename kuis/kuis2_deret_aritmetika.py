
# Kuis 2: Deret Aritmetika
# Input: suku pertama a, beda d, dan banyak suku n.
# Proses: menghasilkan suku dengan for dan menjumlahkannya.
# Kondisi berhenti: n valid dan perulangan selesai sebanyak n kali.
# Output: nomor suku, nilai setiap suku, dan jumlah seluruh suku.

print("Deret Aritmetika")

a = float(input("Suku pertama a: "))
d = float(input("Beda d: "))
n = int(input("Banyak suku n: "))

while n <= 0:
    print("Banyak suku harus bilangan positif!")
    n = int(input("Banyak suku n: "))

total = 0

for i in range(n):
    suku = a + i * d
    total += suku
    print(f"Suku ke-{i + 1} = {suku:g}")

print(f"Jumlah deret = {total:.2f}")
