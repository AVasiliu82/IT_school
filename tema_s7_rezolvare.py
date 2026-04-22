"""
Se cere de la tastatura o parola
Sa se verifice daca este puternica

Parola este considerata buna daca:
1. are cel putin 8 caractere
2. contine cel putin o cifra
3. contine cel putin o litera mare
4. contine cel putin o litera mica

Trebuie sa se afiseze "parola este puternica" sau ce conditii lipsesc

aditional
pentru a verifica daca un caracter este o cifra folosim functia .isdigit()
ex: if caracter.isdigit()

pentru a verifica daca un caracter este litera mare folosim functia .isupper()
ex: if caracter.isupper()

pentru a verifica daca un caracter este litera mica folosim functia .islower()
ex: if caracter.islower()
aveti nevoie de if si for
"""
# Rezolvare:

# parola = input("Introdu o parola: ")
#
# are_8 = False
# are_cifra = False
# l_mica = False
# l_mare = False
#
# if len(parola) >= 8: # verifica lungimea
#     are_8 = True
#
# # verifica fiecare caracter cu for
# for c in parola:
#     if c.isdigit():
#         are_cifra = True
#     if c.isupper():
#         l_mare = True
#     if c.islower():
#         l_mica = True
#
# # verificam fiecare conditie
# if are_8 and are_cifra and l_mare and l_mica:
#     print("Parola este buna")
# else:
#     if not are_8:
#         print("Parola nu are minim 8 caractere")
#     if not are_cifra:
#         print("Parola nu are cifre")
#     if not l_mare:
#         print("Parola nu are litere mari")
#     if not l_mica:
#         print("Parola nu are litera mica")

"""
Programul cere de la 5 utilizatori cate o nota pentu un produs, intre 1 si 5
Trebuie sa se afiseze:
1. cate note de 1, 2, 3, 4, 5 exista
2. media notelor
3. daca produsul este:
    - slab - daca media < 2.5
    - acceptabil - daca media este intre 2.5 si 4
    - excelent daca media > 4
reguli:
1. daca cineva introduce o nota invalida, trebuie ceruta din nou
2. foloseste while pentru validarea notei
3. for pentru cei 5 utilizatori
4. if pentru clasificare
"""
# Rezolvare:

# notam notele produsului
# numar_1 = 0
# numar_2 = 0
# numar_3 = 0
# numar_4 = 0
# numar_5 = 0
# suma = 0
#
# for i in range(5):
#     nota = 0
#     while nota < 1 or nota > 5:
#         nota = int(input("Utilizatorul " + str(i+1) + ", nota (1- 5): "))
#         if nota < 1 or nota > 5:
#             print("Nota invalida")
#
#     if nota == 1:
#         numar_1 += 1
#     if nota == 2:
#         numar_2 += 1
#     if nota == 3:
#         numar_3 += 1
#     if nota == 4:
#         numar_4 += 1
#     if nota == 5:
#         numar_5 += 1
#
#     suma = suma + nota
#
# print("Note de 1: ", numar_1)
# print("Note de 2: ", numar_2)
# print("Note de 3: ", numar_3)
# print("Note de 4: ", numar_4)
# print("Note de 5: ", numar_5)
#
# media = suma / 5
# print("Media este: ", media)
#
# if media < 2.5:
#     print("produsul este slab")
# elif media <= 4:
#     print("Produsul este acceptabil")
# else:
#     print("Produsul este excelent")


"""
La intrarea intr-o parcare privata programul verifica mai multe masini
Pentru fiecare masina, se introduce:
1. Tipul vehiculului: auto, moto, camion
2. Daca are abonament: da / nu
3. Ora intrarii

Reguli:
1. camioanele nu au voie dupa ora 18
2. motocicleta intra mereu
3. masinile fara abonament intra doar intre orele 08:00 si 20:00
4. pentru fiecare vehicul se afiseaza permis sau respins

foloseste for pentru mai multe vehicule
if pentru toate regulile
while pentru validare input
"""
# Rezolvare:

numar_masini = int(input("cate masini verifici: "))

for i in range(numar_masini):
    print("Vehicul nr: ", i+1)

    tip = ""
    while tip != "auto" and tip != "moto" and tip != "camion":
        tip = input("Tip vehicul (auto/moto/camion): ")
        if tip != "auto" and tip != "moto" and tip != "camion":
            print("Tip invalid")

    abonament = ""
    while abonament != "da" and abonament != "nu":
        abonament = input("Are abonament?: ")
        if abonament != "da" and abonament != "nu":
            print("Raspuns invalid")

    ora = -1
    while ora < 0 or ora > 23:
        ora = int(input("Ora intrare: "))
        if ora < 0 or ora > 23:
            print("Ora invalida")

    are_voie = False

    if tip == "camion":
        if ora < 18:
            are_voie = True
    elif tip == "moto":
        are_voie = True
    elif tip == "auto":
        if abonament == "da":
            are_voie = True
        elif ora >= 8 and ora < 20:
            are_voie = True
    if are_voie == True:
        print("acces permis")
    else:
        print("Acces respins")

