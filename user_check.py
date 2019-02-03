import os

file = "name.txt"

def registerUser(user):
    with open(file, 'w') as f:
        f.write(user)
    f.close()

def checkUser():
    if os.path.getsize(file) <= 0:
        return True

def readUser():
    user_name = ""
    if not checkUser():
        with open(file, 'r') as f:
            for line in f:
                user_name = line
    return user_name
