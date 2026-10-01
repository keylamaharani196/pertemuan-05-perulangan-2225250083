
# Latihan 3: Validasi Input
# Input: nilai ujian antara 0 sampai 100.
# Proses: memeriksa apakah nilai berada di luar rentang.
# Kondisi berhenti: nilai sudah berada dalam rentang 0-100.
# Output: pesan penolakan atau nilai yang diterima.

nilai = float(input("Nilai 0-100: "))

while nilai < 0 or nilai > 100:
    print("Nilai tidak valid.")
    nilai = float(input("Nilai 0-100: "))

print(f"Nilai diterima: {nilai}")
