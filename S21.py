import psycopg2

# SQL -> Structured Query Language

# tabel in sql -> structura in care pastram un tip de informatie

# coloana -> proprietatea datelor

# randuri -> o inregistrare concreta din tabel

# tipuri de date in sql
# integer -> numar intreg
# serial -> numar intreg generat automat
# varchar -> text cu lungime limitata
# text -> text mai lung
# date -> data calendaristica
# boolean -> true/false
# numeric -> numar cu zecimale

# PRIMARY KEY -> identificator unic pentru fiecare rand din tabel
# FOREIGN KEY -> legatura intre doua tabele

# o tabela cu toate datele -> NOK
# id, nume_cursant, email, data, prezent

# tabela cursanti
# id, nume, email
# tabela prezente
# id, cursant_id, data, prezent

# pip install psycopg2-binary

# host
# database
# user
# pass
# port

def create_connection():
    connection = psycopg2.connect(
        host = "localhost",
        database = "postgres",
        user = "postgres",
        password = "admin",
        port = "5433"
    )

    return connection

def create_cursanti_table():
    connection = create_connection()

    # cursor este obiectul prin care trimitem comenzi de SQL catre baza de date
    cursor = connection.cursor()

    # scriem comanda SQL
    sql = """
    CREATE TABLE IF NOT EXISTS cursanti (
        id SERIAL PRIMARY KEY,
        nume TEXT NOT NULL,
        oras TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        activ BOOLEAN DEFAULT true
    );
    """

    # executam comanda SQL
    cursor.execute(sql)

    # salvam modificarile in baza de date
    # pentru comenzile: create, insert, update, delete -> avem nevoie de commit
    connection.commit()

    cursor.close()

    # inchidem conexiunea
    connection.close()

def create_prezente_table():
    connection = create_connection()

    # cursor este obiectul prin care trimitem comenzi de SQL catre baza de date
    cursor = connection.cursor()

    # scriem comanda SQL
    sql = """
    CREATE TABLE IF NOT EXISTS prezente (
        id SERIAL PRIMARY KEY,
        cursant_id INTEGER NOT NULL,
        data_curs DATE NOT NULL,
        prezent BOOLEAN DEFAULT TRUE,
        FOREIGN KEY (cursant_id) REFERENCES cursanti(id) ON DELETE CASCADE
    );
    """

    # executam comanda SQL
    cursor.execute(sql)

    # salvam modificarile in baza de date
    # pentru comenzile: create, insert, update, delete -> avem nevoie de commit
    connection.commit()

    cursor.close()

    # inchidem conexiunea
    connection.close()

def insert_cursant(nume, oras, email):
    connection = create_connection()
    cursor = connection.cursor()

    sql = """
    INSERT INTO cursanti (nume, oras, email)
    VALUES (%s, %s, %s)
    ON CONFLICT (email) DO NOTHING;
    """

    cursor.execute(sql, (nume, oras, email))
    connection.commit()
    cursor.close()
    connection.close()
    #print("Cursantul a fost adaugat")

def afiseaza_cursanti():
    connection = create_connection()
    cursor = connection.cursor()
    sql = """
        SELECT * FROM cursanti
        ORDER BY id;
          """

    cursor.execute(sql)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    connection.close()

def insert_all_cursanti():
    cursanti = [
        ("Sorin-Bogdan Castravete-Balaita", "Timisoara", "sorin-bogdan.castravete-balaita@curs.ro"),
        ("Andrei Vasiliu", "Arad", "andrei.vasiliu@curs.ro"),
        ("Zeynep Yalcindag", "Cluj-Napoca", "zeynep.yalcindag@curs.ro"),
        ("Alexandru-Ionut Petraru", "Oradea", "alexandru-ionut.petraru@curs.ro"),
        ("Alexandru Cosac", "Iasi", "alexandru.cosac@curs.ro"),
        ("Corneliu Badelita", "Brasov", "corneliu.badelita@curs.ro"),
        ("Ligia Roberta Iacobescu", "Sibiu", "ligia.roberta.iacobescu@curs.ro"),
        ("Nicoleta Mehedintu", "Craiova", "nicoleta.mehedintu@curs.ro"),
        ("Manuela-Denisa Enache", "Constanta", "manuela-denisa.enache@curs.ro"),
        ("Roxana-Elena Brănescu", "Pitesti", "roxana-elena.branescu@curs.ro"),
        ("Andreea-Alexandra Ambrozi", "Targu Mures", "andreea-alexandra.ambrozi@curs.ro"),
        ("Eduard Marius Nagy", "Baia Mare", "eduard.marius.nagy@curs.ro"),
        ("Malina Marcu", "Alba Iulia", "malina.marcu@curs.ro"),
        ("Alin Cuculescu", "Buzau", "alin.cuculescu@curs.ro"),
        ("Ioan-Albert Flusca", "Deva", "ioan-albert.flusca@curs.ro"),
        ("Alexandar Roicov", "Resita", "alexandar.roicov@curs.ro")
    ]

    for cursant in cursanti:
        nume = cursant[0]
        oras = cursant[1]
        email = cursant[2]

        insert_cursant(nume, oras, email)

