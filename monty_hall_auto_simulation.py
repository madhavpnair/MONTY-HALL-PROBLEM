import random 


    
total_no_of_trials=0
success_count_for_switching=0
success_count_for_NOT_switching=0

print("      Welcome! This is a simulation of the Monty-Hall problem")
n=int(input("Enter the number of attempts to be taken : "))
print()

for i in range(n):
    room_with_car=random.randint(1,3)
    user_input=random.randint(1,3)

    

    door_monty_opens=0

    for i in range(1,4):
        if((i!=user_input) and (i!=room_with_car)):
            door_monty_opens=i
    

    second_choice=room_with_car
    if(room_with_car==user_input):
        for i in range(1,4):
            if(i!=room_with_car) and (i!=door_monty_opens):
                second_choice=i
    
    
    if(second_choice==room_with_car):
        success_count_for_switching+=1

    
    else:
        success_count_for_NOT_switching+=1


    
print(f"  Total attempts: {n}" )
print(f"  switching won : {success_count_for_switching}")  
print(f"  unswitching won : {success_count_for_NOT_switching}") 
print()

print(f"Probability of winning by switching: {success_count_for_switching / n:.2%}")
print(f"Probability of winning by not switching: {success_count_for_NOT_switching / n:.2%}")        
    
        
    
    
