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