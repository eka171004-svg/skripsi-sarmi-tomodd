# Script Versi 1: Bikin event dan phase dari file asli BMKG
import re

input_file = "phase data.txt"
output_event = "event_v1.dat"
output_phase = "phase_v1.dat"

with open(input_file, 'r') as f_in, open(output_event, 'w') as f_ev, open(output_phase, 'w') as f_ph:
    event_id = 0
    for line in f_in:
        line = line.strip()
        if not line:
            continue
        
        if line.startswith('#'):
            if "2022 09" in line:
                event_id += 1
                numbers = re.findall(r'-?\d+\.\d+|-?\d+', line)
                if len(numbers) >= 10:
                    lat = numbers[6]
                    lon = numbers[7]
                    depth = numbers[8]
                    mag = numbers[9]
                    f_ev.write(f"{event_id} {lat} {lon} {depth} {mag}\n")
            else:
                event_id = -1
        else:
            if event_id > 0:
                parts = line.split()
                if len(parts) >= 4:
                    st = parts[0]
                    tt = parts[1]
                    wt = parts[2]
                    ph = parts[3]
                    f_ph.write(f"{st:<5} {tt:>8} {wt:>5} {ph:>2}\n")

print(f"Selesai! Membuat {event_id} event di event_v1.dat dan phase_v1.dat.")