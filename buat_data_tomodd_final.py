# Script FINAL: Bikin event.dat & phase.dat format USTC
import re

input_file = "phase_september2022.txt"
output_event = "event_v3.dat"
output_phase = "phase_v3.dat"

with open(input_file, 'r') as f_in, open(output_event, 'w') as f_ev, open(output_phase, 'w') as f_ph:
    event_id = 0
    for line in f_in:
        line = line.strip()
        if not line:
            continue
        
        if line.startswith('#'):
            event_id += 1
            numbers = re.findall(r'-?\d+\.\d+|-?\d+', line)
            
            if len(numbers) >= 10:
                y, m, d = numbers[0], numbers[1], numbers[2]
                h, mi, s = numbers[3], numbers[4], numbers[5]
                lat, lon = numbers[6], numbers[7]
                depth, mag = numbers[8], numbers[9]
                
                # Format WAJIB USTC ph2dt: 
                # # YYYY MM DD HH MM SS.SSS LAT LON DEPTH MAG EH EV RMS EventID
                f_ev.write(f"# {y:>4} {m:>2} {d:>2} {h:>2} {mi:>2} {s:>7} {lat:>8} {lon:>9} {depth:>5} {mag:>4} 0.0 0.0 0.0 {event_id:>4}\n")
        else:
            parts = line.split()
            if len(parts) >= 4:
                st = parts[0]
                tt = parts[1]
                wt = parts[2]
                ph = parts[3]
                # Format WAJIB USTC ph2dt: Stasiun, TravelTime, Weight, Phase, EventID
                f_ph.write(f"{st:<5} {tt:>8} {wt:>5} {ph:>2} {event_id:>4}\n")

print(f"Selesai! Berhasil membuat {event_id} event dengan format USTC.")