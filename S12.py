# Lista - colectie ordonata si modificabila de elemente. Poate contine tipuri de date diferite: intregi, float, siruri, alte liste etc

lista_goala = []
lista_numere = [1, 2, 3, 4]
lista_mixt = [1, "text", 3.5, False]

# Accesarea elementelor
# Indexarea incepe de la 0
# Se poate folosi index negativ

# Slicing
# lista[start:stop:pas] - ia elementele de la indexul start pana la stop(fara sa il includem), din pas in pas
# start - pozitia de unde incepi(index) - exemplu: 2 va inseamna al 3 lea element
# stop - pozitia unde te opresti(nu se include acel element) - exemplu: 5 inseamna pana la al 6 lea element
# pas - cat sari de fiecare data(poate fi negativ) - exemplu: 2 inseamna din 2 in 2

# Exemple
lista = [1, 2, 3, 4, 5]
# print("Lista initiala: ", lista)
# print("1. lista[:] Copiaza toata lista: ", lista[:]) # Copiaza toata lista
# print("2. lista[1:4] De la al doilea la al patrulea element: ", lista[1:4])
# print("3. lista[::2] Toate elemente din 2 in 2: ", lista[::2])
# print("4. lista[1::2] Incepe de la indexul 1 si sare din 2 in 2: ", lista[1::2])
# print("5. lista[::-1] Listeaza invers: ", lista[::-1])
# print("6. lista[-3:] ", lista[-3:])
# print("6. lista[:-2] Toate, mai putin ultimele doua", lista[:-2])

# [:] - Copiaza lista intreaga
# [::] - La fel ca [:]
# [::2] - Din 2 in 2
# [::-1] - Lista inversata
# [1:4] - De la index 1 la 3
# [-3:] - Ultimele 3 elemente

# Ce inseamna accesare/indexare negativa
# Incepe de la -1(ultimul element), -2(al doilea elemnent) samd
# Poti accesa elemente de la sfarsitul listei fara sa stii exact lungimea ei
# Daca vrei totusi sa afli lungimea listei, folosim functia len(nume_lista)

# Accesare cu index negativ mai mare decat lungimea listei - Erroare - IndexError
#print(lista[6])

# Iterare prin lista
# for element in lista:
#     print(element)

# Daca vrem sa verificam existenta unui element in lista
# if 5 in lista:
#     print("Exista in lista")

# matrice / liste imbricate / nested lists / lista in lista

# matrice = [
#     [1, 2],
#     [3, 4]
# ]

#matrice = [[1, 2], [3, 4]]

matrice = [
    [1, 2, 3], # Linia 0, cu elementele 0, 1, 2
    [4, 5, 6], # Linia 1, cu elementele 0, 1, 2
    [7, 8, 9]  # Linia 2, cu elementele 0, 1, 2
]

# # Accesare elemente liste inlantuite
# # 1. Accesezi prima lista interioara
# print("1. matrice[0] accesam prima lista interioara: ", matrice[0])
# # 2. Accesez un element din lista interioara
# print("2. matrice[0][1] accesam al doilea element din prima lista interioara: ", matrice[0][1])
#
# print("3. Sub lista de pe linia 1, elementul de pe coloana 2: ", matrice[1][2])
# print("4. Sub lista de pe linia 2, elementul de pe coloana 1: ", matrice[2][1])
#
# # Modificarea unui element
# matrice[1][1] = 99
# print(matrice)

clase = [
    ["Ana", "Mihai", "Ioana"],
    ["George", "Maria", "Andrei"],
    ["Alex", "Diana", "Paul"]
] # Lista numita "clase" cu 3 sub-liste

# parcurgerea listei inlantuite cu for
# for clasa in clase:
#     print(clasa)
#
# # parcurgere element cu element
# for clasa in clase:
#     for element in clasa:
#         print(element)

# Exemplu
situatie_elevi = [
    ["Ana", 10, 9, 8],
    ["Mihai", 8, 8, 9],
    ["Ioana", 10, 10, 9]
]

# print(situatie_elevi)
#
# for elev in situatie_elevi:
#     nume = elev[0]
#     note_elev = elev[1:]
#
#     media = sum(note_elev) / len(note_elev)
#
#     print(f"{nume} are media: {media:.2f}")

# adaugare intr-o lista nested
# clase = [
#     ["Ana", "Mihai"],
#     ["George", "Maria"]
# ]
# print(clase)
# clase[0].append("Florin")
# print(clase)
#
# # adaugare lista noua
# clase.append(["Marius", "Cosmin"])
# print(clase)

matrice = [
    [1, 2, 3], # Linia 0, cu elementele 0, 1, 2
    [4, 5, 6], # Linia 1, cu elementele 0, 1, 2
    [7, 8, 9]  # Linia 2, cu elementele 0, 1, 2
]

# for i in range(len(matrice)):
#     print(matrice[i][i])
#
# #0 2  1 1  2 0
# n = len(matrice)
#
# for i in range(len(matrice)):
#     print(matrice[i][n - 1 - i])

# lista = [2, 6, 9, 11, 2, 20, 13, 76, 33, 8]
# # 1. Creeaza o lista cu 10 numere si afiseaza doar elementele de pe pozitiile pare
# # Varianta 1 - Roxana
# for i in range(0, len(lista), 2):
#     print(lista[i])
# # Varianta 2
# print("1. Elemente de pe pozitii pare: ",lista[::2])
# # 2. Adauga un element nou la sfarsitul listei
# print("2. Adauga un element nou la sfarsitul listei")
# lista.append(73)
# print(lista)
#
# # Varianta 2 - Andrei
# lista += [43]
# print(lista)
# # 3. Schimba al doilea element din lista cu 99
# lista[1] = 99
# print(lista)
# # 4. Afiseaza lungimea listei
# print(len(lista))
# # 5. Sorteaza lista crescator si apoi descrescator
# lista.sort()
# print(lista)
#
# lista.sort(reverse=True)
# print(lista)
# # 6. Inverseaza lista fara sa folosesti reverse()
# lista_inversata = lista[::-1]
# print(lista_inversata)


# 2. Folosind lista de mai jos, afiseaza doar cuvintele mai lungi de 3 litere si adauga-le intr-o lista noua
lista_cuvinte = ["studentii", "mei", "stiu", "Python", "foarte", "bine"]

lista_noua = []

for cuvant in lista_cuvinte:
    if len(cuvant) > 5:
        lista_noua.append(cuvant)
print("Cuvinte mai lungi de 3 litere: ", lista_noua)
