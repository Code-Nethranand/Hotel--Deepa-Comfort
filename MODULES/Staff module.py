import mysql.connector as c
import random as r
#Module to store the deatils of staff members
def staff_details():
    db=c.connect(host="localhost",user="root",password="root",database="HOTEL_DEEPA_COMFORTS")
    mc=db.cursor()
    sno=r.randint(101,999)
    print("Staff number : ",sno)
    name=input("Staff name : ")
    mno=int(input("Mobile number : "))
    gender=input("Gender(M/F) : ")
    desg=input("Designation : ")
    salary=int(input("Salary of the staff : "))
    natid_no=input("National ID Card number : ")
    eid=input("Email ID : ")
    accno=int(input("Account number : "))
    sd="INSERT INTO STAFF_DETAILS VALUES({},'{}','{}','{}','{}',{},'{}','{}','{}')".format(sno,name,mno,gender,desg,salary,natid_no,eid,accno)
    mc.execute(sd)
    db.commit()
    print()
    print('Your details have been succesfully entered.')
    db.close()



