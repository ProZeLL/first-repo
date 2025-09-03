# Isi dari character list berdasarkan pada soal
DEFAULT_CHARACTER_LIST = [
    'HOMELANDER', 'IMAN', 'TERMINATOR', 'LELO MUSK', 'MR. MONASH', 
    'FYP STUDENT 2', 'HERMIONE GRANGER', 'SUPERMARIO', 'SUNFLOWER', 
    'THANOS', 'LUIGI', 'CHATGPT5', 'PATRICK STAR', 'GARY THE SNAIL', 
    'MICHONNE', 'VENOM', 'SPONGEBOB', 'DORAEMON', 'WOLVERINE', 
    'DORAEMON 2.0', 'BUMBLEBEE'
]

# Masukkan untuk banyak karakter serta jumlah pilihan karakter menurut masukkan user
banyakKarakter = int(input())
pilihanKarakter = input().strip().upper()  # Mengambil input dan mengubah menjadi huruf besar

# Memasukkan nama karakter menurut ketentuan soal
karakter = []
if pilihanKarakter == "M":
    i = 0
    while i < banyakKarakter:
        namaKarakter = input().strip().upper()  # Ubah nama menjadi huruf besar
        if namaKarakter in karakter:
            print("%s is a duplicate, try again!" % namaKarakter)  # Tampilkan kalimat jika nama karakter terulang
        else:
            karakter.append(namaKarakter)
            i += 1
else:  # Pilihan otomatis
    jumlahKarakter = int(input())
    selected_characters = []  # Menyimpan karakter yang memenuhi syarat
    for character in DEFAULT_CHARACTER_LIST:
        total_consonants = sum(1 for ch in character if ch not in 'AEIOU ')
        if total_consonants % jumlahKarakter == 0:
            selected_characters.append(character)
    
    # Ambil hanya jumlah karakter yang diminta
    karakter = selected_characters[:banyakKarakter]

# Tampilkan karakter-karakter yang didapatkan dengan format dalam list serta huruf kapital semua
print(karakter)

       