from cryptography.fernet import Fernet

master_pwd=input("Enter your Master Password : ")

def write_key():

    key = Fernet.generate_key()
    with open("key.txt","wb") as key_file:
        key_file.write(key)


def view():

    with open('PASSWORDS.txt','r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user,passw = data.rsplit("|")
            print("User : ",user, " | Password : ",passw)

def add():

    name = input("Enter Acccount Name : ")
    pwd = input("Enter The Password : ")
    with open('PASSWORDS.txt','a') as f:

        f.write(name + "|" + pwd + "\n")

while True:

    mode=input("Which Mode Do You Want To Select ( View / Add). Press q to exit : ").lower()

    if mode == "q":
        break

    if mode=="view":
        view()

    elif mode=="add":
        add()
       
    else:

        print("enter a valid statement")
        continue