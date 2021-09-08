import hello

hello.world()

print(hello.nama)

Leon = hello.Reviewer("Leon", "JS")
Leon.review()

def cetak_info(name = 'Aan', age = 5):
    print('Nama:',name,'dan','Umur:',age)

cetak_info()

def cetak(param):
    print(param)
    return

cetak("Leanna")