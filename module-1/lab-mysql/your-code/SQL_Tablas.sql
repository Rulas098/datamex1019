Create Table Cars

use lab_sqlcars;
CREATE TABLE cars(
 cs_id varchar(3),
 cs_VIN varchar(30),
 cs_Manufacturer varchar(15),
 cs_Model varchar (30),
 cs_Year varchar (4),
 cs_Color varchar (15),
 PRIMARY KEY (cs_id)
 );

insert into (cs_id, cs_VIN, cs_Manufacturer, cs_Model, cs_Year, cs_Color) 
values ("0",	"3K096I98581DHSNUP",	"Volkswagen",	"Tiguan",	"2019",	"Blue")
("1",	"ZM8G7BEUQZ97IH46V",	"Peugeot",	"Rifter"	"2019",	"Red"
("2",	"RKXVNNIHLVVZOUB4M",	"Ford",		"Fusion",	"2018",	"White"
("3",	"HKNDGS7CU31E9Z7JW",	"Toyota",	"RAV4",	"2018",	"Silver"
("4",	"DAM41UDN3CHU2WVF6",	"Volvo",	"V60",	"2019",	"Gray"
("5",	"DAM41UDN3CHU2WVF6",	,"Volvo",	"V60 Cross Country",	"2019",	"Gray")

Create Table Customers (
 cr_id decimal (10),
 cr_name varchar (30),
 cr_phone varchar (20),
 cr_email varchar (30),
 cr_address varchar (30),
 cr_city varchar (15),
 cr_state varchar (20),
 cr_country varchar (20),
 cr_postal decimal (15),
 PRIMARY KEY (cr_id)
 );

insert into(cr_id, cr_name, cr_phone, cr_email, cr_address, cr_city, cr_state, cr_country, cr_postal)
(10001,	"Pablo Picasso",	"+34 636 17 63 82",	null,	"Paseo de la Chopera 14",	"Madrid",	Madrid	Spain	28045)
(20001, "Abraham Lincoln",	"+1 305 907 7086",	null,	"120 SW 8th St	Miami",	"Florida",	"United States",	33130)
(30001,	"Napoléon Bonaparte",	"+33 1 79 75 40 00",	null,	"40 Rue du Colisée",	"Paris",	"Île-de-France",	"France",	75008)

create table salesperson(
 sp_id decimal(15),
 sp_name varchar(20),
 sp_store varchar(15),
 PRIMARY KEY (sp_id)
 );

insert into (sp_id, sp_name, sp_store)
values (00001,	"Petey Cruiser",	"Madrid")
(00002,	"Anna Sthesia",	"Barcelona")
(00003,	"Paul Molive",	"Berlin")
(00004,	"Gail Forcewind",	"Paris")
(00005,"Paige Turner",	"Mimia")
(00006,	"Bob Frapples",	"Mexico City")
(00007,	"Walter Melon",	"Amsterdam")
(00008,	"Shonda Leer",	"São Paulo")

create table invoices(
 inv_number decimal(20),
 inv_date varchar(20),
 inv_car decimal(5),
 inv_customer decimal(5),
 inv_salesperson decimal(5),
 PRIMARY KEY (inv_number)
 );

insert into (inv_number, inv_date, inv_car, inv_customer, inv_salesperson)
values (852399038,	"22-08-2018",	0,	1,	3,)
(731166526,	"31-12-2018",	3,	0,	5,)
(271135104,	"22-01-2019",	2,	2,	7,)





BONUS

UPDATE customer
SET cr_email = "ppicasso@gmail.com"
WHERE cr_name = "Pablo Picasso";

UPDATE customer
SET cr_email = "lincoln@us.gov"
WHERE cr_name = "Abraham Lincoln";

UPDATE customer
SET cr_email = "hello@napoleon.me"
WHERE cr_name = "Napoleon Bonaparte";

DELETE from cars where cs_Model = "V60";

select * from cars;
