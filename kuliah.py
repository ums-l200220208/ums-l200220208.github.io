class Mahasiswa:
    def __init__(self, nama, nim, saldo):
        self.nama = nama
        self.nim = nim
        self.saldo = saldo
        self.matakuliah = []
        self.nilai_akhir = {}

    def bayar_spp(self, jumlah):
        if self.saldo >= jumlah:
            self.saldo -= jumlah
            print(f"{self.nama} telah membayar SPP sebesar Rp{jumlah}. Sisa saldo: Rp{self.saldo}.")
        else:
            print(f"{self.nama} tidak memiliki cukup saldo untuk membayar SPP.")

    def tambah_matakuliah(self, nama_mk):
        self.matakuliah.append(nama_mk)
        print(f"Mata kuliah '{nama_mk}' berhasil ditambahkan.")

    def belajar(self, nama_mk):
        if nama_mk in self.matakuliah:
            print(f"{self.nama} sedang belajar mata kuliah '{nama_mk}'.")
        else:
            print(f"{self.nama} tidak terdaftar di mata kuliah '{nama_mk}'.")

    def nilai_akhir_mk(self, nama_mk, nilai):
        if nama_mk in self.matakuliah:
            self.nilai_akhir[nama_mk] = nilai
            print(f"Nilai akhir mata kuliah '{nama_mk}' untuk {self.nama} adalah {nilai}.")
        else:
            print(f"{self.nama} tidak terdaftar di mata kuliah '{nama_mk}'.")

    def tampilkan_transkrip(self):
        print(f"\nTranskrip Nilai - {self.nama} ({self.nim})")
        print("-" * 30)
        for mk, nilai in self.nilai_akhir.items():
            print(f"{mk}: {nilai}")
        print("-" * 30)


# Program Utama
# Buat mahasiswa dengan nama, NIM, dan saldo awal
mahasiswa = Mahasiswa("Andi", "L200220208", saldo=5000000)

# Langkah 1: Bayar SPP
mahasiswa.bayar_spp(2500000)

# Langkah 2: Daftar Mata Kuliah
mahasiswa.tambah_matakuliah("Matematika")
mahasiswa.tambah_matakuliah("Fisika")

# Langkah 3: Proses Belajar
mahasiswa.belajar("Matematika")
mahasiswa.belajar("Fisika")

# Langkah 4: Penilaian Akhir
mahasiswa.nilai_akhir_mk("Matematika", 85)
mahasiswa.nilai_akhir_mk("Fisika", 90)

# Tampilkan Transkrip
mahasiswa.tampilkan_transkrip()
