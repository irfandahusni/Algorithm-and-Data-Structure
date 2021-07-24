class Calculator:
    def __init__(self, nilai = 0):
        self.nilai = nilai

    def tambah_angka(self, angka1, angka2):
        self.nilai = angka1 + angka2
        if self.nilai > 9:  # kalkulator sederhana hanya memroses sampai 9
            print('kalkulator sederhana melebihi batas angka: {}'.format(self.nilai))
        return self.nilai

    @classmethod
    def multiplication(cls  ,a,b):
        return '{} * {} = {}'.format(a,b, a*b)

    @staticmethod
    def divide(a,b):
        return (a/b)



c = Calculator(9999)
print(c.nilai)

print(Calculator.multiplication(3,3))
print(c.multiplication(4,4))

print(Calculator.divide(4,2))