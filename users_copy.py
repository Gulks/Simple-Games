import re 
from time import sleep

users_names = []


def play_game():

    while True: 
        global users_names
        name = input("\nWhat is your name? ")
        name = re.sub("[^A-Za-z]", "", name) 
        users_names.append(name.title())
        ask_to_continue()  



def ask_to_continue(): 
    """Asks a user if they want to contunue entering names."""

    answer = input("\nDo you want to continue? ")

    if answer == 'no':
        sleep(1)
        confirmation = input("\nDo you want to see the list of users' names? ")

        if confirmation == 'no' or confirmation == 'n':
            save_users_names()
            sleep(1)
            print("\nOk, thanks for using our program. Good bye!") 
            quit()

        else:
            save_users_names() 
            show_names() 

    else:
        play_game() 



def save_users_names():
    """Users' names are saved in a separate text file."""

    global users_names 
    new_list = ''.join(users_names)
    f = open('users_names.txt', 'w')
    f.write(new_list)    
    f.close() 



def show_names():   
    """The users' names are shown.
    
    If there are several names, they're enumerated with comma 
    due to another function - 'enumerate_names'."""

    global users_names

    while '' in users_names:
        users_names.remove('')

    users_names = list(users_names)

    if len(users_names) == 0:
        sleep(1)
        print("\nThere are no names in the list.") 
        sleep(1)
        print("\nThanks for using our program. Good bye!\n")
        quit()

    elif len(users_names) == 1:
        sleep(1)
        print("\nThere is only one user name - {}.".format(users_names[0]))
        sleep(1) 
        print("\nIt is saved in a separate text document. Good bye!\n") 
        quit()

    elif len(users_names) == 2:
        sleep(1)
        print("\nThere are two names in the list - {0} and " \
            "{1}.".format(users_names[0], users_names[1])) 
        sleep(1)
        print("\nThey are saved in a separate text document. Good bye!\n") 
        quit()

    else:
        enumerate_names()
        sleep(1)
        print("\nThey are saved in a separate text document. "\
            "If you want to read them, open the file 'users_names'. "\
            "Good bye!\n") 
        quit()



def enumerate_names():
    """Enumerares users names with comma and does not depict the last one (comma)."""

    popped_name = users_names.pop(-1)
    print("The users names are: ", end='')
    for u_name in users_names:
        print(u_name, end=', ') 
    print(popped_name, end='')
    print(".") 



play_game() 
