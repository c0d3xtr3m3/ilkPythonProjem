import alanHesabi
import cevreHesabi
kenar1=0
kenar2=0
kenar3=0
cevre=0
alan=0
sekil = input("Geometrik şekil türünü giriniz :")
if sekil == "üçgen":
    kenar1=int(input("İlk kenarı giriniz :"))
    kenar2=int(input("İkinci kenarı giriniz :"))
    kenar3=int(input("Üçüncü kenarı giriniz :"))
    islem = input("yapılmak istenen hesaplamayı giriniz :")
    if islem == "alan":
        alan = alanHesabi.ucgenAlan(kenar1,kenar2,kenar3)
        print("üçgenin alanı :",alan)
    elif islem=="çevre":
        cevre = cevreHesabi.ucgenCevre(kenar1,kenar2,kenar3)
        print("üçgenin çevresi : ",cevre)
    else:
        print("tanımsız işlem")
elif sekil == "kare":
    kenar1=int(input("Kenar uzunluğu giriniz :"))
    islem = input("yapılmak istenen hesaplamayı giriniz :")
    if islem == "alan":
        alan = alanHesabi.kareAlan(kenar1)
        print("karenin alanı :",alan)
    elif islem=="çevre":
        cevre = cevreHesabi.kareCevre(kenar1)
        print("karenin çevresi : ",cevre)
    else:
        print("tanımsız işlem")
elif sekil=="dikdörtgen":
    kenar1=int(input("İlk kenarı giriniz :"))
    kenar2=int(input("İkinci kenarı giriniz :"))
    islem = input("yapılmak istenen hesaplamayı giriniz :")
    if islem == "alan":
        alan = alanHesabi.dikdortgenAlan(kenar1,kenar2)
        print("dikdörtgenin alanı :",alan)
    elif islem=="çevre":
        cevre = cevreHesabi.dikdortgenCevre(kenar1,kenar2)
        print("dikdörtgenin çevresi : ",cevre)
    else:
        print("tanımsız işlem")
else:
    print("tanımsız şekil")
