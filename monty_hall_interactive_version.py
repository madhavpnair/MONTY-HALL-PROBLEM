import random 

total_no_of_trials=0
success_count_for_switching=0
success_count_for_NOT_switching=0

def fun1(room_with_car,user_input):
        print(f"testing: room with car is :{room_with_car}")
        print()
        print(f"testing: user input is : {user_input}")
        print()

def fun2(door_monty_opens):
        print(f"testing: room Monty opens is: {door_monty_opens}")
        print()
        print(f"{door_monty_opens} is an empty room")
        print()

def fun3(second_choice):
        print(f"testing: second choice is : {second_choice}")
        print()
        

def fun4(user_input,second_choice):
    print(f"testing: the user changed from {user_input} to {second_choice}")
    print()
    print(f"testing: Now the user choice is {second_choice}")
    print()

def fun5(switch,user_input,second_choice):
        if not switch:
                print("testing: the user does not change his choice") 
                print() 
                print(f"testing : so the user choice is {user_input} and the second choice is {second_choice} only ") 
                print()

def fun6(success_count_for_switching,success_count_for_NOT_switching):
        print(f"testing: count for switched and won is : {success_count_for_switching}")
        print()
        
        print(f"testing: count for unswitched and won is : {success_count_for_NOT_switching}")
        print()



while(1):

    
    print()
    print("        Welcome! This is a simulation of the Monty Hall problem")    
    print()
    print()
    print()
    print("        Here we have three doors 1,2,3")
    print("        One room has a car in it and other two are empty")
    print("        choose the number of the door which you want to open")
    

    try:
        user_input=int(input("        Enter '1' or '2' or '3' or '0' to exit the program : "))
        print()
    except ValueError:
        print("please enter a valid door number 1 2 or 3 or 0 to exit!!!")
        print()
        continue
    if user_input not in [1,2,3,0]:
        print("please enter a valid door number 1 2 or 3 or 0 to exit!!!")
        print()
        continue
         
    if(user_input==0):
        break
    
    
    mech="0"    
    while(mech.lower() not in ["yes","no"]):   
        flag=False
        mech=input("Wanna see the inner mechanisms of the gameplay?? - YES (yes) or NO (no) :")
        print()
        if(mech.lower() not in ["yes","no"]):
            print("please enter either YES(yes) or NO(no)!!!")
            continue
        if(mech.lower()=="yes"):
            print("the mechanisms will be shown during the game")
            print()
            flag=True


    total_no_of_trials+=1

    room_with_car=random.randint(1,3)

    if flag:
        fun1(room_with_car,user_input)

    door_monty_opens=0
    for i in range(1,4):
        if((i!=user_input) and (i!=room_with_car)):
            door_monty_opens=i

    if flag:
        fun2(door_monty_opens)
    

    second_choice=room_with_car
    if(room_with_car==user_input):
        for i in range(1,4):
            if(i!=room_with_car) and (i!=door_monty_opens):
                second_choice=i

    if flag:
        fun3(second_choice)

    print(f"You have an option to switch your choice to door number {second_choice} or can continue with your first choice that is {user_input}")
    print()


    user_input1="1"
    while(user_input1 not in ["yes","no"]):
        user_input1=input(f"Enter YES/yes to change your choice to door number {second_choice} ; NO/no to continue with the door number {user_input} : ")
        print()
        if(user_input1.lower() not in ["yes","no"]):
                print("please enter either YES(yes) or NO(no)!!!")
                continue

    switch=False
    if(user_input1.lower()=="yes"):
        
        user_input=second_choice
        switch=True

        if flag:
            fun4(user_input,second_choice)

    if flag:
        fun5 (user_input,second_choice,switch)
    
    
    if((second_choice==room_with_car) and (switch==True)):
        print("switched and won")
        print()
        success_count_for_switching+=1

    
    elif ((switch==False) and (user_input==room_with_car)):
        print("unswitched and won")
        print()
        success_count_for_NOT_switching+=1

    
    if flag:
        fun6(success_count_for_switching,success_count_for_NOT_switching)

    
    
print(f"  Total attempts: {total_no_of_trials}" )
print(f"  switching won : {success_count_for_switching}")  
print(f"  unswitching won : {success_count_for_NOT_switching}") 
print()


print(f"Probability of winning by switching: {success_count_for_switching / total_no_of_trials:.2%}")
print(f"Probability of winning by not switching: {success_count_for_NOT_switching / total_no_of_trials:.2%}") 
print()
    
