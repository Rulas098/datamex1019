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

Create Table Customers (
 cr_id varchar(10),
 cr_name varchar (30),
 cr_phone varchar (15),
 cr_email varchar (30),
 cr_address varchar (30),
 cr_city varchar (15),
 cr_state varchar (20),
 cr_country varchar (20),
 cr_postal decimal (15),
 PRIMARY KEY (cr_id)
 );

create table salesperson(
 sp_id decimal(15),
 sp_name varchar(20),
 sp_store varchar(15),
 PRIMARY KEY (sp_id)
 );

create table invoices(
 inv_number decimal(20),
 inv_date varchar(20),
 inv_car decimal(5),
 inv_customer decimal(5),
 inv_salesperson decimal(5),
 PRIMARY KEY (inv_number)
 );

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
