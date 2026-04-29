# 1. Intro Liste
# O lista reprezinta o colectie de date/valori pastrate intr-o anumita ordine
# Exemplu:
# fructe = ["mere", "banane", "portocale"]
# print(fructe)
#
# # O lista poate contine
# numere = [1, 2, 3]
# nume = ["Florin", "Mihai", "Andrei"]
# valori_mixte = [10, "Florin", True, False, 1.2]

# Listele sunt ordonate
# Sunt modificabile
# Pot contine valorile duplicate
# Pot contine tipuri de date diferite

# 1.2 Folosim liste atunci cand avem mai multe valori care apartin aceleiasi categorii
# note = [7, 6, 9, 10]
# echipament_it = ["laptop", "pc", "mouse"]
# temperaturi = [21.5, 30, 17.5]
# persoane = ["Ana", "Florin", "Bogdan"]

# Folosim lista note ca sa stocam mai multe valori intr-un singur loc, evitand astfel metoda de jos:
# nota1 = 7
# nota2 = 6
# nota = 9
# etc

# 1.3 Cateva diferente intre liste, tupluri, seturi si dictionare
# O lista este ordonata si modificabila

# Un tuplu in schimb, seamana cu lista dar nu il poti modificare dupa creare
#ex_tuplu = (10, 20)
# pastreaza ordinea
# permite duplicate
# nu se poate modifica

# Un set este o colectie fara ordine fixa si fara duplicate
# ex_set = {1, 2, 3, 3, 3, 5, 7, 10, 6}
# print(ex_set)
# nu garanteaza ordinea
# nu permite duplicate
# folosit pentru eliminarea duplicatelor

# un dictionar pastreaza datele sub forma cheie-valoare
# student = {
#     "nume": "Florin",
#     "varsta": 26,
#     "oras": "Timisoara"
# }
# folosit pentru structurare date
# in dictionar accesezi valorile dupa cheie, nu dupa index numeric

# 1.4 Exemplu
# note = [10, 8, 9, 7]
# print(note)
# print("Prima nota din lista: ", note[0])
# print("Cate note sunt in lista: ", len(note))

# 1.5 Exercitiu scurt - Creeaza o lista cu 5 orase si afiseaza
# orase = ["Timisoara", "Cluj", "Bucuresti", "Iasi", "Lugoj"]
# print(orase)

# 2. Crearea listelor
# 2.1 Cu [ ]
# lista = []

# 2.2 Folosim list() - transforma o structura iterabila in lista
# litere = list("Python")
# print(litere)
#
# numere = list(range(1, 6))
# print(numere)

# List comprehension

# numere = [1, 2, 3, 4, 5]
# print(numere)
# nr_dublate = [numar * 2 for numar in numere]
# print(nr_dublate)
#
# patrate = []
#
# for numar in range(1, 6):
#     patrate.append(numar * numar)
# print(patrate)
#
# patrate = [numar * numar for numar in range(1, 6)]
# [ce_adaug_in_lista for fiecare_element in colectie]

# 3. Accesare elemente din lista
# 3.1 Index pozitiv
# Pozitiile elementelor dintr-o lista se numesc indexuri
# in python, indexarea incepe de la 0
# fructe = ["mere", "banane", "portocale"]
# 0 -> mere
# 1 -> banane
# 2 -> portocale
# print(fructe[0])
# print(fructe[1])
# print(fructe[2])

# 3.2 index negativ
# Index negativ -> pornim de la finalul listei
# fructe = ["mere", "banane", "portocale"]
# -1 -> portocale
# -2 -> banane
# -3 -> mere
# print(fructe[-1])
# print(fructe[-2])
# print(fructe[-3])

# 3.3. Slicing -> extrage o anumita parte dintr-o lista
# sintaxa -> lista[start:stop] unde:
# start este inclus
# stop nu este inclus

# numere = [1, 2, 3, 4, 5]
# print(numere[1:4])

