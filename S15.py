# un tuplu este o colectie ordonata de elemente, de orice tip de date(numere, siruri, alte tupluri, liste, samd)
# ordine fixa - se foloseste indexare, incepand de la 0 si pastram ordinea de inserare
# imutabile - odata creat, nu mai poate fi modificat(adaugare, eliminare etc)

# sinxata
#nume_tuplu = (element1, element2, element3, ...)
# tuplurile pot avea de la 0 elemente pana la n elemente(0 elemente -> tuplu vid)

# Creare tuplu
tuplu1 = (5, 6, 7, 8)
tuplu2 = ("Florin", 2.14, True, None)
tuplu_vid = ()
tuplu_un_element = (10, )
tuplu_gresit = (10)
# print(type(tuplu_un_element))
# print(type(tuplu_gresit))

# creare fara paranteze rotunde
t = 1, 2, 3, 4
# print(type(t))

# conversie din alt tip de date in tuplu
lista = [1, 2, 3]
# tuplu_din_lista = tuple(lista)
# print(tuplu_din_lista)

# accesare si indexare
# tuplu1 = (5, 6, 7, 8)
# print(tuplu1[0])

# indexare negativa
# print(tuplu1[-1])

# daca folosesti un index in afara intervalului, se primeste IndexError
#print(tuplu1[7])

# slicing
# print(tuplu1[::-1])

# functii pentru tupluri
# count - numarare elemente
# t = (1, 2, 1, 3, 1, 2)
# print(t.count(3))

# index - returneaza primul index la care apare valoarea cautata
t = ("a", "b", "c", "a")
# print(t.index("b"))

# len - returneaza numarul de elemente din tuplu
# print(len(t))

# min si max
t = (1, 2, 1, 3, 1, 2)
# print(min(t))
# print(max(t))
# print(sum(t))

# any / all - compara elementele cu valori boolene
t = (0, 1, 2)
# print(any(t))
# print(all(t))

# concatenare / repetare
t1 = (1, 2)
t2 = (3, 4)
# print(t1 + t2)
# print(t1 * 3)

# verificare existenta element in tuplu
# print(1 in t1)
# print(1 not in t2)

# imutabilitate
# varianta 1: tuplu -> lista -> modificari -> tuplu
# t = (10, 20, 30)
# print(t)
# lista = list(t)
# lista[1] = 50
# t = tuple(lista)
# print(t)

# varianta 2: cu slicing
# t = (10, 20, 30)
# t = t[:1] + (50, ) + t[2:]
# print(t)

# tupluri care contin elemente mutabile
t = (1, [10, 20], 3)
t[1].append(30)
# print(t)

t = (1, (20, ), 4)
# print(type(t[1]))

tuplu_recursiv = (1, (2, 3), (4, (5, 6)))
# print(tuplu_recursiv[1])
# print(tuplu_recursiv[1][0])
# print(tuplu_recursiv[2][1][1])

# comparare - se compara element cu element, daca primul element difera, se ia rezultatul comparatiei primelor elemente
# daca toate elementele comune sunt egale, tuplul cu lungime mai mica/ mai scurt este considerat mai mic

# print((1,2,3) < (1,2,4))
# print((1, 2) < (1, 2, 0))
# print((2, ) > (1, 100))

# diferente tuplu - lista
# tuplu: imutabil; lista - mutabila
# nu exista metode de modificare; append, pop, remove etc
# utilizat in date fixe; colectii dinamice, modificabile
# accesare elemente - ambele prin indexare

# Exercitiul 1: coord = (10, 20)
# 1. afiseaza coordonata x
# 2. afiseaza coordonata y
# 3. creeaza un tuplu nou cu +5 pe x si -3 pe y
# 4. Afiseaza

# coord = (10, 20)
# # 1.
# print(coord[0])
# # 2.
# print(coord[1])
# # 3.
# lista = list(coord)
# print(lista)
# lista[0] += 5
# lista[1] -= 3
#
# coord = tuple(lista)
# print(coord)

# Exercitiul 2:
produs = ("calculator", 4800, "disponibil")
# 1. afiseaza numele produsului
# 2. verifica daca produsul este disponibil
# 3. creeaza un tuplu nou in care statusul este "stoc epuizat"

nume_produs = produs[0]
pret = produs[1]
status = produs[2]

print("nume produs: ", nume_produs)

if status == "disponibil":
    print("produsul este disponibil")
produs_lista = list(produs)
produs_lista[2] = "stoc epuizat"
produs = tuple(produs_lista)
print("Tuplu actualizat: ", produs)