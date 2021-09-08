class Kalkulator:
    """contoh kelas kalkulator sederhana. anggap kelas ini tidak boleh diubah!"""
    def __init__(self, nilai=0):
        self.nilai = nilai
 
    def tambah_angka(self, angka1, angka2):
        self.nilai = angka1 + angka2
        if self.nilai > 9:  # kalkulator sederhana hanya memroses sampai 9
            print('kalkulator sederhana melebihi batas angka: {}'.format(self.nilai))
        return self.nilai

class KalkulatorKali(Kalkulator):
    """contoh mewarisi kelas kalkulator sederhana"""
 
    def kali_angka(self, angka1, angka2):
        self.nilai = angka1 * angka2
        return self.nilai

class KalkulatorKaliOverride(Kalkulator):
    """contoh mewarisi kelas kalkulator sederhana"""
 
    def kali_angka(self, angka1, angka2):
        self.nilai = angka1 * angka2
        return self.nilai
 
    def tambah_angka(self, angka1, angka2):
        self.nilai = angka1 + angka2
        return self.nilai

class KalkulatorTambahSuper(Kalkulator):
    """contoh mewarisi kelas kalkulator sederhana"""
 
    def tambah_angka(self, angka1, angka2):
        if angka1 + angka2 <= 9:  # fitur ini sudah oke di kelas dasar, gunakan yang ada saja
            super().tambah_angka(angka1, angka2)  # panggil fungsi dari Kalkulator lalu isi nilai
        else:  # ini adalah fitur baru yang ingin diperbaiki dari keterbatasan kelas dasar
            self.nilai = angka1 + angka2
        return self.nilai

kk = KalkulatorKali()
 
b = kk.tambah_angka(5, 6)  # fitur tambah_angka yang dipanggil milik KalkulatorKali
print(b)

kk = KalkulatorKaliOverride()
 
b = kk.tambah_angka(5, 6)  # fitur tambah_angka yang dipanggil milik KalkulatorKali
print(b)

kk = KalkulatorTambahSuper()
 
b = kk.tambah_angka(5, 6)  # fitur tambah_angka yang dipanggil milik KalkulatorKali
print(b)

