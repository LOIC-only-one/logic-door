# logic-door-xor

L'opérateur « ou exclusif » entre deux bits renvoie 0 si les deux bits sont égaux et 1 s'ils
sont différents. Il est symbolisé par le caractère ⊕.
Ainsi :

 0 ⊕ 0 = 0
 0 ⊕ 1 = 1
 1 ⊕ 0 = 1
 1 ⊕ 1 = 0

On représente ici une suite de bits par un tableau contenant des 0 et des 1.
Exemples :
a = [1, 0, 1, 0, 1, 1, 0, 1]
b = [0, 1, 1, 1, 0, 1, 0, 0]

>>> ou_exclusif(a, b)
[1, 1, 0, 1, 1, 0, 0, 1]
