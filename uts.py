skstotal = int(input("masukkan sks 2 semester"))
if 0 <= skstotal and skstotal<= 144:
    nilaiKA = int(input("masukkan nilai MAta kuliah A"))
    bobotA = int(input("masukka bobot A"))
    sksMinimal = int(input("masukkan minimal sks"))
    kelulusan = str(input("masukkan LULUS atau TEMPUH "))
    if kelulusan == str("lulus"):
        if skstotal >= sksMinimal and nilaiKA >50:
            print("bisa")
        else :
            print("tidak bisa")
    elif kelulusan == str("tempuh"):
        print("anda bisa mengambil matkul B")
else:
    print("melebihi sks total")