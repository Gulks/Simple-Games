#import time 
import random 

print("Hi. This is a guessing game. ")
print("You should guess a number from 1 to 20 in 6 steps. ") 
#Как думаешь, если пользователь захочет вводить (или нечаянно введет числа после 20-ти, т.е 
# сознательно будет просирать попытки, надо от этого защиту сделать или пофиг?)

number_guessed = random.randint(1,20)
guessesTaken = 0

def play():
    for guessesTaken in range(7):
        try: 
            user_number = int(input("Enter a number: ")) 
            guessesTaken += 1

            if user_number == number_guessed: 
                print("Congrats!!")
                print("You've done it in {} steps!".format(int(guessesTaken)))
                ask_user()

            elif guessesTaken == 6:
                print("Unfortunately, you lost. ")
                ask_user()

            else: 
                if user_number > number_guessed:
                    print("\nYou number is too big.\n ")
                else: 
                    print("\nYour number is too small.\n ")
        except ValueError: 
            print("You can't enter letters. Start again and enter numbers, please:)\n")  
            play()

def ask_user():
    answer = input("Do you want to play again? (yes/no) ") 
    if answer == 'yes' or answer == 'YES' or answer == 'ye' or answer == 'y':
        print("Ok:)") 
        play()
    else:
        print("Ok, bye!")
        quit()

play()