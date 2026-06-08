# Functia open() - deschidem fisierul
# Sintaxa:
#fisier = open("nume_fisier.txt", "mod_de_deschidere")

# Exemplu:
#fisier = open("date.txt", "r")

# Moduri deschidere fisiere
# r - read - citire, daca fisierul nu exista, da eroare
# w - write - daca fisierul nu exista, il creeaza; scrie in fisier si sterge continutul vechi
# a - append - adauga la finalul fisierului fara sa stearga continutul
# x - create - creeaza un fisier nou, dar va da eroare daca exista deja

# Citirea unui fisier
# fisier = open("date.txt", "r")
# continut = fisier.read()
# print(type(continut))
# print(continut)
# fisier.close()

# Citire cu readline()
# fisier = open("date.txt", "r")
# rand1 = fisier.readline()
# rand2 = fisier.readline()
# print(rand1)
# print(rand2)
# fisier.close()

# Daca incerci sa folosesti functia read de doua ori consecutiv
# fisier = open("date.txt", "r")
# rand1 = fisier.read()
# rand2 = fisier.read()
# print(rand1)
# print(rand2)
# fisier.close()

# Citire cu readlines()
# fisier = open("date.txt", "r")
# linii = fisier.readlines()
#
# print(linii)
#
# fisier.close()

# parcurgere cu for
# fisier = open("date.txt", "r")
#
# for linie in fisier:
#     print(linie.strip()) # strip() - sterge spatiile goale din fisier
#
# fisier.close()

# Scriere in fisier cu w
# fisier = open("date_pentru_write.txt", "w")
# fisier.write("Prima linie din fisierul pentru scriere\n")
# fisier.write("Curs Python IT School 2026\n")
# # fisier.write("""Primul rand
# # Al doilea rand
# # Al treilea rand""")
# fisier.close()

# Adaugare in fisier cu append "a"
# fisier = open("date_pentru_append.txt", "a")
#
# fisier.write("Exemplu fisier creat si linie adaugata cu append\n")
#
# fisier.close()

# Diferenta intre write si append
# 1. Daca folosim write: continutul vechi va fi sters; cu append: se pastreaza continutul vechi si se adauga cel nou pe ultima linie

# Context manager - citire
# with open("date.txt", "r") as fisier: # Cand folosim context manager, inchiderea se face automat, deci nu mai e nevoie de functia close()
#     continut = fisier.read()
# print(continut)

# Scriere in fisier cu with open
# with open("date_pentru_write.txt", "w") as fisier:
#     fisier.write("Prima linie\n")
#     fisier.write("A doua linie\n")

# Append in fisier cu with open
# with open("date_pentru_append.txt", "a") as fisier:
#     fisier.write("Linie adaugata cu append folosind context manager\n")

# with open("date_pentru_append.txt", "a", encoding = "utf-8") as fisier: # pentru caractere speciale, este util sa adaugam un parametru nou in with open: encoding = "utf-8"
#     fisier.write("ĂÂÎȘȚăâîșț\n")

# Exemple

# 1. Salvam un nume introdus de la tastatura intr-un fisier
# nume = input("Adauga nume: ")
#
# with open("fisier_nume.txt", "a") as fisier:
#     fisier.write(f"{nume}\n")
#     # fisier.write(nume + "\n")

# 2. Citim toate persoanele
# with open("fisier_nume.txt", "r") as fisier:
#     for linie in fisier:
#         nume = linie.strip()
#         print(nume)
#         print(type(nume))
#         print(len(nume))
#     # nume = fisier.read()
#     # print(nume)
#     # print(len(nume))

# 3. Verificam daca un nume exista in fisier, folosind input
# nume_cautat = input("Nume cautat: ")
# nume_gasit = False
#
# with open("fisier_nume.txt", "r") as fisier:
#     for nume in fisier:
#         nume = nume.strip()
#         nume = nume.lower()
#         if nume_cautat == nume:
#             nume_gasit = True
#             break
# if nume_gasit:
#     print(f"Nume gasit: {nume_cautat}")
# else:
#     print("Numele nu exista in fisier")

# 4. Scriere valori multiple in fisier
# produs = input("Nume produs: ")
# pret = input("Pret produs: ")
#
# with open("fisier_magazin.txt", "a") as fisier:
#     fisier.write(f"{produs},{pret}\n")

# Daca vrem sa verificam existenta unui produs si sa ii afisam pretul
# produs_cautat = input("Produs cautat: ")
#
# produs_gasit = False
#
# with open("fisier_magazin.txt", "r") as fisier:
#     for produs in fisier:
#         produs = produs.strip()
#
#         separator = produs.split(",")
#         produs = separator[0]
#         pret = separator[1]
#
#         if produs == produs_cautat:
#             print(f"Pretul produsului {produs} este {pret} RON")
#             produs_gasit = True
#             break
#
# if produs_gasit == False:
#     print("Produsul nu exista")

# 5. Creeaza un program pentru o lista de cumparaturi
# 1. Creare meniu: 1. Adauga produs; 2. Afiseaza produse; 3. Sterge produs; 4. Iesire
# 2. pentru stergere produs: citeste toate produsele; pastreaza doar pe cele diferite; rescrie fisierul

# structura:
# 1. functie meniu
# 2. functie adaugare produs
# 3. functie afisare produse
# 4. functie stergere produs
# 5. functia unde rulezi programul

def meniu_principal():
    print("-------------")
    print("1. Adauga produs")
    print("2. Afiseaza produse")
    print("3. Sterge produs")
    print("4. Iesire")
    print("-------------")

def adauga_produs():
    produs = input("Adauga produs: ")

    with open("lista_cumparaturi.txt", "a") as fisier:
        fisier.write(produs + "\n")
    print("Produs adaugat")

def afisare_produse():
    with open("lista_cumparaturi.txt", "r") as fisier:
        produse = fisier.readlines()

        for produs in produse:
            produs = produs.strip()
            print(produs)

def stergere_produs():
    produs_sters = input("Sterge produsul: ")

    produse_ramase = []
    produs_gasit = False

    with open("lista_cumparaturi.txt", "r") as fisier:
        for produs in fisier:
            produs = produs.strip()

            if produs == produs_sters:
                produs_gasit = True
            else:
                produse_ramase.append(produs + "\n")
    if produs_gasit:
        with open("lista_cumparaturi.txt", "w") as fisier:
            for produs in produse_ramase:
                fisier.write(produs)
        print("Produs sters")
    else:
        print("Produsul nu exista")

def main():
    while True:
        meniu_principal()
        alege = input("Optiune meniu: ")

        if alege == "1":
            adauga_produs()
        elif alege == "2":
            afisare_produse()
        elif alege == "3":
            stergere_produs()
        elif alege == "4":
            break
        else:
            print("Optiune NOK")

main()