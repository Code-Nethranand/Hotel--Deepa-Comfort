#HOTEL_MANAGEMENT_SYSTEM MADE BY NETHRANAND & KHYATHI 5CSA 2023-24

import mysql.connector as c
import random as ran
import random as r
from datetime import date
import mysql.connector as sqlc

print("\n\n\t\t\tWELCOME TO HOTEL_MANAGEMENT_SYSTEM")

user=input("\n\nEnter user name of your mysql : ")
password=input("Enter password of your mysql : ")

#Connecting python with mysql
#Creating Data base and required tables for the project
conn = sqlc.connect(host='localhost', user=user, password=password)
a = conn.cursor()
try:
    q1 = "CREATE DATABASE hotel_deepa_comforts;"
    a.execute(q1)
    conn.commit()
    q2 = "USE hotel_deepa_comforts;"
    a.execute(q2)
    conn.commit()
    q3 = "CREATE TABLE REGISTRATION_DETAILS(DATE DATE,REG_NO INT(6) PRIMARY KEY NOT NULL,FNAME VARCHAR(20),LNAME VARCHAR(20),CITIZENSHIP VARCHAR(30),NATIONAL_IDNO VARCHAR(20),GENDER VARCHAR(1),PHONE_NO VARCHAR(13),ADDRESS VARCHAR(100),EMAIL VARCHAR(30),NO_MEMBERS INT(3))"
    a.execute(q3)
    conn.commit()
    q4 = "CREATE TABLE ROOM_DETAILS(ROOM_NO INT(3) PRIMARY KEY,POSITION VARCHAR(10) DEFAULT 'VACANT')"
    a.execute(q4)
    Q1 = "INSERT INTO ROOM_DETAILS(ROOM_NO) VALUES(101),(102),(103),(104),(105),(106),(107),(108),(109),(110),(111),(112),(113),(114),(115),(116),(117),(118),(119),(120),(121),(122),(123),(124),(125);"
    a.execute(Q1)
    q8 = "CREATE TABLE staff_details(STAFF_NO INT(4) PRIMARY KEY,NAME VARCHAR(30),MOBILE_NO VARCHAR(20),GENDER VARCHAR(1),DESIGNATION VARCHAR(20),SALARY INT(8),NATID_NO VARCHAR(20),EMAIL_ID VARCHAR(30),ACC_NO VARCHAR(20))"
    a.execute(q8)
    conn.commit()
    q9 = "CREATE TABLE BILL(ROOM_NO INT(6) REFERENCES REGISTRATION_DETAILS(ROOM_NO),ACCOMMODATION INT(6) DEFAULT 0,MEALS INT(6) DEFAULT 0,ADDON INT(6) DEFAULT 0,TAX INT(6) DEFAULT 0,tc INT(8) DEFAULT 0)"
    a.execute(q9)
    conn.commit()
    q91 = "INSERT INTO BILL(ROOM_NO) VALUES(101),(102),(103),(104),(105),(106),(107),(108),(109),(110),(111),(112),(113),(114),(115),(116),(117),(118),(119),(120),(121),(122),(123),(124),(125);"
    a.execute(q91)
    conn.commit()
except:
    Q = "USE hotel_deepa_comforts;"
    a.execute(Q)
    conn.commit()
conn.close()

#Module to store the registration details of the customer
def REGISTRATION_DETAILS():
    conn = sqlc.connect(host="localhost",user=user,passwd=password,database="hotel_deepa_comforts")
    a = conn.cursor()
    today = date.today()
    tdate = today.strftime("%d,%B,%Y")
    print("Date of Booking:",tdate)
    regno = ran.randint(100000, 999999)
    print("Registration Number:", regno)
    print("--> Please note this registration number it  will be used in compleating other booking procedures later")
    fname = input("First name: ")
    lname = input("Last name: ")
    citi = input("Citizenship: ")
    nat_id = input("National ID card no.: ")
    gen = input("Gender(M)(F)(O): ")
    ph_no = input("Phone no.: ")
    address = input("Address: ")
    email = input("Email ID: ")
    nper = input("No. of members: ")
    inregd = "INSERT INTO REGISTRATION_DETAILS VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(today, regno, fname, lname, citi, nat_id, gen, ph_no, address, email, nper)
    a.execute(inregd)
    conn.commit()
    print("Sucessfully your details have been registered")
    conn.close()

