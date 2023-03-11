print("Silahkan diInput Angka Sembarangnya, Bro!!!")
angkanya = int(input())
if angkanya > 1:
    if angkanya == 2:
        print("Angka ini Bilangan Prima")
    else:
        if angkanya % 2 == 0:
            print("Angka ini bukan Bilangan Prima")
        else:
            pembaginya = 3
            if angkanya % pembaginya == 0:
                if angkanya == pembaginya:
                    print("Angka ini Bilangan Prima")
                else:
                    print("Angka ini bukan Bilangan Prima")
            else:
                while angkanya % pembaginya != 0:
                    pembaginya = pembaginya + 2
                print("Angka ini Bilangan Prima")
else:
    print("Angka ini bukan Bilangan Prima")
