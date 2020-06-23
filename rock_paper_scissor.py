import random

user = 3

compt = 3

count = 0

while True:
    print("Please enter your choice\n 1.rock\n 2.paper\n 3.scissor\n[please enter the number]\n")

    choice = int(input("user turn: "))

    while choice > 3 or choice < 1:
        choice = int(input("enter valid input: "))

    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'paper'
    else:
        choice_name = 'scissor'

    print("user choice is: " + choice_name)

    print("\nNow its computer turn\n")

    comp_choice = random.randint(1, 3)

    while comp_choice == choice:
        comp_choice = random.randint(1, 3)

    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'paper'
    else:
        comp_choice_name = 'scissor'

    print("Computer choice is: " + comp_choice_name)

    print(choice_name + " V/s " + comp_choice_name)

    if ((choice == 1 and comp_choice == 2) or
            (choice == 2 and comp_choice == 1)):
        print("paper wins => ", end="")
        result = "paper"


    elif ((choice == 1 and comp_choice == 3) or (choice == 3 and comp_choice == 1)):
        print("Rock wins =>", end="")
        result = "Rock"

    else:
        print("scissor wins =>", end="")
        result = "scissor"

    if result == choice_name:
        print("<== User wins ==>")
        compt = compt - 1
        count = count + 1

        winner = ("user wins on ",count," rounds \nuser lives left", user,"\ncomputer lives left ",compt)
        f = open('Winner.txt', 'a')
        f.write(str(winner))
        f.write('\n')
        f.close()

        print("\n",winner,"\n")

    else:
        print("<== Computer wins ==>")
        user = user - 1
        count = count + 1

        winner1 = ("computer wins on ", count, " rounds\n computer lives left", compt, " \n user lives left ", user)
        f = open('Winner.txt', 'a')
        f.write(str(winner1))
        f.write('\n')
        f.close()

        print("\n",winner1,"\n")

    if user == 0:
        print("you lost")
        print("\ncomputer won\n")
        print("\ncomputer wins on ", count, " rounds\n computer lives left", compt, " \nuser lives left ", user,"\n")
        quit()

    elif compt == 0:
        print("computer lost")
        print("\nuser won\n")
        print("\n",user ,"wins on ",count," rounds \n user lives left", user," \n computer lives left ",compt)
        quit()