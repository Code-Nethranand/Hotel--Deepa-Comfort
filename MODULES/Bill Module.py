import mysql.connector as c
#Module to generate the final bill
def bill():
    db=c.connect(host="localhost",user="root",password="root",database="HOTEL_DEEPA_COMFORTS")
    mc=db.cursor()
    room_no=int(input(" Enter the room number : "))
    print("Processing details.......")
    print()
    print()
    sd="UPDATE BILL SET TAX=0.145*(ACCOMMODATION+MEALS) WHERE ROOM_NO={}".format(room_no)
    mc.execute(sd)
    db.commit()
    sd2="UPDATE BILL SET TOTAL=1.145*(ACCOMMODATION+MEALS) WHERE ROOM_NO={}".format(room_no)
    mc.execute(sd2)
    db.commit()
    sd3="SELECT*FROM BILL WHERE ROOM_NO={}".format(room_no)
    mc.execute(sd3)
    data=mc.fetchall()
    print(" \t\t\t HOTEL DEEPA COMFORTS ")
    print(" \t\t\t\t BILL ")
    print(" Room number            : ",data[0][0])
    print()
    print(" Accommodation          : ",data[0][1])
    print(" Meals                  : ",data[0][2])
    print(" Tax (GST)              : ",data[0][3])
    print(" Total                  : ",data[0][4])
    print()
    print("Thank you for choosing Moti Mahal for your stay! We hope you visit again!")
    db.close()
