"""
Perogram perulangan membaca buku dengan WHILE sampai paham
"""
jumlah_buku = 10
print('Ibu berkata,"Baca semua Bukumu"')

jumlah_buku_yang_sudah_dibaca_dan_dipahami = 0
print(f'jumlah buku yang sudah dibaca dan dipahami {jumlah_buku_yang_sudah_dibaca_dan_dipahami}')

while jumlah_buku_yang_sudah_dibaca_dan_dipahami < jumlah_buku:
    if jumlah_buku_yang_sudah_dibaca_dan_dipahami == 9:
        print(f"Buku ke {jumlah_buku_yang_sudah_dibaca_dan_dipahami} belum paham")
    else:
        jumlah_buku_yang_sudah_dibaca_dan_dipahami = jumlah_buku_yang_sudah_dibaca_dan_dipahami + 1
        print(f"Buku ke {jumlah_buku_yang_sudah_dibaca_dan_dipahami} sudah dibaca dan dipahami")

print(f'jumlah buku yang sudah dibaca {jumlah_buku_yang_sudah_dibaca_dan_dipahami}')