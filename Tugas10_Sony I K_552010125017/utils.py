# Program utils.py
# Sony Iman Kurnia
# 04 - Desember - 2025

import json
import csv

def input_angka(pesan, minimum=0, maksimum=100):
    while True:
        try:
            angka = float(input(pesan))
            if angka < minimum or angka > maksimum:
                print(f"Nilai harus {minimum}-{maksimum}!")
            else:
                return angka
        except ValueError:
            print("Input harus berupa angka!")

def hitung_rata(nilai):
    return sum(nilai) / len(nilai)

def tentukan_status(rata):
    return "Lulus" if rata >= 60 else "Tidak Lulus"

def tentukan_grade(rata):
    if rata >= 85: return "A"
    if rata >= 75: return "B"
    if rata >= 65: return "C"
    if rata >= 55: return "D"
    return "E"

def input_mahasiswa():
    nama = input("Nama Mahasiswa : ")
    nilai1 = input_angka("Nilai 1: ")
    nilai2 = input_angka("Nilai 2: ")
    nilai3 = input_angka("Nilai 3: ")

    nilai = [nilai1, nilai2, nilai3]
    rata = hitung_rata(nilai)

    return {
        "nama": nama,
        "nilai": nilai,
        "rata": rata,
        "status": tentukan_status(rata),
        "grade": tentukan_grade(rata)
    }

def tampil_tabel(data):
    print("\n=== TABEL DATA MAHASISWA ===")
    print(f"{'Nama':<15}{'N1':<6}{'N2':<6}{'N3':<6}{'Rata':<8}{'Grade':<7}{'Status':<12}")
    print("-"*65)
    for m in data:
        n1, n2, n3 = m["nilai"]
        print(f"{m['nama']:<15}{n1:<6}{n2:<6}{n3:<6}{m['rata']:<8.2f}{m['grade']:<7}{m['status']:<12}")
    print()

def cari_tertinggi(data):
    return max(data, key=lambda x: x["rata"])

def cari_terendah(data):
    return min(data, key=lambda x: x["rata"])

def tertinggi_per_nilai(data, index):
    return max(data, key=lambda x: x["nilai"][index])

def cari_mahasiswa(data, nama):
    for m in data:
        if m["nama"].lower() == nama.lower():
            return m
    return None

def edit_mahasiswa(data, nama):
    mhs = cari_mahasiswa(data, nama)
    if not mhs:
        print("Mahasiswa tidak ditemukan.")
        return

    print("Masukkan nilai baru:")
    nilai = [
        input_angka("Nilai 1: "),
        input_angka("Nilai 2: "),
        input_angka("Nilai 3: ")
    ]
    mhs["nilai"] = nilai
    mhs["rata"] = hitung_rata(nilai)
    mhs["status"] = tentukan_status(mhs["rata"])
    mhs["grade"] = tentukan_grade(mhs["rata"])
    print("Data berhasil diperbarui!")

def hapus_mahasiswa(data, nama):
    mhs = cari_mahasiswa(data, nama)
    if mhs:
        data.remove(mhs)
        print("Berhasil dihapus!")
    else:
        print("Mahasiswa tidak ditemukan.")
