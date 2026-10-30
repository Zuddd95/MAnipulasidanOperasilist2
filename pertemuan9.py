kendaraan = ["motor", "mobil", "sepeda", "bus"]

#a
kendaraan.append("truk")

#b
kendaraan.insert(1, "becak")

#c
kendaraan.pop()

#d
kendaraan[3] = "skuter"

#e
print(len(kendaraan))
print(kendaraan)

angka = [75, 80, 90, 75, 85, 100, 65] 
#a
print(angka.index(100))
#b
print(angka.count(75))
#c
angka.sort()
print(angka)
#d
angka.reverse()
print(angka)

menu_utama = ["Nasi Goreng", "Mie Ayam"]
menu_tambahan = ["Kerupuk","Es Teh"]

menu_utama.extend(menu_tambahan)
print(menu_utama)

data_barang = [["Buku", 5000], ["Pensil", 2000], ["Penggaris", 3000]]

#a
print(data_barang[1][1])

#b
for barang in data_barang:
    print(f"Nama: {barang[0]}, Harga:{barang[1]}")