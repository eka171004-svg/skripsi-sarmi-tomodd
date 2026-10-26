# Script FINAL: Bikin phase.dat LENGKAP dengan header # (Format BMKG)
input_file = "phase_september2022.txt"
output_phase = "phase_final_v4.dat"

with open(input_file, 'r') as f_in, open(output_phase, 'w') as f_out:
    for line in f_in:
        line = line.strip()
        if not line:
            continue
        # Tulis PERSIS seperti aslinya (termasuk header #)
        f_out.write(line + "\n")

print("File phase_final_v4.dat berhasil dibuat (dengan header #).")