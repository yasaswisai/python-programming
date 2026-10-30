import random

print("welcome to rock-paper-scissors!\n")
print("winnig rules:")
print("rock vs paper -> paper wins")
print("rock vs scissors -> rock wins")
print("paper vs scissors -> scissors wins\n")

choices = ["rock","paper","scissors"]

while True:
    
    print("choose an option:")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")
    
    #validate user input
    try:
        choice  = int(input("enter your choice: "))
    except ValueError:
        print("pls enter a valid number.\n")
        continue
    
    while choice < 1 or choice > 3:
        choice = int(input("pls enter a valid choice (1-3): "))
        
    #user choice
    user_choice = choices[choice-1]
    
    print("\n user choice is:", user_choice)
    
    #computer choice
    comp_choice = random.randint(1,3)
    computer_choice = choices[comp_choice-1]
    
    print("computer choice is: ", computer_choice)
    print(user_choice , "vs" , computer_choice)
    
    #determine winner
    if user_choice == computer_choice:
        print("its a tie")
    elif(
        (choice == 1 and comp_choice == 2) or
        (choice == 2 and comp_choice == 3) or
        (choice == 3 and comp_choice == 1)
    ):
        print("user wins")
    else:
        print("computer wins")
        
    #play again
    while True:
        ans = input("\n do u wanna play again(y/n):").lower()
        
        if ans in ["y","n"]:
            break
        print("pls enter y or n")
    
    if ans == 'n':
        break
    
    print()

print("thanks for playing")
