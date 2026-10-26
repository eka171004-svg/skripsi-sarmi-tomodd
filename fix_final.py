# Script PALING FINAL: Baca file yang udah bersih
input_file = "phase_september2022.txt"  # Ini file yang lo tunjukin udah bener
output_event = "event_final.dat"
output_phase = "phase_final.dat"

with open(input_file, 'r') as f_in, open(output_event, 'w') as f_ev, open(output_phase, 'w') as f_ph:
    event_id = 0
    for line in f_in:
        line = line.strip()
        if not line:
            continue
        
        if line.startswith('#'):
            event_id += 1
            parts = line.split()
            # Di file phase_september2022.txt, index Lat/Lon-nya beda!
            # Format: # 2022 09 11 20 14 30.686 -2.2400 138.2300 ...
            lat = parts[6]   # Index 6
            lon = parts[7]   # Index 7
            depth = parts[8] # Index 8
            mag = parts[9]   # Index 9
            
            # Tulis event.dat
            f_ev.write(f"{event_id} {lat} {lon} {depth} {mag}\n")
        else:
            parts = line.split()
            if len(parts) >= 4:
                st = parts[0]
                tt = parts[1]
                wt = parts[2]
                ph = parts[3]
                # Tulis phase.dat
                f_ph.write(f"{st:<5} {tt:>8} {wt:>5} {ph:>2} {event_id:>4}\n")

print(f"Selesai! Berhasil membuat {event_id} event.")