#Module for room selection and accomodation of room for the customer
def room_selection_accomodation():
    conn = sqlc.connect(host="localhost", user=user,passwd=password, database="hotel_deepa_comforts")
    a = conn.cursor()
    print(" OUR ACCOMODATION PACKAGES ")
    print(" Press any key to continue........ ")
    input()
    print(" (1) Suite rooms (double bed,AC)            : Rs.7000 per day ")
    print(" (2) Premium rooms (double bed with AC)     : Rs.6000 per day ")
    print(" (3) Premium rooms (single bed with AC)     : Rs.4000 per day ")
    print(" (4) Premium rooms (double bed without AC)  : Rs.3000 per day ")
    print(" (5) Premium rooms (single bed without AC)  : Rs.2000 per day ")
    print()
    d = input(" Are you sure you want to continue with purchasing our packages(Y/N) : ")
    print()
    if d[0].lower() == 'y':
        global nor
        nor = int(input(" Enter the number of rooms you want : "))
        c = 0 
        tc = 0
        for i in range(nor):
            ch = int(input(" Enter your choice of room type(1,2,3,4 or 5) : "))
            print()
            if ch == 1:
                try:
                    tc += 7000
                    room = "SELECT*FROM ROOM_DETAILS WHERE POSITION='VACANT' AND ROOM_NO BETWEEN 101 AND 105"
                    a.execute(room)
                    d = a.fetchall()
                    print("Your room number is ", d[0][0])
                    room_no = d[0][0]
                    q = 'UPDATE ROOM_DETAILS SET POSITION="OCCUPIED" WHERE ROOM_NO={}'.format(room_no)
                    a.execute(q)
                    conn.commit()
                except:
                    print(" This type of room is not available currently,kindly try other rooms ")
            elif ch == 2:
                try:
                    tc += 6000
                    room = "SELECT*FROM ROOM_DETAILS WHERE POSITION='VACANT' AND ROOM_NO BETWEEN 106 AND 110"
                    a.execute(room)
                    d = a.fetchall()
                    print(" Your room number is ", d[0][0])
                    room_no = d[0][0]
                    q = 'UPDATE ROOM_DETAILS SET POSITION="OCCUPIED" WHERE ROOM_NO={}'.format(room_no)
                    a.execute(q)
                    conn.commit()
                except:
                    print(" This type of room is not available currently,kindly try other rooms ")
            elif ch == 3:
                try:
                    tc += 4000
                    room = "SELECT*FROM ROOM_DETAILS WHERE POSITION='VACANT' AND ROOM_NO BETWEEN 111 AND 115"
                    a.execute(room)
                    d = a.fetchall()
                    print(" Your room number is ", d[0][0])
                    room_no = d[0][0]
                    q = ' UPDATE ROOM_DETAILS SET POSITION="OCCUPIED" WHERE ROOM_NO={} '.format(room_no)
                    a.execute(q)
                    conn.commit()
                except:
                    print(" This type of room is not available currently,kindly try other rooms ")
            elif ch == 4:
                try:
                    tc += 3000
                    room = "SELECT*FROM ROOM_DETAILS WHERE POSITION='VACANT' AND ROOM_NO BETWEEN 116 AND 120"
                    a.execute(room)
                    d = a.fetchall()
                    print(" Your room number is ", d[0][0])
                    room_no = d[0][0]
                    q = 'UPDATE ROOM_DETAILS SET POSITION="OCCUPIED" WHERE ROOM_NO={}'.format(room_no)
                    a.execute(q)
                    conn.commit()
                except:
                    print(" This type of room is not available currently,kindly try other rooms ")
            elif ch == 5:
                try:
                    tc += 2000
                    room = "SELECT*FROM ROOM_DETAILS WHERE POSITION='VACANT' AND ROOM_NO BETWEEN 121 AND 125"
                    a.execute(room)
                    d = a.fetchall()
                    print(" Your room number is ", d[0][0])
                    room_no = d[0][0]
                    q = 'UPDATE ROOM_DETAILS SET POSITION="OCCUPIED" WHERE ROOM_NO={}'.format(room_no)
                    a.execute(q)
                    conn.commit()
                except:
                    print(" This type of room is not available currently,kindly try other rooms ")
            else:
                print(" OOPS! You chose an invalid option ")
        print()
        print(" The specificed details of your choice of room has been made and stored ")
        global rooms_cost
        rooms_cost = tc
        Q = "UPDATE BILL SET ACCOMMODATION={} WHERE ROOM_NO={}".format(rooms_cost, room_no)
        a.execute(Q)
        conn.commit()
    else:
        print('''You can also call us on our toll free number 9148970912 to get further customisation of your choice.
    Exiting...''')
    conn.close()


