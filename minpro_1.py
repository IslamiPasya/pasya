#Nama  : Muhammad Islami Pasya
#NIM   : 2509116108
#Kelas : Sistem Informasi C
#Tema  : Sistem Pembayaran Tagihan Listrik

Tagihan = []  

print("=== Daftar Tagihan ===")
print("1. Tambah Tagihan")
print("2. Lihat Tagihan")
print("3. Keluar")

pilihan = input("Pilih Menu 1/2/3: ")

if pilihan == "1":
    nama = input("Masukkan Nama Pelanggan: ")
    Id = input("Masukkan Id Pelanggan: ")
    Jumlah = input("Jumlah (Rp): ")
    data = (nama, Id, Jumlah)
    Tagihan.append(data)
    print("Tagihan Berhasil Ditambahkan")

    print("\n=== Daftar Tagihan ===")
    print("1. Tambah Peminjaman")
    print("2. Lihat Daftar Peminjaman")
    print("3. Keluar")

    pilihan = input("Pilih Menu 1/2/3: ")

if pilihan == "2":
    if Tagihan:   
        print("\n=== Daftar Tagihan ===")
        p = Tagihan[0] 
        print("Nama:", p[0], "| Id:", p[1], "| Jumlah:", p[2])
    else:
        print("Belum ada tagihan.")


    print("\n=== Daftar Tagihan ===")
    print("1. Tambah Tagihan")
    print("2. Lihat Daftar Tagihan")
    print("3. Keluar")

    pilihan = input("Pilih Menu 1/2/3: ")

if pilihan == "3":
    print("Terima kasih telah menggunakan layanan kami")
else:
    print("Pilihan tidak tersedia")

