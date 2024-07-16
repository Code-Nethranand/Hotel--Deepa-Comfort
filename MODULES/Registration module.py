import mysql.connector as sqlc
import random as ran
from datetime import date
def create():
    conn=sqlc.connect(host="localhost", user="root", passwd="root")
    a=conn.cursor()
    q1 = "create database hotel_deepa_comforts;"
    a.execute(q1)
    q2="create table reg_details(DATE DATE,REG_NO int(6) primary key not null,FIRST_NAME varchar(25),CITIZENSHIP varchar(40),NATIONAL_ID varchar(20),GENDER varchar(1),PHONE_NO varchar(13),ADDRESS varchar(50),EMAIL varchar(45),NO_OF_MEMBERS varchar(2));"
    a.execute(q2)
    conn.commit()
    conn.close()

def notcreate():
    conn = sqlc.connect(host="localhost", user="root", passwd="root")
    a = conn.cursor()
    q1="use hotel_deepa_comforts;"
    a.execute(q1)
    conn.commit()
    conn.close()

def reg():
    conn = sqlc.connect(host="localhost", user="root", passwd="root",database="hotel_deepa_comforts")
    a = conn.cursor()
    today = date.today()
    tdate = today.strftime("%d,%B,%Y")
    print("Date of Booking:", tdate)
    regno=ran.randint(100000,999999)
    print("Registration Number:",regno)
    print("--> Please note this registration number it  will be used in compleating other booking procedures later")
    fname=input("First name: ")
    lname=input("Last name: ")
    citi=input("Citizenship: ")
    nat_id=input("National ID card no.: ")
    gen=input("Gender(M\F\O): ")
    ph_no=input("Phone no.: ")
    address=input("Address: ")
    email=input("Email ID: ")
    nper=input("No. of members: ")
    inregd="INSERT INTO reg_details VALUES['{}','{}','{}','{}','{}','{}','{}','{}','{}','{}',{}]".format(tdate,regno,fname,lname,citi,nat_id,gen,ph_no,address,email,nper)
    a.execute(inregd)
    conn.commit()    
    print("Sucessfully your details have been registered")
    conn.close()

reg()



