import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_img = [rock, paper, scissors]

print("0.Rock")
print("1.Paper")
print("2.Scissors")

user_input =  int(input("Enter your choice: "))
computer_input  = random.randint(0, 2)

if user_input < 0 and user_input >= 3:
    print("You Loos, You have entered a invalid number ")
else:
    print("You have choosen: ")
    print(game_img[user_input])
    print("Computer have choosen: ")
    print(game_img[computer_input])

    if user_input == 0 and computer_input == 2:
        print("You Won")
    elif computer_input == 0 and user_input == 2:
        print("You Loss")
    elif user_input > computer_input:
        print("You Won")
    elif computer_input > user_input:
        print("You loss")