def select_cursanti_by_oras(oras_cautat):
    connection = create_connection()
    cursor = connection.cursor()

    sql = """
        SELECT * FROM cursanti
        WHERE oras = %s
        ORDER BY nume;
    """

    cursor.execute(sql, (oras_cautat, ))

    rows = cursor.fetchall()

    if len(rows) == 0:
        print("Nu exista persoane in orasul cautat")
    else:
        for row in rows:
            print(row)

    cursor.close()
    connection.close()

def search_cursanti_by_nume(nume_cautat):
    connection = create_connection()
    cursor = connection.cursor()

    search_value = "%" + nume_cautat + "%"

    sql = """
    SELECT * FROM cursanti
    WHERE nume ILIKE %s
    ORDER BY nume;
    """

    cursor.execute(sql, (search_value, ))
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    connection.close()

def update_cursant_oras(cursant_id, oras_nou):
    connection = create_connection()
    cursor = connection.cursor()

    sql = """
    UPDATE cursanti
    SET oras = %s
    WHERE id = %s;
    """

    cursor.execute(sql, (oras_nou, cursant_id))
    connection.commit()
    cursor.close()
    connection.close()

def deactivate_cursant(cursant_id):
    connection = create_connection()
    cursor = connection.cursor()

    sql = """
    UPDATE cursanti
    SET activ = false
    WHERE id = %s;
    """

    cursor.execute(sql, (cursant_id, ))
    connection.commit()
    cursor.close()
    connection.close()

def select_activ_cursanti():
    connection = create_connection()
    cursor = connection.cursor()

    sql = """
    SELECT * FROM cursanti
    WHERE activ = true
    ORDER BY nume;
    """

    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    connection.close()

#afiseaza_cursanti()

# 5. Filtreaza persoane dupa oras
# select_cursanti_by_oras("Arad")

# 6. Filtreaza persoane dupa nume
# search_cursanti_by_nume("Alexandru")

# 7. Update oras cursant
# update_cursant_oras(5, "Bucuresti")

# 8. Dezactivare persoana
#deactivate_cursant(5)
#search_cursanti_by_nume("Alexandru Cosac")

# 8. Filtrare doar cursantii activi
#select_activ_cursanti()

# 9. Adaugare prezenta pentru un cursant
def insert_prezenta(cursant_id, data_curs, prezent):
    connection = create_connection()
    cursor = connection.cursor()

    sql = """
        INSERT INTO prezente (cursant_id, data_curs, prezent)
        VALUES (%s, %s, %s);
    """

    cursor.execute(sql, (cursant_id, data_curs, prezent))
    connection.commit()
    cursor.close()
    connection.close()

#insert_prezenta(3, "20261110", True)

# 10. Afisare cursanti cu prezente
def select_cursanti_with_prezenta():
    connection = create_connection()
    cursor = connection.cursor()

    sql = """
    SELECT cursanti.nume, cursanti.email, prezente.data_curs, prezente.prezent
    FROM cursanti
    JOIN prezente ON cursanti.id = prezente.cursant_id
    WHERE cursanti.nume = 'Zeynep Yalcindag'
    ORDER BY cursanti.nume, prezente.data_curs;
    """

    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    connection.close()

select_cursanti_with_prezenta()




