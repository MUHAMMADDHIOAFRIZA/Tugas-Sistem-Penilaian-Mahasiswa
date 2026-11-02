print("SISTEM PENILAIAN MAHASISWA")

jumlah = int(input("Jumlah mahasiswa (5-10): "))

if jumlah >= 5 and jumlah <= 10:
    total_nilai = 0

    for i in range(1, jumlah + 1):
        nilai = float(input(f"Masukkan nilai mahasiswa {i}: "))
        total_nilai += nilai

    rata_rata = total_nilai / jumlah

    print("Nilai rata-rata =", rata_rata)

else:
    print("Jumlah mahasiswa harus 5 sampai 10!")