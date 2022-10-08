# Assignment 5 - Flask and DBs - mySQL

## Steps/details used witin this assignment
- I decided to using Azure as the cloud environment for this assignment. 
1. Create a VM instance with the following settings on Azure and launch 
    - 2 vCPUs and at least 4 GB of RAM as the minimum requirment mentioned by MySQL 
2. Use the command ``` sudo apt-get update ``` to get the VM up to date
3. Install MySQL with the command 
```sh 
sudo apt install mysql-server mysql-client
``` 
4. Log in to MySQL with 
```sh 
sudo mysql
```
5. Create a new user and confirm its creation 
```sh 
CREATE USER ‘USERNAME'@'%' IDENTIFIED BY ‘PASSWORD’;
```
```
select user from mysql.user;
```
6. Give the new user all privileges and confirm
```sh 
GRANT ALL PRIVILEGES ON *.* TO 'USESRNAME'@'%' WITH GRANT
OPTION;
```
```
show grants for dba;
```
7. Test the user connection
```sh 
mysql -u username -p 
```
8. Create a new database and confirm creation 
```sh 
CREATE database databasename
```
```
SHOW databases; 
```
9. For python to be able to connect properly a new inbound port for 3306 must be created first.
10. In addition to the new port the bind address must be changed to ```0.0.0.0``` with the following and restart mysql 
```sh 
sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf
```
```
/etc/init.d/mysql restart
```
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