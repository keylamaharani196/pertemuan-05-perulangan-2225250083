# Pertemuan 05 Perulangan Python

**Nama:** Keyla Maharani
**NIM:** 2225250083
**Kelas:** 3E

## Tujuan

Tujuan dari praktikum Pertemuan 05 adalah memahami dan menggunakan perulangan `for` dan `while` dalam Python untuk menyelesaikan masalah secara berulang. Praktikum ini juga melatih penggunaan validasi input, penghitungan menggunakan akumulator, serta pengujian program untuk memastikan hasil sesuai dengan yang diharapkan.

## Cara Menjalankan

Program dijalankan melalui terminal VS Code dengan perintah berikut:

**Latihan 1: Tabel Perkalian**

```bash
python3 latihan/01_tabel_perkalian.py
```

**Latihan 2: Jumlah 1 sampai n**

```bash
python3 latihan/02_jumlah_bilangan.py
```

**Latihan 3: Validasi Input**

```bash
python3 latihan/03_validasi_input.py
```

**Latihan 4: Menghitung Bilangan Genap**

```bash
python3 latihan/04_hitung_genap.py
```

**Kuis 2: Deret Aritmetika**

```bash
python3 kuis/kuis2_deret_aritmetika.py
```

## Algoritma Kuis 2

1. Menampilkan judul program Deret Aritmetika.
2. Memasukkan suku pertama `a` dan beda `d` sebagai bilangan desimal.
3. Memasukkan banyak suku `n` sebagai bilangan bulat.
4. Memeriksa nilai `n` menggunakan `while`. Jika `n` kurang dari atau sama dengan nol, program meminta input ulang sampai mendapatkan nilai positif.
5. Menginisialisasi variabel `total = 0` sebelum perulangan dimulai.
6. Menggunakan `for` untuk mengulang sebanyak `n` kali.
7. Menghitung setiap suku dengan rumus `suku = a + i * d`.
8. Menambahkan setiap suku ke variabel `total` dan menampilkan nomor serta nilai suku.
9. Setelah perulangan selesai, menampilkan jumlah seluruh suku dengan dua angka di belakang koma.

## Hasil Pengujian

### Test Case 1

* Input: a = 2, d = 3, n = 5.
* Keluaran yang diharapkan: 2, 5, 8, 11, 14.
* Keluaran aktual: 2, 5, 8, 11, 14.
* Jumlah yang diharapkan: 40.00.
* Jumlah aktual: 40.00.
* Status: Berhasil.

### Test Case 2

* Input: a = 10, d = -2, n = 4.
* Keluaran yang diharapkan: 10, 8, 6, 4.
* Keluaran aktual: 10, 8, 6, 4.
* Jumlah yang diharapkan: 28.00.
* Jumlah aktual: 28.00.
* Status: Berhasil.

### Test Case 3

* Input: a = 1.5, d = 0.5, n = 3.
* Keluaran yang diharapkan: 1.5, 2.0, 2.5.
* Keluaran aktual: 1.5, 2, 2.5.
* Jumlah yang diharapkan: 6.00.
* Jumlah aktual: 6.00.
* Status: Berhasil.

### Test Validasi Input

* Input n: 0, kemudian -2, lalu 3.
* Keluaran yang diharapkan: Nilai 0 dan -2 ditolak, sedangkan 3 diterima.
* Keluaran aktual: Diisi sesuai hasil pengujian program.
* Status: Diisi setelah pengujian.

## Refleksi

Salah satu kesalahan yang dapat terjadi pada perulangan adalah menginisialisasi variabel `total = 0` di dalam loop. Kesalahan ini menyebabkan nilai total kembali menjadi nol pada setiap pengulangan sehingga jumlah seluruh suku tidak terkumpul dengan benar.

Cara memperbaikinya adalah meletakkan `total = 0` sebelum perulangan dimulai. Dengan demikian, setiap suku dapat ditambahkan ke nilai total sebelumnya sampai seluruh suku selesai diproses.

## Refleksi Teknis

**1. Bagian mana yang menentukan jumlah iterasi?**

Jumlah iterasi ditentukan oleh `range(n)` pada perulangan `for`. Perulangan tersebut dijalankan sebanyak `n` kali.

**2. Mengapa total harus diinisialisasi sebelum loop?**

Agar variabel `total` memiliki nilai awal nol sebelum proses penjumlahan dimulai.

**3. Apa akibatnya jika `total = 0` ditempatkan di dalam loop?**

Nilai total akan kembali menjadi nol pada setiap pengulangan sehingga hasil penjumlahan menjadi salah.

**4. Mengapa validasi n lebih sesuai menggunakan while?**

Karena `while` dapat meminta input berulang kali selama nilai `n` belum positif dan berhenti ketika kondisi sudah terpenuhi.

**5. Bagaimana Anda membuktikan bahwa loop berhenti tepat?**

Dengan memeriksa bahwa `range(n)` menghasilkan indeks dari 0 sampai `n - 1`, sehingga perulangan berlangsung tepat sebanyak `n` kali.
