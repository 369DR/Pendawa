print("\nPerintah del")
daftar_buku = ['Seven Habits','How to Influence People', 'First things First', 'Rich dad poor dad']
del daftar_buku[0]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nPerintah del dengan list comprehension")
daftar_buku = ['Seven Habits','How to Influence People', 'First things First', 'Rich dad poor dad']
del daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nPerintah del dengan list comprehension start")
daftar_buku = ['Seven Habits','How to Influence People', 'First things First', 'Rich dad poor dad']
del daftar_buku[0:-2] #start:End
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nPerintah del dengan list comprehension start")
daftar_buku = ['Seven Habits','How to Influence People', 'First things First', 'Rich dad poor dad']
del daftar_buku[0::2] #start:End:Step
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nMembuar list baru")
daftar_buku = ['Seven Habits','How to Influence People', 'First things First', 'Rich dad poor dad']
daftar_buku_baru = daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nMembuat list baru")
del daftar_buku[:]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print("\nMembuar list baru")
daftar_buku = ['Seven Habits', 'How to Influence People', 'First things First', 'Rich dad poor dad']
daftar_buku_baru = daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nMembuat list baru")
del daftar_buku[:]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print("\nMembuat list baru dengan comprehension : ganjil")
daftar_buku = ['1 Seven Habits', '2 How to Influence People', '3 First things First', '4 Rich dad poor dad']
daftar_buku_baru = daftar_buku [0::2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print("\nMembuat list baru dengan comprehension : genap")
daftar_buku = ['1 Seven Habits', '2 How to Influence People', '3 First things First', '4 Rich dad poor dad']
daftar_buku_baru = daftar_buku [1::2] #Start:Stop:End
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print("\nMembuat list baru dengan comprehension : buang di ujung")
daftar_buku = ['1 Seven Habits', '2 How to Influence People', '3 First things First', '4 Rich dad poor dad']
daftar_buku_baru = daftar_buku [0:-1:2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print("\nMembuat list baru dengan comprehension : ganjil")
daftar_buku = ['1 Seven Habits', '2 How to Influence People', '3 First things First', '4 Rich dad poor dad']
print(daftar_buku [0::2])
