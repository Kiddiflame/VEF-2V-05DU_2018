import sqlite3,time,sys

def login():
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    with sqlite3.connect("quiz.db") as db:
        cursor = db.cursor()
    find_user = ("SELECT * FROM user WHERE username =? AND password =?")
    cursor.execute(find_user,[(username),(password)])
    results = cursor.fetchall()

    if results:
        for i in results:
            print("Welcome " +i[2])
            break

    else:
        print("Username and password not recognized")
        again = input("Do you want to try again Y/N?: ")
        if again.lower() == "n":
            print("Goodbye")
            time.sleep(1)
            break

def newUser():
    found = 0
    while found == 0:
        username = input("Please enter a username: ")
        with sqlite3.connect("quiz.db") as db:
            cursor = db.cursor()
        findUser = ("SELECT * FROM user WHERE username = ?")
        cursor.execute(findUser,[(username)])

        if cursor.fetchall():
            print("Username taken, please try again")
        else:
            found = 1
    firstname = input("Enter your first name: ")
    lastname = input("Enter your last name: ")
    password = input("Enter your password: ")
    password1 = input("Reenter your password: ")
    while password != password1:
        print("Your passwords didn't match, please try again")
        password = input("Enter your password: ")
        password1 = input("Reenter your password: ")
    insertData = '''INSERT INTO user(username, firstName, lastName, password)
    VALUES(?,?,?,?)'''
    cursor.execute(insertData,[(username), (firstname), (lastname), (password)])
    db.commit()



def menu():
    while True:
        print("Welcome to my login thingy!")
        menu =('''
        1 - Create new user
        2 - Login to System
        3 - Exit System\n''')

        userchoice = input(menu)

        if userchoice == 1:
            newUser()

        elif userchoice == 2:
            login()

        elif userchoice == 3:
            print("Goodbye")
            sys.exit()

        else:
            print("Command not recognized")

menu()