#Module for ordering meals
def meals():
    db = c.connect(host="localhost", user=user,password=password, database="hotel_deepa_comforts")
    mc = db.cursor()
    global meals_cost
    meals_cost=0
    room_no = int(input(" Enter the room number : "))
    print(" The orders will be taken one by one ")
    print(" What would you like : ")
    print(" 1. Breakfast ")
    print(" 2. Lunch ")
    print(" 3. Snacks ")
    print(" 4. Dinner ")
    choice = int(input(" Enter your choice(1,2,3 or 4) : "))
    breakfast_cost = lunch_cost = snacks_cost = dinner_cost = 0
    if choice == 1:
        print()
        f = open("C:\\Users\\Micro\\Desktop\\HOTEL_MANAGEMENT_SYSTEM_CLASS XII 2020-2021\\TEXT FILES\\BREAKFAST.txt", "r")  #Give your own file directory
        s = f.read()
        print(s)
        L = [40,45,70,65,50,65,40,70,80,40,50]
        ans = "yes"
        try:
            while ans[0].lower() == "y":
                print()
                item_code = int(input(" Enter the food code of the item you want : "))
                breakfast_cost = breakfast_cost+L[item_code-1]
                meals_cost += L[item_code-1]
                ans = input(" Do you want to have more items(YES/NO) : ")
            print(" The total cost for breakfast is ", breakfast_cost)
        except:
            print(" Invalid food code........")
        f.close()
    elif choice == 2:
        print()
        f = open("C:\\Users\\Micro\\Desktop\\HOTEL_MANAGEMENT_SYSTEM_CLASS XII 2020-2021\\TEXT FILES\\LUNCH.txt", "r")      #Give your own file directory
        s = f.read()
        print(s)
        L = [45,70,85,75,115,35,30,30,25,155,185,170,165,160,205,220,60,70,35]
        ans = "yes"
        try:
            while ans[0].lower() == 'y':
                print()
                item_code = int(input(" Enter the food code of the item you want : "))
                lunch_cost = lunch_cost+L[item_code-1]
                meals_cost += L[item_code-1]
                ans = input(" Do you want to have more items(YES/NO) : ")
            print(" The total cost for lunch is ", lunch_cost)
        except:
            print(" Invalid food code..........")
        f.close()
    elif choice == 3:
        print()
        f = open("C:\\Users\\Micro\\Desktop\\HOTEL_MANAGEMENT_SYSTEM_CLASS XII 2020-2021\\TEXT FILES\\SNACKS.txt", "r")     #Give your own file directory
        s = f.read()
        print(s)
        L = [40,50,40,55,60,50,45,70,80]
        ans = "yes"
        try:
            while ans[0].lower() == 'y':
                print()
                item_code = int(input(" Enter the food code of the item you want : "))
                snacks_cost = snacks_cost+L[item_code-1]
                meals_cost += L[item_code-1]
                ans = input(" Do you want to have more items(YES/NO) : ")
            print(" The total cost for snacks is ", snacks_cost)
        except:
            print(" Invalid food code.......")
        f.close()
    elif choice == 4:
        print()
        f = open("C:\\Users\\Micro\\Desktop\\HOTEL_MANAGEMENT_SYSTEM_CLASS XII 2020-2021\\TEXT FILES\\DINNER.txt", "r")     #Give your own file directory
        s = f.read()
        print(s)
        L = [30,65,70,85,75,115,35,30,30,25,155,185,170,165,160,215,220,60,70,35]
        ans = "yes"
        try:
            while ans[0].lower() == 'y':
                print()
                item_code = int(input(" Enter the food code of the item you want : "))
                dinner_cost = dinner_cost+L[item_code-1]
                meals_cost += L[item_code-1]
                ans = input(" Do you want to have more items(YES/NO) : ")
            print(" The total cost for dinner is ", dinner_cost)
        except:
            print(" Invalid food code...........")
        f.close()
    else:
        print(" Invalid choice ")
    sd = "UPDATE BILL SET MEALS={} WHERE ROOM_NO={}".format(meals_cost, room_no)
    mc.execute(sd)
    db.commit()
    db.close()


