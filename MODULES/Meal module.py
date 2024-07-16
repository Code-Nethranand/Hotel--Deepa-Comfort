import mysql.connector as c
#Module for ordering meals
def meals():
    db=c.connect(host="localhost",user="root",password="root",database="HOTEL_DEEPA_COMFORTS")
    mc=db.cursor()
    global meals_cost
    room_no=int(input(" Enter the room number : "))
    print(" The orders will be taken one by one ")
    print(" What would you like : ")
    print(" 1. Breakfast ")
    print(" 2. Lunch ")
    print(" 3. Snacks ")
    print(" 4. Dinner ")
    choice=int(input(" Enter your choice(1,2,3 or 4) : "))
    breakfast_cost=lunch_cost=snacks_cost=dinner_cost=0
    if choice==1:
        print()
        f=open("BREAKFAST.txt","r")
        s=f.read()
        print(s)
        L=[70,120,60,50,45,55,30,75,80,60]
        ans="yes"
        try:
            while ans[0].lower()=="y":
                print()
                item_code=int(input(" Enter the food code of the item you want : "))
                breakfast_cost=breakfast_cost+L[item_code-1]
                meals_cost+=L[item_code-1]
                ans=input(" Do you want to have more items(YES/NO) : ")
            print(" The total cost for breakfast is ",breakfast_cost)
        except:
            print(" Invalid food code........")
        f.close()
    elif choice==2:
        print()
        f=open("LUNCH.txt","r")
        s=f.read()
        print(s)
        L=[120,125,145,120,120,200,250,150,175,250,175,300,350,750,125]
        ans="yes"
        try:
            while ans[0].lower()=='y':
                print()
                item_code=int(input(" Enter the food code of the item you want : "))
                lunch_cost=lunch_cost+L[item_code-1]
                meals_cost+=L[item_code-1]
                ans=input(" Do you want to have more items(YES/NO) : ")
            print(" The total cost for lunch is ",lunch_cost)
        except:
            print(" Invalid food code..........")
        f.close()
    elif choice==3:
        print()
        f=open("SNACKS.txt","r")
        s=f.read()
        print(s)
        L=[40,30,50,20,25,65,35,25,40,50,155,125,110,125,165]
        ans="yes"
        try:
            while ans[0].lower()=='y':
                print()
                item_code=int(input(" Enter the food code of the item you want : "))
                snacks_cost=snacks_cost+L[item_code-1]
                meals_cost+=L[item_code-1]
                ans=input(" Do you want to have more items(YES/NO) : ")
            print(" The total cost for snacks is ",snacks_cost)
        except:
            print(" Invalid food code.......")
        f.close()
    elif choice==4:
        print()
        f=open("DINNER.txt","r")
        s=f.read()
        print(s)
        L=[135,75,80,225,150,185,160,175,85,50]
        ans="yes"
        try:
            while ans[0].lower()=='y':
                print()
                item_code=int(input(" Enter the food code of the item you want : "))
                dinner_cost=dinner_cost+L[item_code-1]
                meals_cost+=L[item_code-1]
                ans=input(" Do you want to have more items(YES/NO) : ")
            print(" The total cost for dinner is ",dinner_cost)
        except:
            print(" Invalid food code...........")
        f.close()
    else:
        print(" Invalid choice ")
    sd="UPDATE BILL SET MEALS={} WHERE ROOM_NO={}".format(meals_cost,room_no)
    mc.execute(sd)
    db.commit()
    db.close()

