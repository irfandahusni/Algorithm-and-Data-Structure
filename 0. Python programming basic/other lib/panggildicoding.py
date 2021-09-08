import argparse
 
parser = argparse.ArgumentParser()
parser.add_argument('-o', '--output', action='store_true', help="tampilkan output")
args = parser.parse_args()
 
if args.output:
    print("Halo, ini merupakan sebuah output dari panggildicoding.py")


# Maka pada saat dijalankan di terminal, terdapat beberapa hal yaitu:

# Berkas panggildicoding.py dapat menerima parameter -o atau --output.
# Jika kita memanggil berkas tanpa parameter -o maka berkas tidak akan menampilkan apapun.
# Jika kita memanggil dengan -o atau --output maka berkas akan menampilkan Halo, ini merupakan sebuah output dari panggildicoding.py.
# Jika kita memanggil --help, maka akan tampil help dengan penjelasan "tampilkan output".

# python panggildicoding.py -o

# python panggildicoding.py -o --help