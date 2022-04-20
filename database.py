import sqlite3


createfittnesstable ="CREATE TABLE IF NOT EXISTS participants (id INTEGER PRIMARY KEY, name TEXT, benchmax TEXT, squatmax TEXT, deadliftmax TEXT);"

insertdata = "INSERT INTO participants (name, benchmax, squatmax, deadliftmax) VALUES (?, ?, ?, ?);"

getall = "SELECT * FROM participants;"
getbyname = "SELECT * FROM participants WHERE name = ?;"
getbestbench = """
SELECT * FROM participants
ORDER by benchmax DESC
LIMIT 1;"""

getbestsquat = """
SELECT * FROM participants
ORDER by squatmax DESC
LIMIT 1;"""

getbestdeadlift = """
SELECT * FROM participants
ORDER by deadliftmax DESC
LIMIT 1;"""

def connect():
    return sqlite3.connect("data.db")

def createtable(connection):
    with connection:

        connection.execute(createfittnesstable)

def AddData(connection, name, benchmax, squatmax, deadliftmax):
    with connection:
        connection.execute(insertdata, (name, benchmax, squatmax, deadliftmax))

def GetAllData(connection):
    with connection:
        connection.execute(getall).fetchall()
def GetName(connection, name):
    with connection:
        connection.execute(getbyname, (name,)).fetchall()

def Get_Best_Bench(connection):
    with connection:
        connection.execute(getbestbench).fetchone()

def Get_Best_Squat(connection):
    with connection:
        connection.execute(getbestsquat).fetchone()

def Get_Best_Deadlift(connection):
    with connection:
        connection.execute(getbestdeadlift).fetchone()