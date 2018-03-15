import sqlite3

with sqlite3.connect("quiz.db") as db:
    cursor = db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS user(
userID INT PRIMARY KEY,
username VARCHAR(20) NOT NULL,
firstName VARCHAR(20) NOT NULL,
lastName VARCHAR(20) NOT NULL,
password VARCHAR(20) NOT NULL
''')

cursor.execute("""
INSERT INTO user(username, firstname, lastname, password)
VALUES("Test_User","Bob","Smith","MrBob")

""")
db.commit()

cursor.execute("SELECT * FROM user")
print(cursor.fetchall())