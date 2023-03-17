""""
Program perulangan membaca buku dengan FOR
"""
jumlah_buku = 100
print('Ibu berkata, "Baca Semua Bukumu" ')

jumlah_buku_yang_sudah_dibaca = 0
print(f'Jumlah buku yang sudah dibaca {jumlah_buku_yang_sudah_dibaca}')

print("Dengan for")
for jumlah_buku_yang_sudah_dibaca in range(1, jumlah_buku+1):
    print(f"Buku ke {jumlah_buku_yang_sudah_dibaca} sudah dibaca")

print(f'Jumlah buku yang sudah dibaca {jumlah_buku_yang_sudah_dibaca}')

#tanpa for
"""
print("Tanpa for")
print("membaca buku ke-1")
print("membaca buku ke-2")
print("membaca buku ke-3")
print("membaca buku ke-4")
"""


