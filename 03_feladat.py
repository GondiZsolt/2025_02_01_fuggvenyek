"""Írj egy programot, amely tartalmaz egy 'harommal_oszthatok' nevű függvényt,
amely a paraméterként átvett listában megvizsgálja, hogy hány darab hárommal osztható szám van,
és ezzel az értékkel tér vissza! A program tartalmazza a függvény hívását is!"""


def harommal_oszthatok(a, b, c):
 eredmeny = 0
 if a % 3 == 0:
  eredmeny += 1
 if b % 3 == 0:
  eredmeny += 1
 if c % 3 == 0:
  eredmeny += 1
 return eredmeny

print(harommal_oszthatok(3, 6, 9))
print(harommal_oszthatok(3, 6, 10))
print(harommal_oszthatok(3, 7, 11))
print(harommal_oszthatok(3, 12, 15))




# def harommal_oszthaok(szamok):



# print(harommal_oszthatok([3, 6, 9]))
# print(harommal_oszthatok([3, 6, 10]))
# # print(harommal_oszthatok(3, 7, 11))
# # print(harommal_oszthatok(3, 12, 15))


"""Alakítsd át az előző programot úgy, hogy a felhasználó által megadott számokat tárolja el a program egy listában,
és ezt értékelje ki a függvény! (Az adatbeolvasás addig tartson, míg a felhasználó negatív számot nem ad meg!)
"""

# lista = []

# repeat = True

# while repeat:
#     szamok = int(input("Adj meg számokat(negatív szám a befejezéshez): "))
#     if szamok < 0:
#             repeat = False

# lista.append(szamok)

# def harommal_oszthatok(lista):
#     eredmeny = 0
#     for szam in lista:
#         if int(szam) % 3 == 0:
#             eredmeny += 1
#     return eredmeny

# print(harommal_oszthatok(lista))