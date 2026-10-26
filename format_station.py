# Script 3: Format file stasiun untuk TomoDD
input_file = "station data.txt"
output_file = "station.dat"

print("Memproses data stasiun...")

with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
    for line in f_in:
        line = line.strip()
        if not line:
            continue
            
        # Pisahkan berdasarkan spasi
        parts = line.split()
        
        # Pastikan ada minimal 3 kolom (Nama, Lat, Lon)
        if len(parts) >= 3:
            nama = parts[0]
            lat = parts[1]
            lon = parts[2]
            
            # Format TomoDD standar: Nama Lat Lon Elevasi
            # Kita asumsikan elevasi 0.0 km untuk awal
            elevasi = "0.0" 
            
            f_out.write(f"{nama:<5} {lat:>8} {lon:>9} {elevasi:>5}\n")

print("Selesai! File 'station.dat' berhasil dibuat.")