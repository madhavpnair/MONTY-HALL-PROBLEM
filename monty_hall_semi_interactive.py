import random 

total_no_of_trials=0
success_count_for_switching=0
success_count_for_NOT_switching=0

while(1):

    print()
    print("        Welcome! This is a simulation of the Monty Hall Problem")
    print()
    print()
    print("        Here we have three doors 1,2,3")
    print("        One room has a car in it and other two are empty")
    print("        choose the number of the door which you want to open")
    print()

    user_input=int(input("Enter '1' or '2' or '3' or '0' to exit the program : "))
    print()

    if(user_input==0):
        break

    total_no_of_trials+=1

    
    room_with_car=random.randint(1,3)

    print(f"testing: room with car is :{room_with_car}")
    print()
    print(f"testing: user input is : {user_input}")
    print()

    door_monty_opens=0

    for i in range(1,4):
        if((i!=user_input) and (i!=room_with_car)):
            door_monty_opens=i
    print(f"testing: room Monty opens is: {door_monty_opens}")
    print()
    print(f"{door_monty_opens} is an empty room")
    print()

    second_choice=room_with_car
    if(room_with_car==user_input):
        for i in range(1,4):
            if(i!=room_with_car) and (i!=door_monty_opens):
                second_choice=i
    print(f"testing: second choice is : {second_choice}")
    print()
    
    if(second_choice==room_with_car):
        print("switch to win")
        print()
        success_count_for_switching+=1

    
    else:
        print("unswitch to win")
        print()
        success_count_for_NOT_switching+=1


    print(f"testing: count for switched and won is : {success_count_for_switching}")
    print()
    
    print(f"testing: count for unswitched and won is : {success_count_for_NOT_switching}")
    print()
    print("*****THE END******")



n=total_no_of_trials
s=success_count_for_switching
u=success_count_for_NOT_switching

print(f"  Total attempts: {n}" )
print(f"  switching won : {s}")  
print(f"  unswitching won : {u}") 
print()


print(f"Probability of winning by switching: {s/n:.2%}")
print(f"Probability of winning by not switching: {u/n:.2%}") 
    


