from time import sleep
from random import choice 

print("Hi! This is program which checks if the number you enter is "\
"prime or not.")

prime_numbers = []
not_prime_numbers = []


def show_lists():  

    if len(prime_numbers) == 1 and len(not_prime_numbers) == 0:
        print("The prime number is {}".format(prime_numbers[0]))

    elif len(not_prime_numbers) == 1 and len(prime_numbers) == 0:
        print("Not prime number is {}".format(not_prime_numbers[0]))

    elif len(prime_numbers) > 1 and len(not_prime_numbers) == 0:
        print("Prime numbers are: {}".format(prime_numbers)) ###

    elif len(not_prime_numbers) > 1 and len(prime_numbers) == 0:
        print("Not prime numbers are: {}".format(not_prime_numbers)) ###

    elif len(prime_numbers) > 1 and len(not_prime_numbers) == 1:
        print("Prime numbers are: {}".format(prime_numbers)) ###
        print("Not prime number is {}".format(not_prime_numbers[0]))

    elif len(not_prime_numbers) > 1 and len(prime_numbers) == 1:
        print("The prime number is {}".format(prime_numbers[0]))
        print("Not prime numbers are: {}".format(not_prime_numbers))  ###
    
    elif len(prime_numbers) == 1 and len(not_prime_numbers) == 1:
        print("The prime number is {}".format(prime_numbers[0]))
        print("Not prime number is {}".format(not_prime_numbers[0]))
    
    else:
        print("Prime numbers are: {}".format(prime_numbers)) ###
        print("Not prime numbers are: {}".format(not_prime_numbers)) ###
        

def ask_user():
    """The function asks user if they want to continue checking numbers."""
    
    replies = ["Do you want to check another one? ", 
    "Do you want to check another number? ", "Do you want to continue? "] 
    reply = choice(replies)
    answer = input(reply)

    if answer == 'no':
        sleep(1)
        print("Ok, thanks for using the program! ")
        sleep(1)
        show_lists()
        quit()
    else: 
        sleep(1)
        find_prime_number()


def find_prime_number():
    """The function finds prime numbers.
    
    It will say the user if the number is prime or not.
    Then the prog adds the numbers to the lists (with prime
    numbers and not correspondingly)."""

    while True:
        global prime_numbers
        global not_prime_numbers
        
        try:     
            sleep(1)
            x = int(input("\nEnter a number: "))

        except ValueError:
            sleep(1)
            print("You can't enter letters.")
            sleep(1)
            find_prime_number()

        else:
            if x % 2 != 0:
                sleep(1)
                print("The number is prime.\n")
                prime_numbers.append(x) 
                sleep(1)
                ask_user()

            else:
                sleep(1)
                print("The number isn't prime.\n")
                not_prime_numbers.append(x) 
                sleep(1)   
                ask_user() 

find_prime_number()
