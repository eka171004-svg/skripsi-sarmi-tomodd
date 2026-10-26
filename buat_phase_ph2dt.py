# Script FINAL: Bikin phase.dat yang bersih
input_file = "phase_september2022.txt"
output_phase = "phase_final.dat"

with open(input_file, 'r') as f_in, open(output_phase, 'w') as f_out:
    event_id = 0
    for line in f_in:
        line = line.strip()
        if not line:
            continue
            
        if line.startswith('#'):
            event_id += 1
        else:
            parts = line.split()
            if len(parts) >= 4:
                st = parts[0]
                tt = parts[1]
                wt = parts[2]
                ph = parts[3]
                # Tulis: Stasiun TravelTime Weight Phase EventID
                f_out.write(f"{st:<5} {tt:>8} {wt:>5} {ph:>2} {event_id:>4}\n")

print("File phase_final.dat berhasil dibuat!")