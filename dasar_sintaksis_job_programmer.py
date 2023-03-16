"""
Semua sintaksis dasar bahasa pemrograman terdiri dari
1.Sekuensial  = langkah berurutan
2.Percabangan = langkah melompat jika kondisi terpenuhi
3.Perulangan  = mengulangi langkah yang sama berkali-kali selama/sampai kondisi terpenuhi
"""

# sequential

print('Ibu berkata, "Pergi ke toko"')
print('Budi Menjawab,"Baik apa yang harus saya lakukan di toko?"')
print('Ibu Menjawab,"Beli Satu botol susu"')
print("Maka budi berangkat ke toko")
print("Dan Mulai berbelanja")

# percabangan
jumlah_botol_susu = 170
jumlah_telur = 187
print(f"jumlah botol susu {jumlah_botol_susu}botol")
print(f"jumlah telur {jumlah_telur}butir")
if jumlah_botol_susu > 0:
    print("Budi mengecek harganya, dan ternyata uangnya cukup")
    if jumlah_telur == 0:
        print("Budi membeli 1 botol susu")
    else:
        print("Budi membeli 6 botol susu")
else:
    print("Budi tidak jadi membeli 1 botol susu")

print("Budi Pulang ke rumah")
print("Menyampaikan hasilnya kepada Ibu")
