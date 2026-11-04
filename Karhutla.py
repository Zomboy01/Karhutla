from itertools import permutations

lokasi = [
    "Posko Utama",
    "Titik Api A",
    "Titik Api B",
    "Titik Api C"
]

waktu = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

rute_terbaik = None
waktu_tercepat = float('inf')

for rute in permutations(range(1, len(lokasi))):
    jalur = (0,) + rute + (0,)
    total_waktu = 0

    for i in range(len(jalur) - 1):
        total_waktu += waktu[jalur[i]][jalur[i + 1]]

    if total_waktu < waktu_tercepat:
        waktu_tercepat = total_waktu
        rute_terbaik = jalur

print("=== OPTIMALISASI RUTE PEMADAMAN KARHUTLA ===")

print("\nRute Tercepat:")
for i in rute_terbaik:
    print(lokasi[i], end="")

    if i != rute_terbaik[-1]:
        print(" -> ", end="")

print("\n\nTotal Waktu Tempuh:", waktu_tercepat, "menit")
print("Status: Rute terbaik berhasil ditemukan")
