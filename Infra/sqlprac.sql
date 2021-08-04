use details;
create table details(id int auto_increment primary key,Fname varchar(20) NOT NULL,Lname varchar(20) NOT NULL,email varchar(30) NOT NULL default xyz@gmail.com,DOB date NOT NULL default 13-12-1992);
insert into details(Fname,Lname,email,DOB)values('Shavi','Singh','shavg@gmail.com','1990-06-09');
select concat(Fname,' ',Lname) as fullName from details;