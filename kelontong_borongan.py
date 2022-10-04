def belanja():
    totByr = 0
    jmlitem = int(input("Masukkan jumlah item barang yang ingin dibeli: "))
    for i in range(0,jmlitem):
        print(f'=============== WELCOME TO KELONTONG PNM ===============')
        barang1 = "Beras"
        barang2 = "Gula"
        barang3 = "Minyak"
        barang4 = "Mie"

        print(f'Daftar jenis barang belanjaan Toko Kelontong PNM:\n1.{barang1}\n2.{barang2}\n3.{barang3}\n4.{barang4}')
        print(f'========================================================')
        jenis = int(input(f"Masukkan jenis barang ke-{i+1} yang ingin dibeli: "))
        if jenis == 1:
            nama_barang = barang1
            satuan = "kg"
            harga_satuan = 10000
        elif jenis == 2:
            nama_barang = barang2
            satuan = "kg"
            harga_satuan = 14000
        elif jenis == 3:
            nama_barang = barang3
            satuan = "liter"
            harga_satuan = 18000
        elif jenis == 4:
            nama_barang = barang4
            satuan = "bungkus"
            harga_satuan = 2500
        else:
            print("Jenis barang tidak tersedia")

        jumlah = int(input(f'Masukkan jumlah {satuan} {nama_barang} yang dibeli:'))
        total_bayar = harga_satuan * jumlah
        total_diskon = (total_bayar*diskonan(jenis,jumlah))
        total_bayar_diskon = total_bayar - total_diskon

        # print hasil
        print(f'========================================================')
        print(f'Anda berbelanja {nama_barang} sebanyak {jumlah} {satuan} dengan harga satuan '+"Rp.{:,.2f}".format(harga_satuan))
        print(f'Total belanjaan anda adalah '+'Rp.{:,.2f}'.format(total_bayar))
        print(f'Anda mendapatkan diskon '+'Rp.{:,.2f}'.format(total_diskon))
        print(f'Total bayar setelah diskon adalah {currencyIdr(total_bayar_diskon)}')
        print(f'========================================================')
        totByr += total_bayar_diskon
    print(f'Total bayar keseluruhan belanja adalah {currencyIdr(totByr)}')
    return

def currencyIdr(value):
    return 'Rp.{:,.2f}'.format(value)

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

# Panggil fungsi
belanja()
