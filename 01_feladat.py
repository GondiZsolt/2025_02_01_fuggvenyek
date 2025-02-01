"""Írj egy programot, amely tartalmaz egy 'osszegzo' nevű függvényt,
ami a paraméterként átvett listaelemeket (egész számokat) összeadja
és az összegükkel tér vissza! A program tartalmazza a függvény hívását is!"""

szamok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def osszegzo(szamok):
    osszeg = 0
    for szam in szamok:
        osszeg += szam
    return osszeg


print(osszegzo(szamok))