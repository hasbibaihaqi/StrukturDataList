def buat_daftar_belanja():
    daftar_belanja = []

    while True:
        print("\n--- Daftar Belanja Harian ---")
        print("1. Tambah item")
        print("2. Hapus item")
        print("3. Lihat daftar belanja")
        print("4. Periksa keberadaan item")
        print("5. Jumlah item dalam daftar")
        print("6. Urutkan daftar belanja")
        print("7. Keluar")

        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == '1':
            item = input("Masukkan item yang ingin ditambahkan: ")
            daftar_belanja.append(item) # Metode append()
            print(f"'{item}' berhasil ditambahkan ke daftar belanja.")
        elif pilihan == '2':
            if not daftar_belanja:
                print("Daftar belanja kosong.")
            else:
                print("Daftar belanja saat ini:", daftar_belanja)
                item_hapus = input("Masukkan item yang ingin dihapus: ")
                if item_hapus in daftar_belanja:
                    daftar_belanja.remove(item_hapus) # Metode remove()
                    print(f"'{item_hapus}' berhasil dihapus dari daftar belanja.")
                else:
                    print(f"'{item_hapus}' tidak ditemukan dalam daftar belanja.")
        elif pilihan == '3':
            if not daftar_belanja:
                print("Daftar belanja kosong.")
            else:
                print("--- Isi Daftar Belanja ---")
                for index, item in enumerate(daftar_belanja): # Iterasi
                    print(f"{index+1}. {item}")
        elif pilihan == '4':
            item_periksa = input("Masukkan item yang ingin diperiksa: ")
            if item_periksa in daftar_belanja: # Operator in
                print(f"'{item_periksa}' ada dalam daftar belanja.")
            else:
                print(f"'{item_periksa}' tidak ada dalam daftar belanja.")
        elif pilihan == '5':
            jumlah_item = len(daftar_belanja) # Fungsi len()
            print(f"Jumlah item dalam daftar belanja: {jumlah_item}")
        elif pilihan == '6':
            daftar_belanja.sort() # Metode sort()
            print("Daftar belanja berhasil diurutkan.")
        elif pilihan == '7':
            print("Terima kasih telah menggunakan aplikasi daftar belanja.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    buat_daftar_belanja()