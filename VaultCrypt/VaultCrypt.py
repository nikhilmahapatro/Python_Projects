
#--------------------------------------------- VAULTCRYPT -------------------------------------------#
#----------------------------------------------------------------------------------------------------#

import os
# print("Saving key to directory:", os.getcwd())
from cryptography.fernet import Fernet
#___________________________________________________________________________________________________________________

# KEY MANAGEMENT

def gen_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)

def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key

if not os.path.exists("key.key"):
    gen_key()

key = load_key()
fer = Fernet(key)

#_________________________________________________________________________________________________________________

# MASTER KEY

def set_master_key():
    master_key=input("Set a Master Key:- ")
    with open("master.key","wb") as f:
        f.write(fer.encrypt(master_key.encode()))
    print("Master key has been set. Restart the program to use it.")
    exit()

def verify_master_key():
    if not os.path.exists("master.key"):
        print("No master key found. Let's create one")
        set_master_key()

    master_key = input("Enter master key:- ")
    with open("master.key","rb") as f:
        saved_encrypted = f.read()

    try:
        decrypted = fer.decrypt(saved_encrypted).decode()
        if decrypted == master_key:
            print("Access granted.")
        else:
            print("Incorrect Master key.")
            exit()
    except:
        print("Error decrypting master key.")
        exit()

#_________________________________________________________________________________________________________________

# PASSWORD FUNCTIONS

def add():
    site=input("What website/application does this password belong to? --> ")
    user_id=input("What is the user name/user ID? --> ")
    pwd=input("Enter a safe and secure password --> ")

    with open('PM_password.txt','a') as f:
        f.write(fer.encrypt(site.encode()).decode() + " ||| " + fer.encrypt(user_id.encode()).decode() + " ||| " +
                fer.encrypt(pwd.encode()).decode() + "\n")

def view():
    if not os.path.exists('PM_password.txt'):
        print("No passwords stored yet.")
        return

    with (open('PM_password.txt','r') as f):
        for line in f.readlines():
            data=line.rstrip()
            try:
                site, user_id, pwd = data.split(" ||| ")
                print("Site:- " + fer.decrypt(site.encode()).decode() + ", UserID:- " + fer.decrypt(
                    user_id.encode()).decode() + ", Password:- " + fer.decrypt(pwd.encode()).decode())
            except Exception as e:
                print("Malformed line:", data)
                print("Error:", e)

#____________________________________________________________________________________________________________________

# MAIN PROGRAM

verify_master_key()

while True:
    intention= input("\nWould you like to view existing passwords or add new ones?\nTo quit press \'Q\' \n(v/a/q) --> ").lower()
    if intention=='q':
        break

    if intention=='v':
        view()
    elif intention=='a':
        add()
    else:
        print("Sorry!! The option doesn't exist. Please try again.")