# nume = ["Florin", "Maria", "Andrei", "Mihai", "Ionut"]
# print(nume[0:3])
# print(nume[2:5])
# print(nume[:3])
# print(nume[2:])

# numere = [1, 2, 3, 4, 5, 6, 7]
# # Printeaza primele 3 elemente
# print(numere[:3])
# # printeaza ultimele 3 elemente
# print(numere[4:])
# # printeaza ultimele 3 elemente cu indexare negativa
# print(numere[-3:])

# 3.4 Slicing cu pasi
# Sintaxa -. lista[start:stop:pas]
# numere = [1, 2, 3, 4, 5, 6, 7, 8]
# print(numere[0:8:2])
# print(numere[0::2])
# print(numere[::2])
# print(numere[1::2])

# 3.5 inversarea unei liste cu slicing
# metoda pentru inversarea unei liste rapid:
# lista_inversata = lista[::-1]
# Exemplu
# numere = [1, 2, 3, 4, 5]
# invers = numere[::-1]
# print(numere)
# print(invers)

# 4. Modificarea listelor
# 4.1 Modificare prin index
# Listele sunt modificabile, putem schimba un element folosindu-ne de indexul lui

# masini = ["audi", "logan", "bmw"]
# print(masini)
# masini[1] = "mercedes"
# print(masini)

# 4.2 Modificare prin slicing - poti inlocui mai multe elemente deodata
# numere = [1, 2, 3, 4, 5]
# print(numere)
# numere[1:4] = [20, 30, 40]
# print(numere)

# modificare prin slicing cu numar diferit de elemente
# numere = [1, 2, 3, 4, 5]
# print(numere)
# numere[1:3] = [100, 200, 300, 400]
# print(numere)

# 4.3 Adaugare cu append
# Metoda python care un element la finalul listei

# nume = ["Florin", "Mihai"]
# print(nume)
# nume.append("Maria")
# print(nume)

# 4.4 Inserare cu insert - adauga un element intr-o anumita pozitie din lista
# lista.insert(index, valoare)

# fructe = ["mere", "pere"]
# print(fructe)
# fructe.insert(1, "banane")
# print(fructe)

# 4.5 Extindere cu extend - adauga intr-o lista elementele din alta lista
# lista1 = [1, 2, 3]
# lista2 = [4, 5, 6]
# print("lista 1 inainte de extend: ", lista1)
# lista1.extend(lista2)
# print("Lista 1 dupa extend; ", lista1)
# print("Lista 2: ", lista2)

# lista = [1, 2]
# #lista.append([3, 4])
# lista.extend([3, 4])
# print(lista)

# 5. Stergerea elementelor din lista
# 5.1 del() - sterge un element dupa index

# fructe = ["mere", "pere", "banane"]
# del fructe[1]
# print(fructe)

# 5.2 remove() - sterge dupa valoare, nu dupa index
# fructe = ["mere", "pere", "banane"]
# print(fructe)
# fructe.remove("pere")
# print(fructe)

# 5.3 Stergere cu pop() - sterge un element si il returneaza. Daca nu specifici indexul, sterge ultimul element
# fructe = ["mere", "pere", "banane"]
# ultimul_element = fructe.pop()
# print("Element sters: ", ultimul_element)
# print("Lista actualizata: ", fructe)
#
# fructe = ["mere", "pere", "banane"]
# sters = fructe.pop(0)
# print(sters)
# print(fructe)

# 5.4 Stergere cu clear() - sterge lista complet - ramane lista goala\
# numere = [1, 2, 3, 4]
# print(numere)
# numere.clear()
# print(numere)

# 6 Alte functii utile
# 6.1 sort() - sorteaza lista, modificand-o pe cea originala
# numere = [2, 6, 1, 7, 15, 100, 1001]
# print(numere)
# numere.sort()
# print(numere)

