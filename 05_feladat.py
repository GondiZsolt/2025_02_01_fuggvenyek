"""Írj egy programot, ami addig kér be egész pozitív számokat, amíg a felhasználó negtív számot nem ír!
A megadott számokat tárolja a program egy listában, és ezt adja át paraméterként egy függvények, amely a lista legkisebb elemével tér vissza.
A program írja ki, hogy melyik volt a megadott legkisebb szám!
"""

lista = []

while True:
    szamok = int(input("Adj meg számokat(negatív szám a befejezéshez): "))
    if szamok < 0:
            break

lista.append(szamok)

def legkisebb(szamok):
    return min(szamok)

print(legkisebb(lista))