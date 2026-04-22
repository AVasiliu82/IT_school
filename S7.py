import random

# Ce este WHILE in Python
# - Instructiunea WHILE este o structura de control care executa un bloc de cod atata timp cat o conditie este adevarata

# Sintaxa
#while conditie:
    # bloc de cod executat daca "conditie" este True

# Exemplu:
# x = 0
# while x < 5:
#     print(x)
#     x += 1

# 1. Conditia trebuie sa se schimbe
# x = 0
# while True:
#     print("aragaz")
# Daca nu modifici variabilele din conditie, vei crea o bucla infinita / loop inifinit

# 2. Comanda BREAK
# x = 0
# while True:
#     print("aragaz")
#     x += 1
#     if x == 30:
#         break

# 3. Comanda CONTINUE
# x = 0
# while x < 5:
#     x += 1
#     if x == 3:
#         continue
#     print(x)

# 4. else in while
# x = 0
# while x < 3:
#     print(x)
#     x += 1
# else:
#     print("WHILE s-a termiant in mod normal")
# Se executa doar daca bucla se incheie in mod normal (fara BREAK)

# Cazuri de utilizare

# 1. Numarare
# x = 10
# while x > 0:
#     print(x)
#     x -= 1

# 2. Asteptare pana la o conditie
# conditie = ""
# while conditie != "exit":
#     conditie = input("Scrie 'exit' pentru a iesi: ")

# 3. Validare input
# valoare = int(input("Introdu un numar pozitiv: "))
# while valoare <= 0:
#     valoare = int(input("Numar invalid. Reincearca: "))

# while True cu break
# while True:
#     comanda = input("Comanda: ")
#     if comanda == "stop":
#         break
#     print("Ai tastat:", comanda)

# Blocul try / except
# Folosit pentru gestionarea exceptiilor(pentru a prinde si trata erori care pot aparea in timpul rularii unui program) fara ca aceasta sa se opreasca brusc
# In loc sa crape tot progamul, try/except permite sa tratezi aceste situatii controlat

# Sintaxa
# try:
#     x = 10 / 0
# except ZeroDivisionError:
#     print("Nu poti imparti la zero")

# Exemplu:
# try:
#     numar = int(input("Introdu un numar: "))
#     print("Numarul este: ", numar)
# except ValueError:
#     print("Nu ai introdus un numar valid")
#
# Fara try / except - va afisa eroarea "ValueError"
# numar = int(input("Introdu un numar: "))
# print("Numarul este: ", numar)

# Ce se intampla daca nu specifici nimic
# try:
#     x = 1 / 0
# except:
#     print("A aparut o eroare")

# 1. Generare de numere prime
# Un numar este prim atunci cand se divide numai cu 1 si cu el insusi(ex; 2, 3, 5, 7, 11)

# numar = 2 # numarul pe care il verificam
# while numar <= 20: # cat timp numarul curent este mai mic sau egal cu 20, repeta instructiunile
#     divizor = 2 # Variabila cu care incercam sa impartim numarul
#     prim = True # Am pus True la inceput pentru ca presupunem ca numarul este prim
#     while divizor < numar: # Cat timp divizorul este mai mic decat numarul, verifica daca numarul se imparte exact la acel divizor
#         if numar % divizor == 0: # Verifica daca se divide exact. Daca se indeplineste, inseamna ca numar se divide exact la divizor
#             prim = False # numarul nu mai este prim
#             break # oprim imediat bucla INTERIOARA
#         divizor += 1 # daca nu s-a impartit exact, trecem la urmatorul divizor
#     if prim: # daca variabila prim este inca True, inseamna ca nu am gasit niciun divizor
#         print(numar)
#     numar += 1 # dupa verificare, trecem la urmatorul numar

# Ghiceste numarul - varianta fara modulul RANDOM
# numar_secret = 7
# ghicire = None
# while ghicire != numar_secret:
#     ghicire = int(input("Ghiceste numarul: "))
# print("Ai ghicit")

# Ghiceste numarul - varianta cu modulul RANDOM
# numar_secret = random.randint(1, 100)
# ghicire = None
# incercari = 0
# incercari_maxime = 5
#
# while ghicire != numar_secret and incercari <= incercari_maxime:
#     try:
#         ghicire = int(input("Ghiceste numarul(1 - 10). Ai 3 incercari: "))
#         incercari += 1
#         if ghicire < numar_secret:
#             print("Numarul este mai mare")
#         elif ghicire > numar_secret:
#             print("Numarul este mai mic")
#     except ValueError:
#         print("Introdu un numar valid")
#         continue
# if ghicire == numar_secret:
#     print(f"Ai ghicit din {incercari} incercari")
# else:
#     print(f"Ai pierdut, numarul era: {numar_secret}")


# Exercitiu:
# Simulator bancomat
# Avem un sold initial de 1000 LEI. Vrem sa afisam un meniu:
# 1. Vezi sold
# 2. Depune bani
# 3. Retrage bani
# 4. Iesire
# Reguli:
# 1. Meniul trebuie repetat pana cand userul alege iesirea
# 2. la retragere, nu ai voie sume mai mari decat soldul
# 3. Fara sume negative sau zero
# 4. dupa fiecare operatie afisezi soldul nou

sold = 1000.0
aplicatia_ruleaza = False
pin_corect = "1234"
incercari_maxime = 3
autentificat = False

incercari = 0
while incercari < incercari_maxime:
    pin_introdus = input("Introdu PIN: ")

    if len(pin_introdus) != 4:
        print("PIN trebuie sa contina 4 cifre")
        incercari += 1
        incercari_ramase = incercari_maxime - incercari
        print(f"Incercari ramase: {incercari_ramase}")
        continue

    if pin_introdus == pin_corect:
        print("Autentificare OK")
        autentificat = True
        break
    else:
        incercari = incercari + 1
        incercari_ramase = incercari_maxime - incercari
        print("PIN incorect")
        print(f"Incercari ramase: {incercari_ramase}")

if autentificat == False:
    print("Card blocat. Prea multe incercari")

if autentificat == True:
    aplicatia_ruleaza = True
    while aplicatia_ruleaza:
        print("\n**** MENIU ****")
        print("1. Vezi sold")
        print("2. Depune bani")
        print("3. Retrage bani")
        print("4. Iesire")
        print("*****************\n")

        optiune = input("Alege o optiune (1-4): ")

        if optiune == "1":
            print(f"Soldul curent este: {sold:.2f} LEI")
        elif optiune == "2":
            suma_text = input("Introdu suma pe care vrei sa o depui: ")
            try:
                suma = float(suma_text)
                if suma <= 0:
                    print("Suma introdusa trebuie sa fie mai mare decat 0")
                else:
                    sold = sold + suma
                    print(f"Ai depus {suma:.2f} LEI")
                    print(f"Noul sold este {sold:.2f} LEI")
            except ValueError:
                print("valoare invalida. Introdu un numar valid")
        elif optiune == "3":
            suma_text = input("Introdu suma pe care vrei sa o retragi: ")
            try:
                suma = float(suma_text)
                if suma <= 0:
                    print("Suma introdusa trebuie sa fie mai mare decat 0")
                elif suma > sold:
                    print("Fonduri insuficiente")
                else:
                    sold = sold - suma
                    print(f"Ai retras {suma:.2f} LEI")
                    print(f"Noul sold este {sold:.2f} LEI")
            except ValueError:
                print("valoare invalida. Introdu un numar valid")
        elif optiune == "4":
            print("Iesire din meniu")
            aplicatia_ruleaza = False
        else:
            print("Optiune invalida")



