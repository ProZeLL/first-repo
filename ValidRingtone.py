# Function untuk mengecek apakah durasi valid
def cekDurasi(durasi):
    valid_durations = {"1", "2", "4", "8", "16", "32"}
    return durasi in valid_durations

# Function untuk mengecek apakah pitch valid
def cekPitch(pitch):
    valid_pitches = {"a", "b", "c", "d", "e", "f", "g", "a#", "b#", "c#", "d#", "e#", "f#", "g#", "p"}
    return pitch in valid_pitches

# Function untuk mengecek apakah skala valid
def cekSkala(skala):
    return skala.isdigit() and 1 <= int(skala) <= 8

# Function utama untuk memeriksa apakah nada valid
def is_valid_note(note):
    # Awali dengan asumsi semua bagian kosong
    durasi = ""
    pitch = ""
    skala = ""
    titik = False
    
    # Pisahkan bagian durasi, pitch, skala, dan titik
    i = 0
    while i < len(note) and note[i].isdigit():
        durasi += note[i]
        i += 1

    # Tentukan pitch (bisa 1 atau 2 karakter)
    if i < len(note) and note[i] in "abcdefgp":
        pitch += note[i]
        i += 1
        if pitch in "abcdefg" and i < len(note) and note[i] == '#':
            pitch += note[i]
            i += 1

    # Tentukan skala (opsional)
    if i < len(note) and note[i].isdigit():
        skala += note[i]
        i += 1

    # Cek titik di akhir (opsional)
    if i < len(note) and note[i] == '.':
        titik = True
        i += 1

    # Pastikan tidak ada karakter tersisa yang belum diperiksa
    if i != len(note):
        return False

    # Pengecekan validitas durasi, pitch, dan skala
    if durasi and not cekDurasi(durasi):
        return False
    if not cekPitch(pitch):
        return False
    if pitch == "p" and skala:
        return False
    if skala and not cekSkala(skala):
        return False

    return True

# Membaca input dan memeriksa setiap nada
masukan_ringtone = input().split()
for note in masukan_ringtone:
    print(is_valid_note(note))