#A module to select additional provisional services of the HOTEL DEEPA COMFORTS
def additional_services():
    db=sqlc.connect(host='localhost',user=user,password=password,database='hotel_deepa_comforts')
    mc=db.cursor()
    room_no=int(input("\n Enter the room number : "))
    print("\n Following are the services we provide in addition to our normal facilities. ")
    print("\n 1. Laundry (Rs.885) ")
    print("2. Spa (Rs.2000) ")
    print("3. Room cleaning (Free) ")
    print("4. Ironing service (Amount depends upon the clothing items) ")
    print("5. Swimming (250 , Timings(7 AM - 7 PM)) ")
    print("6. Games (Free) ")
    print("7. Gym (Rs.300 ) ")
    any="yes"
    service_charge=0
    while any[0].lower()=='y':
        choice=int(input("\n Choose a service (1,2,3,4,5,6 or 7) : "))
        if choice==1:
            service_charge=service_charge+885
        elif choice==2:
            service_charge=service_charge+2000
        elif choice==3:
            service_charge=service_charge+0
        elif choice==4:
            cloth_no=int(input("\n How many clothes are to be ironed? : "))
            cloth_amount=100*cloth_no
            service_charge=service_charge+cloth_amount
        elif choice==5:
            service_charge=service_charge+250
        elif choice==6:
            service_charge=service_charge+0
        elif choice==7:
            service_charge=service_charge+300
        q1="INSERT INTO ADDON_SERVICE(ROOM_NO,SERVICE_NO) VALUES({},'{}')".format(room_no,choice)
        print()
        any=input("\n Do you want to choose more facilities? [YES/NO] : ")
        print()
    global addon_service_cost
    addon_service_cost=service_charge
    q2="UPDATE BILL SET ADDON={} WHERE ROOM_NO={}".format(addon_service_cost,room_no)
    mc.execute(q2)
    db.commit()
    print("\n Thank you for choosing our services! We are happy helping you ! ")
    db.close()

    
