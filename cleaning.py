# Script 1: Filter data fase gempa (Hanya ambil periode September 2022)
input_file = "phase data.txt"
output_file = "phase_september2022.txt"

print("Mulai membaca data fase dari BMKG...")

# Membuka file input (read) dan file output (write)
with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
    simpan_event = False
    total_event_disimpan = 0
    
    for line in f_in:
        # Mengecek baris event (ditandai dengan '#')
        if line.startswith('#'):
            # Cek apakah tahun 2022 dan bulan 09 (September)
            # Format data lo: # 2022 09 11 ...
            if "2022 09" in line:
                simpan_event = True
                total_event_disimpan += 1
            else:
                simpan_event = False # Kalau bukan Sept 2022, abaikan event ini dan stasiunnya
                
        # Kalau eventnya masuk kriteria, tulis baris event '#' dan baris stasiun di bawahnya
        if simpan_event:
            f_out.write(line)

print(f"Selesai! Berhasil menyimpan {total_event_disimpan} event ke file '{output_file}'.")