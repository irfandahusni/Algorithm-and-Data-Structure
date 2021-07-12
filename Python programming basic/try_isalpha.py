while True:
    print('Masukkan nama Anda:')
    name = input()
    if name.isalpha():
        print("Halo", name)
        break
    print('Masukkan nama Anda dengan benar.')