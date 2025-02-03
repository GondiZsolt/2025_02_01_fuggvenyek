"""Írj egy programot, amelyben van egy 'kerulet' nevű függvény, amely az egyetlen kötelező paramétere mellett fogadhat több paramétert is!
Az opcionális paraméterek száma alapján döntse el milyen síkidomról van szó, és számolja ki a kerületét
(0 tetszőleges paraméter: négyzet, 1 tetszőleges paraméter: téglalap, 2 tetszőleges paraméter: háromszőg, 3 vagy több tetszőleges paraméter: sokszög)!

A program tartalmazzon mindegyik síkidom típusra egy-egy függvényhívást!
"""

def kerulet(a, *extra):
    if len(extra) == 0:
        print("Négyzet, kerülete:")
        return 4 * a
    elif len(extra) == 1:
        print("Téglalap, kerülete:")
        return 2 * (a + extra[0])
    elif len(extra) == 2:
        print("Háromszőg, kerülete:")
        return a + extra[0] + extra[1]
    else:
        print("Sokszőg, kerülete:")
        return sum(extra) + a


print(kerulet(5))
print(kerulet(3, 4)) 
print(kerulet(3, 4, 5))
print(kerulet(3, 4, 5, 6, 7))















# import math

# def kerulet(*args):
#     if len(args) == 1:
#         # Négyzet
#         return 4 * args[0]
#     elif len(args) == 2:
#         # Téglalap
#         return 2 * (args[0] + args[1])
#     elif len(args) == 3:
#         # Háromszög
#         a, b, c = args
#         return a + b + c
#     else:
#         # Sokszög
#         return sum(args)

# # Függvényhívások
# print(kerulet(5))  # Négyzet
# print(kerulet(3, 4))  # Téglalap
# print(kerulet(3, 4, 5))  # Háromszög
# print(kerulet(3, 4, 5, 6, 7))  # Sokszög