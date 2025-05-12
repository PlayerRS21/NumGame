from pyfiglet import Figlet

import os

import random

import time

import sys

from enc import encrypt,decrypt

i = 1

def verify_login(username, password):

    try:

        with open(".credential.txt", "r") as file:

            for line in file:

                stored_username, stored_password = line.strip().split(":")

    except FileNotFoundError:

        print("Credentials Deleted!!!\nSignup Again: ")

        time.sleep(2)

        signup()

    stored_user = str(decrypt(stored_username))

    stored_pass = str(decrypt(stored_password))

    if stored_user == str(username) and stored_pass == str(password):

        print("Login Successful\nRedirecting to Game...")

        time.sleep(1)

        game()

        return  # Important to stop further execution

        # If loop finishes without finding a match

    else:

        print("Login Failed\nRedirecting to Login Screen...")

        time.sleep(1)

        login()


def game():

    def chance(num, list1):

        global i

        while i < 4:

            guess = input(f"Guess A Number Between 1 to {len(list1)} {{{i}/3}}\n=>")

            try:

                if int(guess) == num:

                    print(f3.renderText("You  Guess Correct!!!"))

                    again()

                else:

                    i = i + 1

                    if int(guess) > num:

                        print("Entered Value is Too High")

                    else:

                        print("Entered Value is Too Small")

            except ValueError:

                print("Enter Correct Input")

        else:

            print(f3.renderText("You  Lose!!!"))

            again()

    def again():

        global i

        aga = input("Play Again (y/n) ")

        if aga.lower() == "y":

            i = 1

            os.system("cls" if os.name == "nt" else "clear")

            level()

        elif aga.lower() == "n":

            print("Exiting in 3 seconds\nYou Played Well!!!")

            time.sleep(3)

            sys.exit(0)

        else:

            print("Enter Correct Input")

            again()

    f1 = Figlet(font="standard")

    f2 = Figlet(font="cyberlarge")

    f3 = Figlet(font="epic")

    os.system("cls" if os.name == "nt" else "clear")

    # nums = ""

    with open("numlist.txt") as wlist:

        line = wlist.readline()

        # global nums

        nums = line.strip().split(",")

    # print(nums)

    def play(l):

        digit = int(random.choice(l))

        chance(digit, l)

    def lv1():

        first_10 = nums[0:10]

        play(first_10)

    def lv2():

        first_20 = nums[0:20]

        play(first_20)

    def lv3():

        first_50 = nums[0:50]

        play(first_50)

    def lv4():

        first_100 = nums[0:100]

        play(first_100)

    print(f1.renderText("Welcome To"), end="")

    print(f2.renderText("Number Guessing"), end="")

    print(f3.renderText("Game"))

    inp = input("Press Any Key To Start...")

    os.system("cls" if os.name == "nt" else "clear")

    def ques(a):

        try:

            if int(a) == 1:

                lv1()

                print("Level 1")

            elif int(a) == 2:

                lv2()

                # print("Level 2")

            elif int(a) == 3:

                lv3()

                # print("Level 3")

            elif int(a) == 4:

                lv4()

                # print("Level 4")

            else:

                os.system("cls" if os.name == "nt" else "clear")

                print("Enter Valid Input...")

                level()

        except ValueError:

            os.system("cls" if os.name == "nt" else "clear")

            print("Enter Integer Input...")

            # level()

    def level():

        inp1 = input("Choose Difficulty\n1. Easy\n2. Normal\n3. Hard\n4. Extreme\n")

        print(inp1)

        ques(inp1)

    level()

def signup():

    os.system('cls' if os.name == 'nt' else 'clear')

    uname = input("Enter Your UserName to register or exit to return and don't use Numbers in username: ")

    if uname==" " or uname=="":

        print("Enter valid username...")

        signup()

    elif uname =="exit":

        main()

    else:

        pswd2 = str(input("Enter Your Password to login don't use numbers: "))

        pswd3 = str(input("Enter Your Password Again: "))

        if pswd2 == pswd3:
                
            confirm = input("Do you want to continue(y/n): ")

            if confirm.lower() =="y" or confirm.lower == "yes":

                with open(".credential.txt", "a") as file:

                    uname_new = encrypt(uname)

                    pswd2_new = encrypt(pswd2)

                    file.write(f"{uname_new}:{pswd2_new}\n")

                print("Signup Successful!!!")

                ch = input("Press any key to continue...")

                login()

            else:
                    
                print("Signup Failed!!! Redirecting you to main screen in 3 seconds...")

                time.sleep(3)

                signup()

def login():

    os.system('cls' if os.name == 'nt' else 'clear')

    inp_user = input("Enter Your UserName or exit to return: ")

    if inp_user =="exit":

        main()

    elif inp_user == "" or inp_user == " ":

        print("Enter Correct Username...")

        time.sleep(2)

        login()

    else:

        inp_pswd = input("Enter Your Password: ")

        verify_login(inp_user,inp_pswd)

        # if inp_user in user:

        #     index = user.index(inp_user)

        #     if str(inp_pswd) == str(pswd[index]):

        #         print("Login Successfull!!!\nRedirecting to Game...")

        #         time.sleep(2)

        #         os.system('cls' if os.name == 'nt' else 'clear')

        #         game()
            
        #     else:

        #         print("Credientials Mismatch!!\nRedirecting to Login Screen...")

        #         time.sleep(1)

        #         os.system('cls' if os.name == 'nt' else 'clear')

        #         login()

        # else:

        #     print("No user found\nRedirecting to Login Screen...")

        #     time.sleep(1)

        #     os.system('cls' if os.name == 'nt' else 'clear')

        #     login()

def main():

    os.system('cls' if os.name == 'nt' else 'clear')

    try:

        inp = int(input("Enter 0 to login or 1 to signup..."))

        if inp==0:
        
            os.system('cls' if os.name == 'nt' else 'clear')

            login()

        elif inp == 1:
            
            os.system('cls' if os.name == 'nt' else 'clear')

            signup()

        else:

            print("Enter Correct Value...")

            time.sleep(1)
            
            main()

    except ValueError:

        print("Enter Correct Value...")

        time.sleep(1.5)

        os.system('cls' if os.name == 'nt' else 'clear')

        main()

main()
