# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# RRoot,1.1.2030,Created started script
# Changelog: M Kim, Nov 5, TODO Code added
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
strFile = "ToDoList.txt"   # An object that represents a file
strData = ""    # A row of text data from the file
dicRow = {}     # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []   # A dictionary that acts as a 'table' of rows
strMenu = ""    # A menu of user options
strChoice = ""  # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python Dictionary.

objFile = open(strFile, "r")
for row in objFile:
    lstRow = row.split(",")
    dicRow = {"task": lstRow[0], "priority": lstRow[1]}
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print(lstTable)
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        newTask = input("Enter Task: ")
        newPriority = input("Enter Priority: ")
        dicRow = {"task": newTask, "priority": newPriority + "\n"}
        lstTable.append(dicRow)
        continue

    # Step 5 - Remove a new item to the list/Table
    elif (strChoice.strip() == '3'):
        removeTask = input("Which task do you want to remove? Enter Task. ")
        i = 0
        for row in lstTable:
            if lstTable[i]['task'].strip().lower() == removeTask.strip().lower():
                lstTable.remove(row)
            i = i + 1
        continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open("ToDoToDoList.txt", "w")

        i=0
        while (i<len(lstTable)):
            objFile.write(lstTable[i]["task"])
            objFile.write(",")
            objFile.write(lstTable[i]["priority"])
            i = i+1
        objFile.close()
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("Thank you for using the program. Good bye!")
        break  # and Exit the program
