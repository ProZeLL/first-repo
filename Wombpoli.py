# Masukkan dan sebuah list untuk banyak titik yang digambar Wompoli
jumlahTitik = input()
titik = []

# Menggunakan looping untuk memasukkan titik berupa 2 bilangan bulat pada list tersebut dalam tipe tuple
for i in range (int(jumlahTitik)):
    inputTitik = input().split()
    x, y = map(int, inputTitik)
    titik.append((x, y))
    
# Menampilkan list tersebut
print(titik)

# Menggunakan looping untuk mencari total jarak pada setiap titik tersebut
total = 0.0
for i in range (1, len(titik)):
    total = total + ((titik[i][0]-titik[i-1][0])**2+(titik[i][1]-titik[i-1][1])**2)**0.5
    
# Menampilkan total jarak dari setiap titik tersebut
print(total)