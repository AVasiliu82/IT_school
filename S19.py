import json
"""
Lucram intr-o companie care are date salvate in JSON, noi trebuie sa scrie diferite scripturi care citesc datele,
le modifica si genereaza rapoarte

Task 1: HR are un fisier JSON cu angajatii firmei, Vor un raport cu angajatii activi si inactivi
Task 2: Firma mareste salariile din dep de IT cu 10%
Task 3: Support IT. Echipa de support are un fisier cu tichete. Afisam doar tichetele urgente care inca nu sunt rezolvate
Task 4: Support IT. Managerul cere un raport care sa arate cate tichete are fiecare persoana asignata
    1. citim ticetele
    2. numaram cate tchete are fiecare persoana asignata
    3. generam un dictionar cu cheia fiind numele persoanei si valoarea: numarul de tichete asignate
    4. salvam in JSON nou tichete_per_angajat.json
Task 5: Dep de vanzari are un fisier cu comenzi. Ei vor sa stie valoarea totala a comenzilor
    1. citim comenzile
    2. pentru fiecare comanda: total_price = quantity * unit_price
    3. adaugam cheia total_price in fiecare comanda
    4. salvam rezultatul in comenzi_total.json
    5. afisam valoarea totala a comenzilor

"""

"""
Task 1 cerinta:
1. citim angajatii din JSON
2. separam angajatii activi de cei inactivi
3. afisam angajatii inactivi
4. -||- activi
5. afisam totalurile; afiseaza o lista de angajati
6. salvam in doua fisiere: angajati_activi.json / angajati_inactivi.json
"""

# 1. ***********************
def load_employees():
    with open("angajati.json", "r", encoding = "utf-8") as file:
        employees = json.load(file)
    return employees

def split_status_employees(employees):
    active_employees = []
    inactive_employees = []

    for employee in employees:
        if employee["active"] == True:
            active_employees.append(employee)
        else:
            inactive_employees.append(employee)
    return active_employees, inactive_employees

def display_employees(title, employees):
    print(title)

    for employee in employees:
        print(f"{employee["name"]} - {employee["department"]} - {employee["role"]}")

def save_employees(file_name, employees):
    with open(file_name, "w", encoding = "utf-8") as file:
        json.dump(employees, file, indent = 4)

"""
Task 2 cerinta:
1. Citim angajatii
2. marim cu 10% salariul doar pentru angajatii din dep de IT si care sunt activi
3. flag cu salary_updated = True pentru cei modificati
4. flag cu salary_updated = False pentru restul
5. salvam rezultatul in angajati_nou.json
"""

def load_employees():
    with open("angajati.json", "r", encoding = "utf-8") as file:
        employees = json.load(file)
    return employees

def increase_it_salary(employees):
    for employee in employees:
        if employee["department"] == "IT" and employee["active"] == True:
            old_salary = employee["salary"]
            new_salary = old_salary + old_salary * 10 / 100
            employee["salary"] = new_salary
            employee["salary_updated"] = True
        else:
            employee["salary_updated"] = False
    return employees

def updated_employees_count(employees):
    updated_counter = 0

    for employee in employees:
        if employee["salary_updated"] == True:
            updated_counter += 1

    return updated_counter

def save_employees(file_name, employees):
    with open(file_name, "w", encoding = "utf-8") as file:
        json.dump(employees, file, indent = 4)

"""
Task 3 cerinta:
1. Citim tichetele
2. pastram tichetele cu priority = high si status = open
3. afisam tichetele urgente
4. afisam totalul lor
5. salvam rezultatul in tichete_urgente.json
"""


def load_tickets():
    with open("tichete.json", "r", encoding="utf-8") as file:
        tickets = json.load(file)
    return tickets


def filter_urgent_open_tickets(tickets):
    urgent_tickets = []

    for ticket in tickets:
        if ticket["status"] == "open" and ticket["priority"] == "high":
            urgent_tickets.append(ticket)

    return urgent_tickets

def display_tickets(title, tickets):
    print(title)
    for ticket in tickets:
        print(f"{ticket["id"]} - {ticket['title']} - {ticket['assigned_to']}")

def save_tickets(file_name, tickets):
    with open(file_name, "w", encoding = "utf-8") as file:
        json.dump(tickets, file, indent = 4)


def main():
    """
    Task 1
    """
    # # citim angajatii din fisier
    # employees = load_employees()
    #
    # # separam angajatii in doua liste, returnam doua valori deci folosim doua variabile
    # active_employees, inactive_employees = split_status_employees(employees)
    #
    # # afisam angajatii activi
    # display_employees("Angajati activi", active_employees)
    #
    # # angajatii inactivi
    # display_employees("Angajati inactivi", inactive_employees)
    #
    # # afisam totalul de angajati activi
    # print("Total angajati activi: ", len(active_employees))
    #
    # # afisam totalul de angajati inactivi
    # print("Total angajati inactivi: ", len(inactive_employees))
    #
    # # salvam angajatii activi in fisier JSON nou
    # save_employees("angajati_activi.json", active_employees)
    #
    # # salvam angajatii inactivi in fisier JSON nou
    # save_employees("angajati_inactivi.json", inactive_employees)

    """
    Task 2
    """
    # # 1. Citim angajatii
    # employees = load_employees()
    #
    # # 2. aplicam marirea
    # updated_employees = increase_it_salary(employees)
    #
    # # 4. salvam rezultatul in fisier nou
    # save_employees("angajati_nou.json", updated_employees)
    #
    # # 3. cati angajati au fost modificati
    # updated_counter = updated_employees_count(updated_employees)
    #
    # print("Angajati actualizati: ", updated_counter)

    """
    Task 3
    """
    # 1. citim toate tichetele
    tickets = load_tickets()

    # 2. pastram doar tichetele cu prio high
    urgent_tickets = filter_urgent_open_tickets(tickets)

    # 3. afisam tichetele urgente
    display_tickets("Tichete urgente: ", urgent_tickets)

    # 4. afisam total tichete urgente
    print("Total tichete urgente: ", len(urgent_tickets))

    # 5. salvam tichetele urgente in fisier nou
    save_tickets("tichete_urgente.json", urgent_tickets)

main()


