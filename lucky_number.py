import random 
import time 

lucky_numbers = []

while True:
    def play_game():
        global lucky_numbers
        name = input("\nWhat's your name? ")  
        time.sleep(1)
        print("Hello, {}!".format(name.title())) 
        number = random.randint(1,1000) 
        time.sleep(2)
        print("Your lucky number is {}.".format(str(number)))
        lucky_numbers.append(number) 

            
    def ask_user():
        global lucky_numbers
        time.sleep(1)
        answer = input("\nDo you want to play again? (yes/no) \n")

        if answer == 'no':
            if len(lucky_numbers) == 1:
                time.sleep(1)
                print("Ok. Bye!")
                quit()
                
            else: 
                time.sleep(1)
                print("\nOk. Your lucky numbers are: ")
                for lucky_number in lucky_numbers:
                    print(lucky_number) 
                time.sleep(1)
                print("Bye!")
                quit()
        else: 
            time.sleep(1)
            play_game()

    play_game()
    ask_user() 