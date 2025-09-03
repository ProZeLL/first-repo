# Masukkan banyak binatang dan sebuah list untuk semua data binatang di Wombozoo
jumlahBinatang = input()
binatang = []

# Menggunakan looping untuk memasukkan data binatang (nama, berat, tinggi) pada list tersebut dalam tipe tuple
for i in range (int(jumlahBinatang)):
    dataBinatang = input().split()
    namaBinatang = dataBinatang[0]
    berat, tinggi = map(int, dataBinatang[1:])
    binatang.append((namaBinatang, berat, tinggi))
    
# Tampilkan list of tuple untuk semua binatang beserta data masing-masing tersebut
print(binatang)
print()

# Tampilkan sebuah kalimat untuk info binatang yang memiliki teringan dan terberat berdasarkan berat badannya
print("Animals with min & max weight:")

# Menggunakan looping dan branching untuk mencari binatang yang memiliki teringan dan terberat tersebut
minValue = 10 ** 5
maxValue = -1
for i in range (int(jumlahBinatang)):
    if (binatang[i][1] < minValue):
        namaBinatangMin = binatang[i][0]
        minValue = binatang[i][1]
    if (binatang[i][1] > maxValue):
        namaBinatangMax = binatang[i][0]
        maxValue = binatang[i][1]
        
# Tampilkan nama binatang dan berat badannya yang memiliki teringan dan terberat tersebut 
print(namaBinatangMin, minValue)
print(namaBinatangMax, maxValue)
print()

# Tampilkan sebuah kalimat untuk info binatang yang memiliki terendah dan tertinggi berdasarkan tinggi badannya
print("Animals with min & max height:")

# Menggunakan looping dan branching untuk mencari binatang yang memiliki terendah dan tertinggi tersebut
minValue = 10 ** 5
maxValue = -1
for i in range (int(jumlahBinatang)):
    if (binatang[i][2] < minValue):
        namaBinatangMin = binatang[i][0]
        minValue = binatang[i][2]
    if (binatang[i][2] > maxValue):
        namaBinatangMax = binatang[i][0]
        maxValue = binatang[i][2]
        
# Tampilkan nama binatang dan tinggi badannya yang memiliki terendah dan tertinggi tersebut
print(namaBinatangMin, minValue)
print(namaBinatangMax, maxValue)