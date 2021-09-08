# Kita juga bisa membuat argumennya bersifat wajib. Modifikasi berkas panggildicoding.py menjadi seperti berikut:

# Maka pada saat dijalankan, terdapat beberapa hal yaitu:

# Berkas panggildicoding.py harus dipanggil dengan parameter -n atau --nama.
# Jika kita memanggil berkas tanpa parameter -n maka berkas akan meminta parameter n atau nama.
# Jika kita memanggil dengan -n NAMAKITA atau --nama NAMAKITA maka berkas akan menampilkan Terima kasih telah menggunakan panggildicoding.py NAMAKITA.
# Jika kita memanggil --help, maka akan tampil help dengan penjelasan "Masukkan Nama Anda".

import argparse
 
parser = argparse.ArgumentParser()
parser.add_argument('-n', '--nama', required=True, help="Masukkan Nama Anda")
args = parser.parse_args()
 
print("Terima kasih telah menggunakan panggildicoding.py, "+args.nama)