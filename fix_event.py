# Script FINAL: Bikin event.dat dengan format HypoDD yang ketat
import re

input_file = "phase_september2022.txt"
output_event = "event_final.dat"

with open(input_file, 'r') as f_in, open(output_event, 'w') as f_out:
    event_id = 0
    for line in f_in:
        line = line.strip()
        if line.startswith('#'):
            event_id += 1
            # Ambil angka pakai regex
            numbers = re.findall(r'-?\d+\.\d+|-?\d+', line)
            
            # Format asli: # 2022 09 11 20 14 30.686 -2.2400 138.2300 10.00 4.49 ...
            # Index: [0]=2022, [1]=09, [2]=11, [3]=20, [4]=14, [5]=30.686, [6]=Lat, [7]=Lon, [8]=Depth, [9]=Mag
            if len(numbers) >= 10:
                y = numbers[0]
                m = numbers[1]
                d = numbers[2]
                h = numbers[3]
                mi = numbers[4]
                s = numbers[5]
                lat = numbers[6]
                lon = numbers[7]
                depth = numbers[8]
                mag = numbers[9]
                
                # Format WAJIB ph2dt:
                # # YYYY MM DD HH MM SS.SSS LAT LON DEPTH MAG EH EV RMS EventID
                f_out.write(f"# {y:>4} {m:>2} {d:>2} {h:>2} {mi:>2} {s:>7} {lat:>8} {lon:>9} {depth:>5} {mag:>4} 0.0 0.0 0.0 {event_id:>4}\n")

print(f"Selesai! Berhasil mengekstrak {event_id} event.")