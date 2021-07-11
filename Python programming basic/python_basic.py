a = 1 + 3j + 4j + 4 + 4 + 4
print(type(a))

b = [['key1', 1],['key2',2]]
c = dict(b)
print(c)

x = [('a',1),('b',1)]
y = dict(x)
print(y)

v = (('a',1),('b',1))
v2 = dict(v)
print(v2)

print(type(2.2))

# %s - String
# %d - Integers
# %f - Bilangan Desimal
# %.<digit>f - Bilangan desimal dengan sejumlah digit angka dibelakang koma.
# %x/%X - Bilangan bulat dalam representasi Hexa (huruf kecil/huruf besar)

int_ex = 199
float_ex = 2.123456789
str_ex = "this is str"
print("integer example : %d" % int_ex)
print("float example : %d" % int_ex)
print("str float example : %.2f and %s" %(float_ex, str_ex))

angka = [7, 9, 11, 13]
print("Angka saya: %s" % angka)

value = int(input("give me number : "))
print(value * 5)

print(eval('90+10'))
