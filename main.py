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
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n "))
computer = [rock, paper, scissors]
computer_choice = random.choice(computer)
if user_choice == 0:
    print(f"User:\n {rock}")
    print("\nComputer: ")
    print(computer_choice)
    if computer_choice == rock:
        print("Draw 🤝")
    elif computer_choice == paper:
        print("You Loose ☹")
    elif computer_choice == scissors:
        print("You Win! 🎉")
elif user_choice == 1:
    print(f"User:\n {paper}")
    print("\nComputer: ")
    print(computer_choice)
    if computer_choice == rock:
        print("You Win! 🎉")
    elif computer_choice == paper:
        print("Draw 🤝")
    elif computer_choice == scissors:
        print("You Loose ☹")
elif user_choice == 2:
    print(f"User:\n {scissors}")
    print("\nComputer: ")
    print(computer_choice)
    if computer_choice == rock:
        print("You Loose ☹")
    elif computer_choice == paper:
        print("You Win! 🎉")
    elif computer_choice == scissors:
        print("Draw 🤝")
else:
    print("Enter a valid number")