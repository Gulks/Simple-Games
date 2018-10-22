import random

print("Hello, what is your name?")
name = input()        

print("Welcome, " + name + "! This is a 'Guess a number' game. Do you what to play it? Type 'Yes' or 'No'.")

def main():
    number = random.randint(1, 20)
    guessesTaken = 0

    answer = input()
    if answer == str("No") or answer == str("no") or answer == str("n"):
        print("Ok, " + name + ". Good bye!")
        quit()
    if answer == str("Yes") or answer == str("Y") or answer == str("yes") or answer == str("ye") or answer == str("y"):
        print("Well, " + name + ". I am thinking of a number between 1 and 20. You have 6 attempts to guess it.")  
            
    for guessesTaken in range(6):
        print("Try to guess!")
        guess = input()
        guess = int(guess)

        if guess < number:
            print("Your number is too low.")

        if guess > number:
            print("Your number is too high.")

        if guess == number:
            break

    if guess == number:
        guessesTaken = str(guessesTaken + 1)
        if guessesTaken == str(1):
            print("Congratulations, " + name + "! You've done it in " + guessesTaken + " attempt! Do you want to play again? Type 'Yes' or 'No'.")
        else:
            print("Congratulations, " + name + "! You've done it in " + guessesTaken + " attempts! Do you want to play again? Type 'Yes' or 'No'.")

        answer = input()
        if answer == str("Yes") or answer == str("Y") or answer == str("yes") or answer == str("ye") or answer == str("y"):
            print("Press Enter to start.")
            main()
        else:
            print("Ok, good bye!")
            quit()
    
    if guess != number:
        print("Unfortunately, " + name + ", you haven't guessed the number. Do you want to play again? Type 'Yes' or 'No'.")
        answer = input()
        if answer == str("Yes") or answer == str("Y") or answe == str("yes") or answer == str("ye") or answer == str("y"):
            print("Press Enter to start.")
            main()
        else:
            print("Ok, good bye!")
            quit()
    
main() 


    
    


     
    
    
    
   