# 6.2 reverse() - inverseaza lista originala
# numere = [2, 6, 1, 7, 15, 100, 1001]
# print(numere)
# numere.reverse()
# print(numere)

# 6.3 copy() - creeaza o copie superficiala a listei
# a = [1, 2, 3]
# b = a.copy()
# b.append(4)
# print(a)
# print(b)

# 6.4 count() - numara de cate ori apare o valoare
# numere = [1, 2, 2, 2, 3]
# nume = ["ana", "ana", "florin"]
# aparitii = nume.count("ana")
# print(aparitii)

# 6.5 min / max - returneaza cea mai mica/ cea mai mare valoare
# numere = [1, 2, 3, 4, 5]
# print(min(numere))
# print(max(numere))

# 6.6 sum() - aduna toate elementele numerice dintr-o lista
# numere = [1, 2, 3, 4, 5, int("6")]
# total = sum(numere)
# print(total)

# 6.7 zip() - combina doua sau mai multe liste element cu element
# nume = ["ana", "florin", "mihai"]
# note = [7, 8, 9]
# for nume, note in zip(nume, note):
#     print(nume, note)

# Iterare prin liste
# for simplu
# nume = ["ana", "florin", "mihai"]
# for persoana in nume:
#     print(persoana)

# for numar in range(1, 5):
#     print(numar)

# Iterare cu index
# nume = ["ana", "florin", "mihai"]
# for index in range(len(nume)):
#     print(index, nume[index])

# # cu enumerate - parcurgi o lista si ai nevoie de doua lucruri in acelasi timp: indexul si valoarea
# fructe = ["mere", "pere", "banane"]
# for index, valoare in enumerate(fructe):
#     print(index, valoare)

# Exercitiu 1 - gestionare comenzi magazin
# avem o lista pentru comenzile dintr-un magazin
# [nume_produs, pret, status]
# 1. sa afisam toate comenzile
# 2. afiseaza doar comenzile neprocesate
# 3. calculeaza valoarea totala a comenzilor
# 4. pune toate comenzile neprocesate ca procesate
# 5. afiseaza lista dupa modificari

# comenzi = [
#     ["telefon", 1000, "neprocesata"],
#     ["laptop", 5000, "procesata"],
#     ["aspirator", 2000, "neprocesata"]
# ]
#
# lista_cumparaturi = ["lapte", "carne", "oua", "paine"]
#
# # 1. Afiseaza toate produsele pe rand nou
# for produs in lista_cumparaturi:
#     print(produs)
# # 2. Adauga produsul "iaurt" in lista
# lista_cumparaturi.append("iaurt")
# print("Ultimul element adaugat: ", lista_cumparaturi[-1])
# print("Lista noua: ", lista_cumparaturi)
# # 3. Daca "paine" exista in lista, sterge elementul
# if "paine" in lista_cumparaturi:
#     lista_cumparaturi.remove("paine")
# print("Lista dupa ce stergem paine: ", lista_cumparaturi)
# # 4. Sortam lista la final
# lista_cumparaturi.sort()
# for produs in lista_cumparaturi:
#     print(produs)

# Lista numere
numere = [10, -3, 5, 0, -11, 12, 7, -1]
# 1. Afiseaza toate numerele
# 2. O lista doar cu numere pozitive
# 3. o lista doar cu numere negative
# 4. Suma numerelor pozitive
# 5. Sorteaza descrescator lista cu numere pozitive

# 1.
print("toate numerele:")
for numar in numere:
    print(numar)
# 2 & 3
pozitive = []
negative = []

for numar in numere:
    if numar >= 0:
        pozitive.append(numar)
    elif numar < 0:
        negative.append(numar)
print("Numere pozitive: ", pozitive)
print("Numere negative: ", negative)

# 4.
suma_nr_pozitive = sum(pozitive)
print("Suma numerelor pozitive este: ", suma_nr_pozitive)

# 5.
print(pozitive)
pozitive.sort(reverse=True)
print(pozitive)