import database


menuPrompt = """
Welcome to the database where you can enter all of your fitness tracking
Choose one of the options:
1 - Add data from a new person
2 - See the whole database
3 - Get the Personal Maxes of one individual 
4 - See who has the highest bench
5 - See who has the highest squat
6 - See who has the highest deadlift
7 - Exit

Your Selection:"""

def menu():
    connection = database.connect()
    database.createtable(connection)

    while(user_input := input(menuPrompt)) != "7":
        if user_input == "1":

        elif user_input == "2":
            DATA = database.GetAllData(connection)
            print(DATA)
        elif user_input == "3":
            pass
            #name = input("which name are you looking for?")
            #DATA = database.GetName(connection, name)
            #for i in DATA:
                #print(i)
        elif user_input == "4":
            pass
            #DATA = database.Get_Best_Bench(connection)
            #for i in DATA:
                #print(i)
        elif user_input == "5":
            pass
        elif user_input == "6":
            pass
        else:
            print("invalid input please try again")

menu()