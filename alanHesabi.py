import math

def ucgenAlan(kenar1,kenar2,kenar3):
    yariCevre = (kenar1+kenar2+kenar3)/2
    alan = math.sqrt((yariCevre-kenar1)*(yariCevre-kenar2)*(yariCevre-kenar3))
    return alan

def kareAlan(kenar):
    alan = pow(kenar,2)
    return alan

def dikdortgenAlan(kenar1,kenar2):
    alan = kenar1*kenar2
    return alan

    
