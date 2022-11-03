import string
from string import Formatter
from pathlib import Path

import os
import time
import sys

print("Loading:")

animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
             "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

for i in range(len(animation)):
    time.sleep(0.2)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()

# print("\n")


menu = ""
url = ""
username = ""
password = ""
charSet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|\}]{[\"':;?/.< >,"


def fun_input():
    username = input('Enter User Name: ')  # take plan text user name
    password = input('Enter Password: ')  # take plan text password
    url = input('Enter URL: ')

    charSet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|\}]{[\"':;?/>.<, "

    encPass = "".join(charSet[(charSet.find(c) + 3) % 95] for c in password)  # rot 3 to encrypt password

    file = open('securePassword_3.txt', 'a')  # password save as txt file
    # print("Username\tPassword\tURL")
    file.write(username + ";" + encPass + ";" + url + "\n")
    file.close()
    print("Record succesfully added into the file")


def fun_display():
    header = 'Username\tPassword\tURL\n'
    header_value = 1
    path_to_file = 'securePassword_3.txt'
    path = Path(path_to_file)
    #data = None
    #print(path)


    if path.is_file():
        #print("Null value:", data)
        with open("securePassword_3.txt", 'r') as data_file:
            #print("Null value:", data)
            #print(path)

            if os.stat(path).st_size == 0:
                    print('File is  empty')
            else:
                for line in data_file:
                    data = line.split(";")

                    usr_value = data[0]
                    charSet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|\}]{[\"':;?./<,> "
                    
                    enc_pass_value = data[1]
                    dec_pass_value = "".join(charSet[(charSet.find(c) - 3) % 95] for c in enc_pass_value)  # decrypt the password
                    url_value = data[2]

                    if header_value == 1:
                        print(header)
                        print(usr_value + '\t\t' + dec_pass_value + '\t\t' + url_value)
                        header_value = 2
                    else:
                        print(usr_value + '\t\t' + dec_pass_value + '\t\t' + url_value)


    else :
        print('There is no password stored file.\n')


while menu != '1' or menu != '2' or menu != '3':
    menu = input('\n------Menu------'
                 '\n1. Insert Password'
                 '\n2. View Password'
                 '\n3. Exit'
                 '\nEnter selection: ')

    if menu == '1':
        fun_input()

    elif menu == '2':
        # file = open("securePassword_3.txt", "r")
        # print("url\tusername\tpassword")
        # print(file.read()) #to read encrypt txt file
        # print("Username\tPassword\tURL")
        fun_display()

    elif menu == '3':
        print("Program terminated")
        exit()

    else:
        print("Invalid Options. Please try again. \n")

