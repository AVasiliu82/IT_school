--serial
--text
--boolean
-- SERIAL -> folosit de obicei pentru coloanele ID
-- id SERIAL
-- PRIMARY KEY -> identifica unic fiecare rand
-- id SERIAL PRIMARY KEY
-- NOT NULL -> o coloana trebuie completata obligatoriu
-- nume TEXT NOT NULL
-- UNIQUE -> o valoare nu are voie sa se repete, este unica
-- email TEXT UNIQUE
-- DEFAULT -> pune valoare implicita
-- activ BOOLEAN DEFAULT true

-- CREATE TABLE
create table if not exists cursanti (
	id serial primary key,
	nume text not null,
	oras text not null,
	email text unique not null,
	activ boolean default true

);

select * from cursanti
where oras = 'Timisoara'; -- arata-mi doar persoanele care sunt din Timisoara

insert into cursanti (nume, oras, email)
values ('Andrei Vasiliu', 'Arad', 'andrei.vasiliu@curs.ro');

insert into cursanti (nume, oras, email)
values
('Sorin-Bogdan Castravete-Balaita', 'Timisoara', 'sorin-bogdan.castravete-balaita@curs.ro'),
('Zeynep Yalcindag', 'Cluj-Napoca', 'zeynep.yalcindag@curs.ro');

select * from cursanti
order by nume desc; -- arata-mi randurile cu date descrescator

select * from cursanti
limit 2; -- arata-mi doar primele 2 randuri

update cursanti
set oras = 'Bucuresti'

select * from cursanti;

delete from cursanti
where id = 3;

delete from cursanti;

truncate table cursanti restart identity cascade;

-- foreign key

create table if not exists prezente (
	id serial primary key,
	cursant_id integer not null,
	data_curs date not null,
	prezent boolean default true,
	foreign key (cursant_id) references cursanti(id) on delete cascade
)

select * from prezente;

