# mysql-selfmanaged
 HHA 504  Assignment 5 - Flask and DBs - mySQL


# 
## Good MySQL to know 
To see the list of tables within selected database
```sh 
SHOW TABLES FROM 'DATABASE NAME';
``` 
View all databases 
```sh 
SHOW databases; 
```
Selecting a database to use commands on 
```sh 
USE 'DATABASE NAME'; 
```
Creating a new table within specific databse
```sh 
CREATE TABLE Persons (
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
);
```