#Module to store the deatils of staff members
def staff_details():
    db = c.connect(host="localhost", user=user,password=password, database="hotel_deepa_comforts")
    mc = db.cursor()
    sno = r.randint(101, 999)
    print("Staff number : ", sno)
    name = input("Staff name : ")
    mno = int(input("Mobile number : "))
    gender = input("Gender(M/F) : ")
    desg = input("Designation : ")
    salary = int(input("Salary of the staff : "))
    natid_no = input("National ID Card number : ")
    eid = input("Email ID : ")
    accno = int(input("Account number : "))
    sd = "INSERT INTO STAFF_DETAILS VALUES({},'{}','{}','{}','{}',{},'{}','{}','{}')".format(sno, name, mno, gender, desg, salary, natid_no, eid, accno)
    mc.execute(sd)
    db.commit()
    print()
    print('Your details have been succesfully entered.')
    db.close()


#Module to generate the final bill
def bill():
    db = c.connect(host="localhost", user=user,password=password, database="hotel_deepa_comforts")
    mc = db.cursor()
    room_no = int(input(" Enter the room number : "))
    print("Processing details.......")
    print()
    print()
    sd = "UPDATE BILL SET TAX=0.145*(ACCOMMODATION+MEALS+ADDON) WHERE ROOM_NO={}".format(room_no)
    mc.execute(sd)
    db.commit()
    sd2 = "UPDATE BILL SET tc=1.145*(ACCOMMODATION+MEALS+ADDON) WHERE ROOM_NO={}".format(room_no)
    mc.execute(sd2)
    db.commit()
    sd3 = "SELECT*FROM BILL WHERE ROOM_NO={}".format(room_no)
    mc.execute(sd3)
    data = mc.fetchall()
    print(" \t\t\t HOTEL DEEPA COMFORTS ")
    print(" \t\t\t\t BILL ")
    print(" Room number            : ", data[0][0])
    print()
    print(" Accommodation          : ", data[0][1])
    print(" Meals                  : ", data[0][2])
    print(" Additional service     : ", data[0][3])
    print(" Tax (GST)              : ", data[0][4])
    print(" Total                  : ", data[0][5])
    print()
    print("Thank you for choosing hotel deepa comforts  for your stay! We hope you visit again!")
    db.close()


