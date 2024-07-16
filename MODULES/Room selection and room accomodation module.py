import random as r
from datetime import date
import mysql.connector as sqlc
conn=sqlc.connect(host='localhost',user='root',password='root')
a=conn.cursor()
try:
    q1="CREATE DATABASE hotel_deepa_comforts;"
    a.execute(q1)
    conn.commit()
    q2 = "USE hotel_deepa_comforts;"
    a.execute(q2)
    conn.commit()
    q3='CREATE TABLE REGISTRATION_DETAILS(DOB DATE,REG_NO INT(6) PRIMARY KEY NOT NULL,FNAME VARCHAR(20),LNAME VARCHAR(20),CITIZENSHIP VARCHAR(30),NATIONAL_IDNO VARCHAR(20),GENDER VARCHAR(1),PHONE_NO VARCHAR(13),ADDRESS VARCHAR(100),EMAIL VARCHAR(30),NO_MEMBERS INT(3))'
    a.execute(q3)
    conn.commit()
    q4="CREATE TABLE ROOM_DETAILS(ROOM_NO INT(3) PRIMARY KEY,POSITION VARCHAR(10) DEFAULT 'VACANT')"
    a.execute(q4)
    Q1 = "INSERT INTO ROOM_DETAILS(ROOM_NO) VALUES(101),(102),(103),(104),(105),(106),(107),(108),(109),(110),(111),(112),(113),(114),(115),(116),(117),(118),(119),(120),(121),(122),(123),(124),(125);"
    a.execute(Q1)
    q8="CREATE TABLE STAFF(STAFF_NO INT(4) PRIMARY KEY,NAME VARCHAR(30),MOBILE_NO VARCHAR(20),GENDER VARCHAR(1),DESIGNATION VARCHAR(20),SALARY INT(8),NATID_NO VARCHAR(20),EMAIL_ID VARCHAR(30),ACC_NO VARCHAR(20))"
    a.execute(q8)
    conn.commit()
    q9="CREATE TABLE BILL(ROOM_NO INT(6) REFERENCES REGISTRATION_DETAILS(ROOM_NO),ACCOMMODATION INT(6) DEFAULT 0,MEALS INT(6) DEFAULT 0,ADDON INT(6) DEFAULT 0,EVEORG INT(6) DEFAULT 0,TAX INT(6) DEFAULT 0,tc INT(8) DEFAULT 0)"
    a.execute(q9)
    conn.commit()
    q91 = "INSERT INTO BILL(ROOM_NO) VALUES(101),(102),(103),(104),(105),(106),(107),(108),(109),(110),(111),(112),(113),(114),(115),(116),(117),(118),(119),(120),(121),(122),(123),(124),(125);"
    a.execute(q91)
    conn.commit()
except:
    Q = 'USE hotel_deepa_comforts;'
    a.execute(Q)
    conn.commit()
conn.close()
conn = sqlc.connect(host='localhost', user='root',password='root', database='hotel_deepa_comforts')
a = conn.cursor()
def room_selection():
        
    print('OUR ACCOMODATION PACKAGES')
    print('Press any key to continue...')
    input()
    print('(1) Suite rooms (double bed,AC)            : Rs.7000 per day')
    print('(2) Premium rooms (double bed with AC)     : Rs.6000 per day')
    print('(3) Premium rooms (single bed with AC)     : Rs.4000 per day')
    print('(4) Premium rooms (double bed without AC)  : Rs.3000 per day')
    print('(5) Premium rooms (single bed without AC)  : Rs.2000 per day')
    print()
    d = input('Are you sure you want to continue with purchasing our packages(Y/N):')
    print()
    if d[0].lower() == 'y':
        global nor
        nor = int(input('Enter the number of rooms you want:'))
        c = 0
        tc = 0
        for i in range(nor):
            ch = int(input("Enter your choice of room type(1,2,3,4 or 5):"))
            print()
            if ch == 1:
                try:
                    tc += 7000
                    room = "SELECT*FROM ROOM_DETAILS WHERE POSITION='VACANT' AND ROOM_NO BETWEEN 101 AND 105"
                    a.execute(room)
                    d = a.fetchall()
                    print('Your room number is', d[0][0])
                    room_no = d[0][0]
                    q = 'UPDATE ROOM_DETAILS SET POSITION="OCCUPIED" WHERE ROOM_NO={}'.format(room_no)
                    a.execute(q)
                    conn.commit()
                except:
                    print('This type of room is not available currently,kindly try other rooms')
            elif ch == 2:
                try:
                    tc += 6000
                    room = "SELECT*FROM ROOM_DETAILS WHERE POSITION='VACANT' AND ROOM_NO BETWEEN 106 AND 110"
                    a.execute(room)
                    d = a.fetchall()
                    print('Your room number is', d[0][0])
                    room_no = d[0][0]
                    q = 'UPDATE ROOM_DETAILS SET POSITION="OCCUPIED" WHERE ROOM_NO={}'.format(room_no)
                    a.execute(q)
                    conn.commit()
                except:
                    print('This type of room is not available currently,kindly try other rooms')
            elif ch == 3:
                try:
                    tc += 4000
                    room = "SELECT*FROM ROOM_DETAILS WHERE POSITION='VACANT' AND ROOM_NO BETWEEN 111 AND 115"
                    a.execute(room)
                    d = a.fetchall()
                    print('Your room number is', d[0][0])
                    room_no = d[0][0]
                    q = 'UPDATE ROOM_DETAILS SET POSITION="OCCUPIED" WHERE ROOM_NO={}'.format(room_no)
                    a.execute(q)
                    conn.commit()
                except:
                    print('This type of room is not available currently,kindly try other rooms')
            elif ch == 4:
                try:
                    tc += 3000
                    room = "SELECT*FROM ROOM_DETAILS WHERE POSITION='VACANT' AND ROOM_NO BETWEEN 116 AND 120"
                    a.execute(room)
                    d = a.fetchall()
                    print('Your room number is', d[0][0])
                    room_no = d[0][0]
                    q = 'UPDATE ROOM_DETAILS SET POSITION="OCCUPIED" WHERE ROOM_NO={}'.format(room_no)
                    a.execute(q)
                    conn.commit()
                except:
                    print('This type of room is not available currently,kindly try other rooms')
            elif ch == 5:
                try:
                    tc += 2000
                    room = "SELECT*FROM ROOM_DETAILS WHERE POSITION='VACANT' AND ROOM_NO BETWEEN 121 AND 125"
                    a.execute(room)
                    d = a.fetchall()
                    print('Your room number is', d[0][0])
                    room_no = d[0][0]
                    q = 'UPDATE ROOM_DETAILS SET POSITION="OCCUPIED" WHERE ROOM_NO={}'.format(room_no)
                    a.execute(q)
                    conn.commit()
                except:
                    print('This type of room is not available currently,kindly try other rooms')
            else:
                print('OOPS! You chose an invalid option')
        print()
        print('The specificed details of your choice of room has been made and stored')
        global rooms_cost
        rooms_cost = tc
        Q = 'UPDATE BILL SET ACCOMMODATION={} WHERE ROOM_NO={}'.format(rooms_cost, room_no)
        a.execute(Q)
        conn.commit()
    else:
        print('''You can also call us on our toll free number 9482843844 to get further customisation of your choice.
    Exiting...''')
    conn.close()



