# Contoh Dictionary untuk para pelanggan di sebuah restoran
restaurant_customers = {
'John Steven': (10, 'still waiting'),
'Jane Black': (5, 'still waiting'),
'Mark Dawson': (15, 'got the food :)'),
'Janet Roberts': (30, 'left without eating :('),
'John Parker': (22, 'still waiting'),
'Anne Edwards': (18, 'got the food :)'),
'Mary Rogers': (7, 'got the food :)'),
'Emma Reed': (35, 'got the food :)'),
'Sophia Steven': (25, 'still waiting'),
'Amelia Cook': (32, 'still waiting'),
'John Scott': (15, 'still waiting'),
'George Famous': (20, 'still waiting'),
'Jack Baker': (38, 'got the food :)')
}
 
# Variabel total_left untuk menghitung total pelanggan yang menunggu selama 20 menit atau lebih dan masih belum mendapatkan makanan
total_left = 0
 
# Menggunakan looping untuk mencari pelanggan dengan ketentuan tersebut
for customer in restaurant_customers:
    if restaurant_customers[customer][0] >= 20 and restaurant_customers[customer][1] != "got the food :)":
        total_left = total_left + 1 # Jika ada yang sesuai ketentuan, ditambahkan satu
 
# Tampilkan total pelanggan berdasarkan ketentuan tersebut
print(str(total_left) + " customers left")