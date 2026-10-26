# Script 4: Membuat model kecepatan 1D (Vp & Vs)
# Menggunakan model standard global yang disederhanakan untuk kerak bumi
output_file = "model.dat"

# Data: [Kedalaman (km), Vp (km/s), Vs (km/s)]
# Angka ini adalah standar model kerak bumi bagian atas (crustal)
model_data = [
    [  0.0, 5.80, 3.36], # Lapisan paling atas (sedimen)
    [ 10.0, 6.00, 3.50], 
    [ 20.0, 6.50, 3.70], 
    [ 35.0, 7.80, 4.40], # Moho (batas kerak dan mantel)
    [ 70.0, 8.05, 4.50],
    [100.0, 8.10, 4.55]
]

print("Membuat file model kecepatan awal...")

with open(output_file, 'w') as f_out:
    for layer in model_data:
        depth = layer[0]
        vp = layer[1]
        vs = layer[2]
        
        # Format standar model TomoDD: Depth Vp Vs
        f_out.write(f"{depth:>6.1f} {vp:>6.2f} {vs:>6.2f}\n")

print(f"Selesai! File '{output_file}' berhasil dibuat.")