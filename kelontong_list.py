listBarang = ["Beras", "Gula ", "Minyak", "Mie"]
listSatuan = ["kg", "kg", "lt", "bungkus"]
listHarga = [10000, 14000, 18000, 2500]

def belanja(index):
    print(f'========================================================')
    jenis = int(input(f'Masukkan jenis barang ke-{index+1}: '))
    if jenis == 1:
        nama_barang = listBarang[0]
        satuan = listSatuan[0]
        harga_satuan = listHarga[0]
    elif jenis == 2:
        nama_barang = listBarang[1]
        satuan = listSatuan[1]
        harga_satuan = listHarga[1]
    elif jenis == 3:
        nama_barang = listBarang[2]
        satuan = listSatuan[2]
        harga_satuan = listHarga[2]
    elif jenis == 4:
        nama_barang = listBarang[3]
        satuan = listSatuan[3]
        harga_satuan = listHarga[3]
    else:
        print("WARNING: Jenis barang tidak tersedia.")
        choice = input(f'Apakah anda ingin mengulangi proses pilih barang (y/n)? ')

        if choice == "y":
            return belanja(index)
        elif choice == "n":
            print("Terima kasih sudah berbelanja")
            exit()
        else:
            print("Tidak Dapat Memproses inputan.")
            exit()

    jumlah = int(input(f'Masukkan jumlah {satuan} {nama_barang} yang dibeli: '))
    total_bayar = harga_satuan * jumlah
    total_diskon = (total_bayar*diskonan(jenis,jumlah))

    # Mengembalikan nilai dari fungsi berbentuk List
    return [jenis, jumlah, total_bayar, total_diskon]


def currencyIdr(value):
    return 'Rp {:,.2f}'.format(value)

def diskonan(jenis,jumlah):
    diskon = 0
    if jenis == 1:
        if jumlah >= 10:
            diskon = 5/100
    elif jenis == 2:
        if 10 <= jumlah < 20:
            diskon = 5/100
        else:
            diskon = 10/100
    elif jenis == 3:
        diskon = 10/100 if 10 <= jumlah < 20 else 15/100
    elif jenis == 4:
        if jumlah < 20:
            diskon = 5/100
        elif 20 < jumlah < 40:
            diskon = 10 / 100
        else:
            diskon = 15 / 100
    else:
        print("Gagal hitung diskonan")

    return diskon

def keranjang():
    keranjang = []
    print(f'=============== WELCOME TO KELONTONG PNM ===============')
    print(f'Berikut daftar jenis barang belanjaan Toko Kelontong PNM:\n1.{listBarang[0]}\n2.{listBarang[1]}\n3.{listBarang[2]}\n4.{listBarang[3]}')
    print(f'========================================================')
    jmljenis = int(input("Masukkan jumlah jenis barang yang akan dibeli: "))
    index = 0
    while (index < jmljenis):
        # add list from call function here
        keranjang.append(belanja(index))
        # add count +1
        index += 1
    return keranjang

def nota_belanja():
    total_akhir = 0
    for i, k in enumerate(keranjang()):
        # Format List: [jenis, jumlah, total_bayar, total_diskon]
        jenis = k[0]
        jumlah = k[1]
        total_bayar = k[2]
        total_diskon = k[3]
        if jenis == 1:
            nama_barang = listBarang[0]
            satuan = listSatuan[0]
            harga_satuan = listHarga[0]
        elif jenis == 2:
            nama_barang = listBarang[1]
            satuan = listSatuan[1]
            harga_satuan = listHarga[1]
        elif jenis == 3:
            nama_barang = listBarang[2]
            satuan = listSatuan[2]
            harga_satuan = listHarga[2]
        elif jenis == 4:
            nama_barang = listBarang[3]
            satuan = listSatuan[3]
            harga_satuan = listHarga[3]
        else:
            print("Jenis barang tidak tersedia")
        # print nota
        total_bayar_diskon = total_bayar - total_diskon
        total_akhir += total_bayar_diskon
        print(f'===================== ITEM ke-{i+1} ========================')
        print(f'{nama_barang} @{currencyIdr(harga_satuan)} \t\t{jumlah} {satuan} \t\t{currencyIdr(total_bayar)}')
        print(f'Diskon ({diskonan(jenis,jumlah)*100}%) \t\t\t\t\t\t\t(-{currencyIdr(total_diskon)})')

    print(f'========================================================')
    print(f'TOTAL BAYAR\t\t\t\t\t\t\t\t{currencyIdr(total_akhir)}')
    print(f'========================================================')

# Panggil fungsi
nota_belanja()
