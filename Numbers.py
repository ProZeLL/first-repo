# Masukkan pengguna untuk total kasus
jumlahKasus = int(input())

# Menggunakan looping untuk mencari apakah bisa diurutkan berdasarkan ketentuan Dodo
for i in range(jumlahKasus):
    # Masukkan pengguna untuk total bilangan dan bilangan apa saja
    jumlahBilangan = int(input())
    bil = list(map(int, input().split()))

    # Hitung jumlah angka genap dan ganjil
    totalGenap = 0
    totalGanjil = 0

    for angka in bil:
        if angka % 2 == 0:
            totalGenap += 1
        else:
            totalGanjil += 1

    # Jika jumlah genap dan ganjil berbeda lebih dari satu, hasilnya "NO"
    if abs(totalGenap - totalGanjil) <= 1:
        print("YES")
    else:
        print("NO")



        