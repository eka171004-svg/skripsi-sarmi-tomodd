# skripsi-sarmi-tomodd
Logbook dan kode skripsi relokasi gempa Sarmi
# Logbook Skripsi: Relokasi Hiposenter & Tomografi Sarmi 2022 (TomoDD)

**Status Saat Ini:** Tahap Setup Environment & Persiapan Data.
**Tujuan Akhir:** Mendapatkan model kecepatan 3D (Vp, Vs, Vp/Vs) dan hiposenter presisi untuk mengidentifikasi Sesar Mamberamo.

---

## Day 1: Setup Environment & GitHub
**Tanggal:** [Isi tanggal hari ini, misal: 24 Oktober 2026]

### Progress Hari Ini:
- [x] **Install Python:** Menggunakan Python Install Manager resmi. Mengaktifkan *Long Path Support* (fitur wajib untuk Windows agar tidak error saat path folder terlalu panjang).
- [x] **Install VS Code:** Sebagai *text editor* untuk menulis *script* Python. Menginstall ekstensi Python.
- [x] **Setup Workspace:** Membuat folder kerja `skripsi-sarmi-tomodd` yang terintegrasi dengan GitHub.
- [x] **Setup GitHub:** Membuat repository dan menghubungkannya dengan GitHub Desktop untuk *version control* (mencatat jejak *coding*).

### Analisis Awal Data:
Sebelum masuk ke *software* TomoDD (yang berbasis CLI/Linux), data mentah dari BMKG harus dibersihkan dulu menggunakan Python.
1. **Filter Tanggal:** Data `phase data.txt` masih berisi *event* dari tahun 2008-2021. Harus difilter **HANYA** untuk periode September 2022 (sesuai Bab 3 Skripsi).
2. **Kualitas Data:** Ada beberapa data fase dengan nilai waktu tempuh `0.000` atau tipe fase `Pg`, `Sg`, `Pn`. Ini harus di-*handling* agar tidak *error* saat masuk TomoDD.
3. **Elevasi Stasiun:** File `station data.txt` dari BMKG hanya berisi Latitude dan Longitude. Software TomoDD **membutuhkan Elevasi**. Nanti kita harus mencari data elevasi 26 stasiun tersebut.

### Next Step:
- Membuat *script* Python (`cleaning.py`) untuk memfilter data `phase data.txt` khusus periode September 2022.