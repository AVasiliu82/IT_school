# # Conditionale - if/else/elif
# # O conditie este o expresie care poate fi adevarata (True) sau falsa (False)
# # Pe baza ei, putem sa decide daca anumite blocuri de cod se vor executa sau nu
#
# # if conditie:
#       # codul se executa doar daca conditia este True
# # elif alta conditie:
# #   codul executa daca prima conditie nu a fost true, dar aceasta este
# # else:
# # codul se executa daca niciuna dintre conditii nu a fost adevarata/indeplinita
#
# # Exemplu 1:
#
# # varsta = 18
# # if varsta >= 18:
# #     print("Ai voie sa votezi")
# # else:
# #     print("Esti prea tanar ca sa votezi")
#
# # Python foloseste indentare pentru a sti ce cod apartine blocului if/else etc. Nu folosim acolade {} in alte limbaje
#
# # x = 11
# # if x > 10
# #     print("Mai mare")
# # print("Final")
#
# # 1. == -> egal cu
# # a = 5
# # b = 3
# # a == b -> Flase
#
# # 2. != -> diferit de
# # a != b -> True
#
# # 3. > -> mai mare decat
# # a > b -> True
#
# # 4. < -> mai mic decat
# # a < b -> False
#
# # 5. >= -> mai mare sau egal
# # a >= b -> True
#
# # 6. <= -> mai mic sau egal
# # a <= b -> False
#
# # 1. Egal cu - ==
# x = 5
# if x == 55:
#     print("x este egal cu 5")
#
# # 2. Diferit de - !=
# if x != 10:
#     print("x NU este egal cu 10")
#
# # 3 Mai mare decat - >
# temperatura = 30
# if temperatura > 25:
#     print("afara este cald")
#
# # 4 Mai mic decat - <
# elevi = 18
# if elevi < 20:
#     print("Clasa este mica")
#
# # 5. Mai mare sau egal
# varsta = 10
# if varsta >= 18:
#     print("Ai voie sa votezi")
#
# # 6. Mai mic sau egal
#
# pret = 99
# if pret <=99:
#     print("Produsul este ieftin")
#
# # Operatori logici
#
# # 1. AND -> ambele conditii trebuie sa fie true
# # 2. OR -> cel putin una din conditii trebuie sa fie true
# # 3. NOT -> inverseaza valoarea - True -> False
#
# # 1. AND
# varsta = 20
# nationalitate = "roman"
#
# if varsta > 18 and nationalitate == "roman":
#     print("Poti vota in Romania")
# else:
#     print("Nu poti vota in Romania")
#
# # 2. OR
# zi = "sambata"
#
# if zi == "sambata" or zi == "duminica":
#     print("este weekend")
#
# # 3. NOT
# ploua = False
#
# if not ploua:
#     print("vremea este frumoasa")
#
# # if not -> aceasta este o verificare de tip "falsy" . Python interpreteaza valoarea lui "x" in contextul de adevar sau fals
# # if x: verifica daca x este adevarat (truthy)
# # if not x: verifica daca x este fals (False)
#
# # Ce valori sunt considerate fals in Python
# # Toate vor face ca not x sa fie True, adica sa execute codul din interior if:
#
# # 1. None
# # 2. False
# # 3. 0 (orice numar 0)
# # 4. '' -> str gol
# # 5. [] -> lista goala
# # 6. {} -> dictionar gol
# # 7. set() -> set gol
# # 8.() -> tupplu gol
#
# # Exemple concrete
#
# x = 0
# print(bool(x))
# print(not x)
# if not x:
#     print("Este zero")
#
# x = ""
# if not x:
#     print("String gol")
#
# x = [1, 2, 3]
# if not x:
#     print("Lista este goala") # NU se va afisa, lista contine elemente
#
# # ALte modalitati de a scrie if
#
# # 1. If pe o singura linie
# x = 3
# if x % 2 != 0: print ("Numar impar")
#
# # 2. If termar (pe o singura linie - inlocuieste if/else)
# x = 7
# rezultat = "Par" if x % 2 == 0 else "Impar"
# print(rezultat)
#
# if x % 2 == 0:
#     rezultat = "Par"
# else:
#     rezultat = "Impar"
# print(rezultat)
#
# # 3. if cu in (verificare apartenenta
# litera = 'b'
# if litera in "aeiou":
#     print("este vocala")
# else:
#     print("este consoana")
#
# # 4. if cu bool() (conditie implicita)
#
# nume = "Maria"
# if nume:
#     print("Ai introdus un nume")
#
# # 5. if comparativ cu mai multe valori
#
# x = 7
# if 5 < x < 10:
#     print("x este intre 5 si 10")
#
# # Neste if - if in interiorul altui if - folosit pentru mai multe niveluri de verificare
#
# varsta = int(input("Introdu varsta ta: "))
#
# if varsta >= 18:
#     print("Esti adult")
#
#     if varsta >= 65:
#         print("Esti pensionar")
#     else:
#         print("Inca muncesti")
#
# else:
#     print("Esti minor")


# Exercitii :

# 1. Citeste un numar de la tastatura sau introdu un numar de la tastatura

# numar = int(input("Introdu numar: "))
#
# if numar % 2 == 0:
#     print("Par")
# else:
#     print("Impar")

# 2. Afiseaza daca un numar introdus este pozitiv/ negativ sau zero

# numar_1 = int(input("Valoare: "))
#
# if numar_1 == 0:
#     print("Este zero")
# elif numar_1 > 0:
#     print ("Pozitiv")
# else:
#     print("Negativ")

# 3. Verifica daca un numar introdus de la tastatura este intre 1 si 100, inclusiv

# numar_2 = int(input("Introdu un numar: "))
#
# if numar_2 > 1 and numar_2 <= 100:
#     print("In interval")
# else:
#     print("Inafara intervalului")

# if 1 < numar_2 <= 100:
#     print("In interval")
# else:
#     print("Inafara intervalului")
#

# 4. Daca temperatura este sub 0 - ger; intre 0-15 - frig; intre 16-25 - placut; peste 25 - cald

temperatura = int(input("Mentioneaza temperatura de afara: "))

if temperatura < 0:
    print("Ger")
elif temperatura >= 0 and temperatura <= 15:
    print("Frig")
elif temperatura >= 16 and temperatura <= 25:
    print("Placut")
elif temperatura > 25:
    print("Cald")
else:
    print("De ce?")












