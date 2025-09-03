# Masukkan menyatakan banyaknya Dorabies, Doubloons, dan Dusts pada saat awal.
masukkan_dana = input().split(" ")
initial_dorabies = int(masukkan_dana[0])  # Dorabies
initial_doubloons = int(masukkan_dana[1])  # Doubloons
initial_dusts = int(masukkan_dana[2])  # Dusts

# Nilai konversi dari Dusts ke Doubloons dan dari Doubloons ke Dorabies
dust_to_doubloons_rate = int(input())
doubloons_to_dorabies_rate = int(input())

# Pilihan karakter
character_choice = int(input())

# Data posisi dan indikator dollar
visited_list = [
    [(3, 2), (3, 3), (3, 4)],  # visited0
    [(3, 4), (2, 4), (1, 4)],  # visited1
    [(2, 2), (2, 3), (2, 4), (2, 5)]  # visited2
]

dollar_indicator_list = [
    [235, -12, -89],  # dollar_indicator0
    [-89, -76, 365],  # dollar_indicator1
    [112, -46, -76, -11]  # dollar_indicator2
]

# Inisialisasi dana awal
dorabies = initial_dorabies
doubloons = initial_doubloons
dusts = initial_dusts

# Ambil data untuk karakter yang dipilih
visited = visited_list[character_choice]
dollar_indicators = dollar_indicator_list[character_choice]

# Function untuk menghitung dana setelah mengunjungi posisi
def calculate_funds(visited, dollar_indicators):
    global dorabies, doubloons, dusts
    current_position = None

    for i in range(len(visited)):
        current_position = visited[i]
        indicator = dollar_indicators[i]

        if indicator >= 0:
            # Positif: 3 digit
            dorabies += indicator // 100
            doubloons += (indicator // 10) % 10
            dusts += indicator % 10
        else:
            # Negatif: 2 digit
            dorabies += indicator // 10
            doubloons += indicator % 10

        # Konversi dusts ke doubloons jika ada
        if dusts >= dust_to_doubloons_rate:
            extra_doubloons = dusts // dust_to_doubloons_rate
            doubloons += extra_doubloons
            dusts %= dust_to_doubloons_rate

        # Konversi doubloons ke dorabies jika ada
        if doubloons >= doubloons_to_dorabies_rate:
            extra_dorabies = doubloons // doubloons_to_dorabies_rate
            dorabies += extra_dorabies
            doubloons %= doubloons_to_dorabies_rate

        # Cek apakah dana habis
        if dorabies <= 0 and doubloons <= 0 and dusts <= 0:
            break

    return current_position

# Hitung posisi terakhir yang berhasil dicapai
current_position = calculate_funds(visited, dollar_indicators)

# Tampilkan posisi terakhir dan dana yang tersisa
print("Reached position {} with {} Dorabies, {} Doubloons, {} Dusts".format(
    current_position, dorabies, doubloons, dusts
))
