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




"""
La intrarea intr-o parcare privata programul verifica mai multe masini
Pentru fiecare masina, se introduce:
1. Tipul vehiculului: auto, moto, camion
2. Daca are abonament: da / nu
3. Ora intrarii

Reguli:
1. camioanele nu ai voie dupa ora 18
2. motocicleta intra mereu
3. masinile fara anonament intra doar intre orele 08:00 si 20:00
4. pentru fiecare vehicul se afiseaza permis sau respins

foloseste for pentru mai multe vehicule
if pentru toate regulile
while pentru validare input
"""
# Rezolvare:

numar_masini = int(input("cate masini verifici:"))
for i in range(numai_masini)
    print("Vehicul numarul:", i+1)

tip = "" # text gol
while tip !=("auto" and tip !="moto" and tip != "camion")
    tip = input ("tipul vehicul(auto/moto/camion):")
    if tip != "auto" and tip != "moto" and tip !="camion"
        print("Tip invalid")

abonament = ""
while abonament != "da" and abonament!="nu":
    abonament = input ("Are abonamnet?:")
    if abonament != = "da" and abonaent !="nu":
        print("raspuns invalid")

ora = -1
while ora <0  ora >23;
    ora = int(input("Ora intrare:"))
    if ora < 0 or ora >23:
        print ("ora invalida")

are_voie=False

if tip =="camion":
    if ora  <18:
    are_voie=True
