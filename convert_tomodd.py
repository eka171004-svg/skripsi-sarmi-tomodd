# Script 2 (Revisi): Konversi cerdas ke format TomoDD (dengan Event ID)
input_file = "phase_september2022.txt"
output_phase = "phase.dat"   # File input fase untuk TomoDD
output_event = "event.dat"   # File koordinat event untuk TomoDD

print("Mulai konversi cerdas ke format TomoDD...")

event_id = 0 # Mulai dari event pertama

with open(input_file, 'r') as f_in, open(output_phase, 'w') as f_phase, open(output_event, 'w') as f_event:
    
    for line in f_in:
        line = line.strip() # Hapus spasi di ujung kiri/kanan
        
        # Kalau baris kosong, skip
        if not line:
            continue
            
        # Kalau baris adalah Event Header (ditandai '#')
        if line.startswith('#'):
            event_id += 1 # Tambah ID event setiap ketemu tanda '#'
            
            # Format baris: # 2022 09 11 20 14 30.686   -2.2400   138.2300   10.00 4.49 ...
            parts = line.split()
            
            # Ekstrak data koordinat untuk file event.dat
            # Format event.dat standar TomoDD: EventID Lat Lon Depth Mag
            lat = parts[5]
            lon = parts[6]
            depth = parts[7]
            mag = parts[9]
            
            # Tulis ke event.dat
            f_event.write(f"{event_id} {lat} {lon} {depth} {mag}\n")
            
        # Kalau baris adalah data stasiun (bukan '#')
        else:
            parts = line.split()
            # Cek apakah baris data valid (minimal 4 kolom)
            if len(parts) >= 4:
                station = parts[0]
                travel_time = parts[1]
                weight = float(parts[2])
                phase = parts[3]
                
                # ATURAN 1: Buang jika weight = 0.000 (data sampah)
                if weight == 0.0:
                    continue
                
                # ATURAN 2: Cuma terima fase P atau S murni (abaikan Pg/Sg/Pn)
                if phase not in ['P', 'S']:
                    continue
                
                # Tulis ke phase.dat dengan format TomoDD:
                # Stasiun  TravelTime  Weight  Phase  EventID
                f_phase.write(f"{station:<5} {travel_time:>8} {weight:>5.3f}  {phase:<2} {event_id:>4}\n")

print(f"Selesai! Berhasil memproses {event_id} event.")
print("File 'phase.dat' dan 'event.dat' sudah siap.")