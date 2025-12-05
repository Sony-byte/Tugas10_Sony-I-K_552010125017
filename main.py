# Program main.py
# Sony Iman Kurnia
# 04 - Desember - 2025

import utils

def menu():
    print("""
======= MENU UTAMA =======
1. Input data mahasiswa
2. Tampilkan tabel data
3. Cari mahasiswa
4. Edit data mahasiswa
5. Hapus data mahasiswa
6. Tampilkan nilai tertinggi & terendah
0. Keluar
""")

def main():
    data = []

    while True:
        menu()
        pilih = input("Pilih menu: ")

        if pilih == "1":
            data.append(utils.input_mahasiswa())

        elif pilih == "2":
            if data:
                utils.tampil_tabel(data)
            else:
                print("Belum ada data.")

        elif pilih == "3":
            nama = input("Nama yang dicari: ")
            mhs = utils.cari_mahasiswa(data, nama)
            print(mhs if mhs else "Data tidak ditemukan.")

        elif pilih == "4":
            nama = input("Nama yang ingin diedit: ")
            utils.edit_mahasiswa(data, nama)

        elif pilih == "5":
            nama = input("Nama yang ingin dihapus: ")
            utils.hapus_mahasiswa(data, nama)

        elif pilih == "6":
            if data:
                t = utils.cari_tertinggi(data)
                r = utils.cari_terendah(data)
                print("Tertinggi :", t)
                print("Terendah  :", r)
            else:
                print("Data kosong.")

        elif pilih == "0":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()
