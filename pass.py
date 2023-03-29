from cryptography.fernet import Fernet


# def Key():
#     key = Fernet.generate_key()

#     with open("key.key", "wb") as key_file:
#         key_file.write(key)


# Key() # to make key.key file


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)


def add():
    username = input("Enter Username:\t")
    passw = input("Enter password:\t")

    with open("password.txt", "a") as f:
        f.write(username + "<|>" + fer.encrypt(passw.encode()).decode() + "\n")


def view():
    with open("password.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            myUser, passwo = data.split("<|>")
            print(
                f"Username: {myUser} & Password: {fer.decrypt(passwo.encode()).decode()}"
            )


while True:
    taskInput = input(
        "Do you want to view(1) or add(0) a password? Press 'q' to quit. \t"
    )

    if taskInput == "1" or taskInput.lower() == "view":
        view()
    elif taskInput == "0" or taskInput.lower() == "add":
        add()
    elif taskInput.lower() == "q":
        print("Stopped the program!")
        break
    else:
        print("ERROR | Invalid Input")
from cryptography.fernet import Fernet


# def Key():
#     key = Fernet.generate_key()

#     with open("key.key", "wb") as key_file:
#         key_file.write(key)


# Key() # to make key.key file


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)


def add():
    username = input("Enter Username:\t")
    passw = input("Enter password:\t")

    with open("password.txt", "a") as f:
        f.write(username + "<|>" + fer.encrypt(passw.encode()).decode() + "\n")


def view():
    with open("password.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            myUser, passwo = data.split("<|>")
            print(
                f"Username: {myUser} & Password: {fer.decrypt(passwo.encode()).decode()}"
            )


while True:
    taskInput = input(
        "Do you want to view(1) or add(0) a password? Press 'q' to quit. \t"
    )

    if taskInput == "1" or taskInput.lower() == "view":
        view()
    elif taskInput == "0" or taskInput.lower() == "add":
        add()
    elif taskInput.lower() == "q":
        print("Stopped the program!")
        break
    else:
        print("ERROR | Invalid Input")