#Admin and login Module
#_main_#
print()
print(" \t\t\t\t WELCOME TO THE HOTEL DEEPA COMFORTS ")
print(" \t\t\t\t--------------------------------- ")
while True:
    print(" Are you : ")
    print(" 1. A Customer ")
    print(" 2. An administrator ")
    print(" 3. A staff ")
    print(" 4. About ")
    print(" 5. Exit the HOTEL DEEPA COMFORTS page ")
    choice = int(input(" Enter your choice(1,2,3,4 or 5) : "))
    if choice == 1:
        print()
        print("---------------------------------------------------")
        print("                  CUSTOMER PAGE                    ")
        print("---------------------------------------------------")
        print(" Dear Customer! Welcome to the HOTEL DEEPA COMFORTS! ")
        print(" Kindly register into our page to buy packages ")
        ch = input(" Do you want to continue with the registration (yes/no) : ")
        if ch[0].lower() == 'y':
            REGISTRATION_DETAILS()  # Calling of function
            print(" \n\n\n\n ")
            input(" Press any key to continue .......... ")
            print()
            room_selection_accomodation()  # Calling of function
            input(" Press any key to continue ........... ")
            print()
            print(" Your registration and the required type of room has been successfully reserved for you ")
            print(" You may now start with exploring and availing the facilities in our hotel ")
            print()
            input(" Press any key to continue ........... ")
            print()
            meals_cost = 0
            while True:
                print(" Which of the following services you would like to avail... ")
                print(" 1. Order food ")
                print(" 2. Avail additional services ")
                print(" 3. Exit ")
                ch2 = int(input(" Your choice (1,2 or 3) : "))
                if ch2 == 1:
                    print(" ---------------------------------------------------- ")
                    print("                   FOOD ORDERS                        ")
                    print(" ---------------------------------------------------- ")
                    meals()  # Calling of function
                    print()
                    input(" Press any key to continue ........... ")
                    print()
                elif ch2 == 2:
                    print(" ---------------------------------------------------- ")
                    print("               ADDITIONAL SERVICES                    ")
                    print(" ---------------------------------------------------- ")
                    additional_services() #Calling of function
                    print()
                    input(" Press any key to continue ........... ")
                    print()   
                elif ch2 == 3:
                    print(" Exiting .......... ")
                    break
                    input(" Press any key to continue ........... ")
                    print()
                else:
                    print(" Invalid choice ")
                    input(" Press any key to continue ........... ")
                    print()
            print()
            print(" Thank you for chosing our services! You may now proceed for the billing ")
            input(" Press any key to continue ........... ")
            print()
            print(" ------------------------------------------------------ ")
            print("                      BILL                              ")
            print(" ------------------------------------------------------ ")
            bill()  # Calling of function
            print()
            print(" We hope to see you again ")
            print(" \n\n\n\n ")
            input(" Press any key to continue ......... ")
        else:
            print(" Thank you for visiting our page! We hope to provide you services in the future ")
            input(" Press any key to continue ......... ")
    elif choice == 2:
        #Administrator module
        print(" -------------------------------------------------- ")
        print("                 ADMINISTRATOR PAGE                 ")
        print(" -------------------------------------------------- ")
        print(" LOGIN ")
        user2 = input(" Enter Admin username : ")
        password2 = input(" Enter Admin password : ")
        try:
            db = c.connect(host="localhost", user=user,password=password, database="hotel_deepa_comforts")
            mc = db.cursor()
            while True:
                print("What operations would you like to perform ? ")
                print(" 1. Modify customer details as per their requirement ")
                print(" 2. Overviewing the customer's bill ")
                print(" 3. Overviewing the staff details ")
                print(" 4. Modifying the staff details ")
                print(" 5. Delete a staff record ")
                print(" 6. Delete a customer record ")
                print(" 7. Exit ")
                ch = int(input(" Enter your choice(1,2,3,4,5,6 or 7) : "))
                if ch == 1:
                    print()
                    print(" \t\t\t CUSTOMER DATA MODIFICATION ")
                    print()
                    try:
                        #Updation of registration details
                        reg_no = int(input(
                            " Enter the registration number of the customer whose details are to be modified : "))
                        print(" Kindly enter the new or modified details of the customer ")
                        fname = input(" First name : ")
                        sd1 = "UPDATE REGISTRATION_DETAILS SET FNAME='{}' WHERE REG_NO={}".format(fname, reg_no)
                        mc.execute(sd1)
                        db.commit()
                        lname = input(" Last name : ")
                        sd2 = "UPDATE REGISTRATION_DETAILS SET LNAME='{}' WHERE REG_NO={}".format(lname, reg_no)
                        mc.execute(sd2)
                        db.commit()
                        citz = input(" Citizenship : ")
                        sd3 = "UPDATE REGISTRATION_DETAILS SET CITIZENSHIP='{}' WHERE REG_NO={}".format(citz, reg_no)
                        mc.execute(sd3)
                        db.commit()
                        natid_no = input(" National ID card number : ")
                        sd4 = "UPDATE REGISTRATION_DETAILS SET NATIONAL_IDNO='{}' WHERE REG_NO={}".format(natid_no, reg_no)
                        mc.execute(sd4)
                        db.commit()
                        gender = input(" Gender(M/F) : ")
                        sd5 = "UPDATE REGISTRATION_DETAILS SET GENDER='{}' WHERE REG_NO={}".format(gender, reg_no)
                        mc.execute(sd5)
                        db.commit()
                        ph_no = int(input(" Phone number : "))
                        sd6 = "UPDATE REGISTRATION_DETAILS SET PHONE_NO='{}' WHERE REG_NO={}".format(ph_no, reg_no)
                        mc.execute(sd6)
                        db.commit()
                        address = input(" Residential address : ")
                        sd7 = "UPDATE REGISTRATION_DETAILS SET ADDRESS='{}' WHERE REG_NO={}".format(address, reg_no)
                        mc.execute(sd7)
                        db.commit()
                        email = input(" Email ID : ")
                        sd8 = "UPDATE REGISTRATION_DETAILS SET EMAIL='{}' WHERE REG_NO={}".format(email, reg_no)
                        mc.execute(sd8)
                        db.commit()
                        nm = int(input(" No.of members : "))
                        sd9 = "UPDATE REGISTRATION_DETAILS SET NO_MEMBERS={} WHERE REG_NO={}".format(nm, reg_no)
                        mc.execute(sd9)
                        db.commit()
                        print()
                        print(" Details have been successfully updated ! ")
                        input(" Press any key to continue ......... ")
                        print()
                    except:
                        print(" An unexpected connection error occured! Kindly try again! ")
                        input(" Press any key to continue ......... ")
                        print()
                elif ch == 2:
                    try:
                        #Overviewing the Customer's Bill
                        print()
                        print(" \t\t\t CUSTOMER BILL OVERVIEW ")
                        print()
                        room_no = int(input(" Enter the room number of the customer whose billing details you want to view : "))
                        print()
                        sd = "SELECT*FROM BILL WHERE ROOM_NO={}".format(room_no)
                        mc.execute(sd)
                        data = mc.fetchall()
                        print(" Accommodation      : ", data[0][1])
                        print(" Food               : ", data[0][2])
                        print(" Additional service : ", data[0][3])
                        print()
                        print(" GST                : ", data[0][4])
                        print(" Total              : ", data[0][5])
                        print()
                        input(" Press any key to continue ......... ")
                        print()
                    except:
                        print(" An unexpected error occured! Kindly try again! ")
                        print()
                        input(" Press any key to continue ......... ")
                        print()
                elif ch == 3:
                    try:
                        #Overviewing the details of the Staff Members
                        print()
                        print(" \t\t\t OVERVIEWING THE STAFF DETAILS ")
                        sno = int(input(" Enter the staff number whose details you want to view : "))
                        sd = "SELECT*FROM staff_details WHERE STAFF_NO={}".format(sno)
                        mc.execute(sd)
                        data = mc.fetchall()
                        print(" Staff number     : ", data[0][0])
                        print(" Staff name       : ", data[0][1])
                        print(" Mobile number    : ", data[0][2])
                        print(" Gender           : ", data[0][3])
                        print(" Designation      : ", data[0][4])
                        print(" Salary           : ", data[0][5])
                        print(" National ID no.  : ", data[0][6])
                        print(" Email ID         : ", data[0][7])
                        print(" Account number   : ", data[0][8])
                        print()
                        input(" Press any key to continue ......... ")
                        print()
                    except:
                        print(" An unexpected error occured or the staff number not found! Kindly try again! ")
                        print()
                        input(" Press any key to continue ......... ")
                        print()
                elif ch == 4:
                    try:
                        #Updation of the details Of the Staff Members
                        print()
                        print(" \t\t\t STAFF DATA MODIFICATION ")
                        reg_no = int(input(" Enter the staff number whose details are to be modified : "))
                        print(" Kindly enter the new or modified details of the staff ")
                        name = input(" Staff name : ")
                        sd1 = "UPDATE staff_details SET NAME='{}' WHERE STAFF_NO={}".format(name, reg_no)
                        mc.execute(sd1)
                        db.commit()
                        mno = int(input(" Mobile number : "))
                        sd2 = "UPDATE staff_details SET MOBILE_NO={} WHERE STAFF_NO={}".format(mno, reg_no)
                        mc.execute(sd2)
                        db.commit()
                        gender = input(" Gender(M/F) : ")
                        sd3 = "UPDATE staff_details SET GENDER='{}' WHERE STAFF_NO={}".format(gender, reg_no)
                        mc.execute(sd3)
                        db.commit()
                        desg = input(" Designation : ")
                        sd4 = "UPDATE staff_details SET DESIGNATION='{}' WHERE STAFF_NO={}".format(desg, reg_no)
                        mc.execute(sd4)
                        db.commit()
                        sal = int(input(" Salary : "))
                        sd5 = "UPDATE staff_details SET SALARY={} WHERE STAFF_NO={}".format(sal, reg_no)
                        mc.execute(sd5)
                        db.commit()
                        natid_no = input(" National ID card number : ")
                        sd6 = "UPDATE staff_details SET NATID_NO='{}' WHERE STAFF_NO={}".format(natid_no, reg_no)
                        mc.execute(sd6)
                        db.commit()
                        email = input(" Email ID : ")
                        sd7 = "UPDATE staff_details SET EMAIL_ID='{}' WHERE STAFF_NO={}".format(email, reg_no)
                        mc.execute(sd7)
                        db.commit()
                        acno = input(" Account number : ")
                        sd8 = "UPDATE staff_details SET ACC_NO='{}' WHERE STAFF_NO={}".format(acno, reg_no)
                        mc.execute(sd8)
                        db.commit()
                        print()
                        print(" Details have been successfully updated ! ")
                        print()
                        input(" Press any key to continue ......... ")
                        print()
                    except:
                        print(" An unexpected error occured or the record could not be found! Kindly try again! ")
                        print()
                        input(" Press any key to continue ......... ")
                        print()
                elif ch == 5:
                    try:
                        #Deleting the record of a Staff Member
                        print()
                        print(" \t\t\t STAFF DATA RECORD DELETION")
                        stno = int(input(" Enter staff number whose record you want to delete : "))
                        sd = "DELETE FROM staff_details WHERE STAFF_NO={}".format(stno)
                        mc.execute(sd)
                        db.commit()
                        print(" Record of the staff has been deleted successfully ")
                        print()
                        input(" Press any key to continue ......... ")
                        print()
                    except:
                        print(" An unexpected error occured or the record could not be found! Kindly try again! ")
                        print()
                        input(" Press any key to continue ......... ")
                        print()
                elif ch == 6:
                    try:
                        #Deleting the record of a Customer
                        print()
                        print(" \t\t\t CUSTOMER DATA RECORD DELETION")
                        cno = int(input(" Enter registration number whose record you want to delete : "))
                        sd = "DELETE FROM REGISTRATION_DETAILS WHERE REG_NO={}".format(cno)
                        mc.execute(sd)
                        db.commit()
                        print(" Record of the customer has been deleted successfully ")
                        print()
                        input(" Press any key to continue ......... ")
                        print()
                    except:
                        print(" An unexpected error occured or the record could not be found! Kindly try again! ")
                        print()
                        input(" Press any key to continue ......... ")
                        print()
                elif ch == 7:
                    print()
                    print(" EXITING.......... ")
                    break
                    input(" Press any key to continue ......... ")
            db.close()

        except:
            print(" KINDLY CHECK YOUR USERNAME AND PASSWORD  TRY AGAIN! ")
            input(" Press any key to continue .......... ")
            print()
    elif choice == 3:
        print()
        print(" -------------------------------------------------- ")
        print("                    STAFF PAGE                      ")
        print(" -------------------------------------------------- ")
        print(" Thank you for showing interest in joining our community ")
        print()
        staff_details()     # Calling of function
        print()
        input(" Press any key to continue ......... ")
        print()
    elif choice == 4:
        print()
        print(" -------------------------------------------------- ")
        print("                  THE CREATORS                      ")
        print(" -------------------------------------------------- ")
        print(" 1. Geddada Nethranand ")
        print(" 2. Balagouda Patil ")
        print(" 3. Deepanshu Sharma")
        print()
        input(" Press any key to continue ........ ")
        print()
    elif choice == 5:
        print(" Exiting permanantly from HOME ........ ")
        print()
        break
        input(" Press any key to continue .......... ")
        print()
    else:
        print(" An invalid choice! ")
        print()
        input(" Press any key to continue ........ ")
        print()
