""""
Tugas mengerjakan dari course,yaitu membuat flowcart dan coding
tentang ibu memerintahkan anaknya untuk membeli 1 botol susu dan 6 telur
"""

#sekuensial
print('Ibu memberi perintah"Beli 1 bottol susu dan beli 6 telur"')
print('Budi menjawab"Oke"')
print("Budi pergi ke toko")

# percabangan
jumlah_botol_susu = 170
jumlah_telur = 28
print(f"jumlah botol susu {jumlah_botol_susu} botol")
print(f"jumlah telur {jumlah_telur} Butir")
if jumlah_botol_susu > 0:
    print("budi membeli susu")
else:
    print("Budi tidak membeli telur")
print("Lalu")
if jumlah_telur == 0:
    print("Budi tidak membeli telur")
else:
    print("Budi membeli 6 Butir telur")