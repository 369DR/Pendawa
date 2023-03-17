daftar_buku = ['Seven Habits','How to Influence People', 'First things First', 'Rich dan for dad']
print("tampilkan varialbel daftar_buku")
print(daftar_buku)

print("\nproses semua dengan for in")
for buku in daftar_buku:
    print(buku)

print("\nTampilkan isi daftar_buku pada indeks tertentu")
print(daftar_buku[0])
print(daftar_buku[1])

print("\nTampilkan dengan for in range")
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

daftar_buku = [1, "Profit Maker", 888, 3.14]
print("\nTampilkan dengan for in range, dimana tipe data tiap elemen berbeda2")
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nkembalikan nilai awal daftar buku")
daftar_buku = ['Seven Habits','How to Influence People', 'First things First', 'Rich dan for dad']
print("\nTambahkan 1 buku baru")
daftar_buku.append("The visual MBA")
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nClear list")
daftar_buku.clear()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nGanti elemen pertama")
daftar_buku = ['Seven Habits','How to Influence People', 'First things First', 'Rich dan for dad']
daftar_buku[0] = "Eight Habits"
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nAnmbil elemen ke-2")
buku = daftar_buku.pop(1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nBuku yang diambil tadi")
print(buku)

print("\npop")
daftar_buku.pop()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\npop -1 ")
daftar_buku = ['Seven Habits','How to Influence People', 'First things First', 'Rich dan for dad']
daftar_buku.pop(-4)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])


