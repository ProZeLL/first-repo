# Isi dari character list berdasarkan pada soal
DEFAULT_CHARACTER_LIST = ['HOMELANDER', 'IMAN',
'TERMINATOR', 'LELO MUSK', 'MR. MONASH', 'FYP STUDENT 2',
'HERMIONE GRANGER', 'SUPERMARIO', 'SUNFLOWER', 'THANOS',
'LUIGI', 'CHATGPT5', 'PATRICK STAR', 'GARY THE SNAIL',
'MICHONNE', 'VENOM', 'SPONGEBOB', 'DORAEMON', 'WOLVERINE',
'DORAEMON 2.0', 'BUMBLEBEE']
 
# Masukkan untuk banyak karakter serta jumlah pilihan karakter menurut masukkan user
banyakKarakter = int(input())
pilihanKarakter = input()
 
# Memasukkan nama karakter menurut ketentuan soal
karakter = []
if (pilihanKarakter == "M" or pilihanKarakter == "m"):
    i = 0
    while (i < banyakKarakter): 
        namaKarakter = input() # Masukkan untuk nama karakter
        if (namaKarakter in karakter):
            print(namaKarakter.upper() + " is a duplicate, try again!")  # Tampilkan kalimat tersebut jika nama karakter yang dimasukkan terulang kembali
        else:
            karakter.append(namaKarakter)
            i = i + 1
else:
    namaKarakter = int(input()) # Masukkan untuk banyak karakter yang didapatkan berdasarkan huruf konsonan yang habis dibagi dengan jumlah banyak karakter
    for character in DEFAULT_CHARACTER_LIST: # Menggunakan looping untuk mencari karakter dengan ketentuan tersebut untuk dimasukkan ke dalam list
        total = 0
        for k in range(len(character)):
            if (character[k] != 'A' and character[k] != 'I' and character[k] != 'U' and character[k] != 'E' and character[k] != 'O'):
                total = total + 1
        if (total%namaKarakter == 0):
            karakter.append(character)
 
# Tampilkan karakter-karakter yang didapatkan dengan format dalam list serta huruf kapital semua
printKarakter = []
for i in range(banyakKarakter):
    printKarakter.append(karakter[i].upper())
print(printKarakter)
                
       
       