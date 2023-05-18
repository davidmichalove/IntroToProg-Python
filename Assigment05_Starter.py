# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# <David Michalove>,<05/15/23>,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection
strFile = None # File handle

# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
print("\n Here are your current items if any:")
strFile = open(objFile, "r")
# Reads the data in the txt file
for row in strFile:
# Loops through the content within the txt file
    lstRow = row.split(",")
    # splits apart data based on a comma and returns a list
    dicRow = {"task":lstRow[0],"priority":lstRow[1].strip()}
    lstTable.append(dicRow)
    print(dicRow)
strFile.close()

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
    print()  # Adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        for objRow in lstTable:
        # Prints the contents of lstTable
            print(objRow)
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strTask = input("Enter Task: ")
        # Saves the user's input to the key: task.
        strPriority = input("Enter Priority: ")
        # Saves the user's input to the key: priority.
        dicRow = {"task": strTask, "priority": strPriority}
        # Main dictionary that will make up the lstTable
        lstTable.append(dicRow)
        # Puts dictionary into a list making a table
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        amountOptions = len(lstTable)
        # Gets the length of the table for indexing
        print("Here are your tasks so far:")
        for objRow in lstTable:
        # Prints the contents of lstTable
            print(objRow)

        term = int(input("What task/priority do you wish to remove?\nPlease choose from 0 to "+ str(amountOptions - 1) + ": "))
        # Gets the user's input for what term is wished to be removed
        while term >= amountOptions:
            # Uses the greater than or equal to cases because this part tests for an out of range index selection
            print("Please only respond with a number from 0 to " + str(amountOptions - 1) +".")
            term = int(input("What task/priority do you wish to remove?\nPlease choose from 0 to " + str(amountOptions - 1) + ": "))
        yesNo = input("You wish to remove: " + str(lstTable[term]) + "? [yes/no] ")
        # Asks user if they wish to proceed
        print(lstTable[term])
        if yesNo.lower() == "yes":
            lstTable.pop(term)
            # Removes and returns the selected dictionary so the user can see what has been deleted
        continue
    elif (strChoice.strip() == '4'):
    # Step 6 - Save tasks to the ToDoList.txt file
        open('ToDoList.txt', 'w').close()
        # Clears what is in the txt file so nothing will be duplicated by writing lstTable into the txt file
        objFile = open("ToDoList.txt", "a")
        for i in range(len(lstTable)):
        # Saves each dictionary pair to a txt file
            dItem = lstTable[i]
            print(dItem.get("task") + ", " + dItem.get("priority"))
            objFile.write(dItem.get("task") + ', ' + dItem.get("priority") + "\n")
        objFile.close()
        print("Saved!")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        finalYesNo = input("Do you wish to end the program? [yes/no] ")
        while finalYesNo.lower() != "yes" and finalYesNo.lower() != "no":
        # Ensures user will only respond within the asked for parameters
            print("Please only respond with: [yes/no] ")
            finalYesNo = input("Do you wish to end the program? [yes/no] ")
        if finalYesNo.lower() == "no":
            continue
        break # and Exit the program