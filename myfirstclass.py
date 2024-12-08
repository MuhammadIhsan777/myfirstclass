class Mamalia:

    def menyusui():
        print("menyusui")

q=Mamalia
q.menyusui()

# Ini Adalah class Monkey
class Monkey(Mamalia):
    pass
    jumlah_tangan=2
    jumlah_kaki=2

    def berjalan():
        print('jalan')


myfirstobject=Monkey
myfirstobject.berjalan()
print(myfirstobject.jumlah_tangan)
myfirstobject.menyusui


# Class Kuda
class Kuda(Mamalia):
    pass
    jumlah_tangan=2
    jumlah_kaki=4

    def berlari():
        print('lari')

mysecondobject=Kuda
mysecondobject.berlari()
print(mysecondobject.jumlah_kaki)
mysecondobject.menyusui

