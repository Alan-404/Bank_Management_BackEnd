CREATE DATABASE BANK_MANAGEMENT
USE BANK_MANAGEMENT

CREATE TABLE ROLE(
	ID INT PRIMARY KEY AUTO_INCREMENT,
    NAME NVARCHAR(50)
)

INSERT INTO ROLE (NAME) VALUES ('ADMIN')
INSERT INTO ROLE (NAME) VALUES ('MANAGER')
INSERT INTO ROLE (NAME) VALUES ('CUSTOMER')

SELECT * FROM ROLE

CREATE TABLE EMPLOYEE(
	ID VARCHAR(50) PRIMARY KEY,
	EMAILWORK VARCHAR(50) UNIQUE NOT NULL,
    USERID VARCHAR(20),
    FOREIGN KEY(USERID) REFERENCES USER(ID)
)



SELECT * FROM EMPLOYEE


INSERT INTO EMPLOYEE VALUES ('MANAGER_01', '152266633', 'Nguyễn', 'Đức', 'Alan', '2001-04-04', '0938671122','34A đường 43 phường 4 quận 4' ,'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSs8ZWfJV0IH_LCCSeZqOXiEpVbYrvE6p0QnfUvMq48XINsxmz-v5YwboD4sa9mJzhaioo&usqp=CAU','manager_01@bank.alan.porco.com', 2  )


CREATE TABLE ACCOUNT (
	ID INT PRIMARY KEY AUTO_INCREMENT,
    USERNAME VARCHAR(20) UNIQUE NOT NULL,
    PASSWORD TEXT NOT NULL,
    FOREIGN KEY (USERNAME) REFERENCES USER(ID)
)

drop table account

select * from account

select * from account

select * from user


select * from employee
select * from customer

select * from account

CREATE TABLE USER (
	ID VARCHAR(20) PRIMARY KEY,
    CID VARCHAR(20) UNIQUE NOT NULL,
    FIRSTNAME NVARCHAR(50) NOT NULL,
    MIDDLENAME NVARCHAR(50),
    LASTNAME NVARCHAR(50) NOT NULL,
    BDATE DATE,
    PHONE VARCHAR(12) UNIQUE,
    ADDRESS TEXT,
    AVATAR TEXT,
    EMAIL VARCHAR(100) UNIQUE,
    ROLE INT NOT NULL,
    FOREIGN KEY(ROLE) REFERENCES ROLE(ID)
)

CREATE TABLE CUSTOMER(
	ID INT PRIMARY KEY AUTO_INCREMENT,
	USERID VARCHAR(20),
    TRANSACTION ARRAY,
    FOREIGN KEY(USERID) REFERENCES USER(ID)
)

DROP TABLE CUSTOMER

CREATE TABLE BANKCARD(
	CUSTOMERID INT,
    CARD VARCHAR(30) UNIQUE,
    FOREIGN KEY (CUSTOMERID) REFERENCES CUSTOMER(ID),
    PRIMARY KEY (CUSTOMERID, CARD)
)

DROP TABLE BANKCARD

CREATE TABLE BANNER (
	ID INT PRIMARY KEY AUTO_INCREMENT,
    NAME NVARCHAR(100),
    IMAGE TEXT
)


select * from banner










drop table account
drop table employee
DROP TABLE CUSTOMER
DROP TABLE BANKCARD
drop table user




