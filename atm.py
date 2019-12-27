saldo = 0
penarikan = 0
pilihan = 0
deposito = 0

import sys


print("\tSELAMAT DATANG DI ATM")
bahasa=int(input("\tPilih Bahasa=\n"))
if (bahasa==1):
	print("bahasa Indonesia")
elif(bahasa==2):
	print("bahasa Inggris")
else:
	bahasa="tidak ada"

pin=int(input("\tMasukkan Pin Anda=\n"))
if (pin==100919):
	pin="Benar"
else:
	pin=int(input("\tMasukkan Pin Anda=\n"))


tabungan = True
 
while tabungan:
    print("1: Deposit")
    print("2: Penarikan")
    print("3: Saldo")
    print("4: Keluar")
 
    pilihan = int(input("Masukkan menu yang anda inginkan: "))
 
    if pilihan == 1:
        deposito = int(input("Jumlah yang akan ditabung: Rp"))
        print("Jumlahnya yang akan ditabung yaitu Rp" + str(deposito))
        saldo = saldo + deposito
    elif pilihan == 2:
        print("Jumlah yang akan ditarik yaitu: Rp" + str(saldo))
        while True:
            penarikan = int(input("Penarikan: Rp"))
            if penarikan > saldo:
                print("Saldo anda tidak mencukupi untuk melakukan transaksi ini")
                continue
            saldo = saldo - penarikan
            break
    elif pilihan == 3:
        print("Sisa saldo: Rp" + str(saldo))
    elif pilihan == 4:
        sys.exit("Terima kasih")