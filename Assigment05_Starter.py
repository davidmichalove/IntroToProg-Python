# ------------------------------------------------- #
# Title: <Type the name of the script here>
# Description: <Type a description of the script>
# ChangeLog: (Who, When, What)
# <Example Dev,01/01/2030,Created Script>
# ------------------------------------------------- #

# -- Data -- #
# -- Processing -- #
# -- Presentation (I/O) -- #

objFile = open("HomeInventory.txt", "a")
lstItems = []
lstCosts = []
lstTable = [lstItems, lstCosts]
def Menu():
# This function allows the menu to be used various times without unnecessary lines of code.
    print("Menu of Options")
    print("1) Add Data to List")
    print("2) Display Current Data")
    print("3) Exit and Save to File")
Menu()
answer = input("Which option would you like to perform? [1 to 3] - ")
# This input response allows the while loop to begin.
while answer != "1" and answer != "2" and answer != "3":
# Uses the negation cases because this part tests for prohibited user inputs.
    print("Please only respond with: (1, 2, or 3) ")
    Menu()
    answer = input("Which option would you like to perform? [1 to 3] - ")
    # This ensures that the program will not accept any other response than the 3 integers.
while answer == "1" or answer == "2":
# Loops through until user enters "3" after each section.
    if answer == "1":
    # If user enters "1" then user can enter primary data.
        item = input("Name of item: ")
        cost = input("Value of " + item + ": ")
        lstItems.append(item)
        lstCosts.append(cost)
        Menu()
        answer = input("Which option would you like to perform? [1 to 3] - ")
        # This allows user to break this section of the while loop
        # and enter into the "elif answer == "2"" section or end the program.
    elif answer == "2":
        for i in range(len(lstItems)):
            print(lstItems[i]+ ":\t\t$" + lstCosts[i])
        Menu()
        answer = input("Which option would you like to perform? [1 to 3] - ")
        # Allows the user to enter into the while loop again or leave the program.

for i in range(len(lstItems)):
    save = (lstItems[i] + ":\t\t$" + lstCosts[i] +"\n")
    # Saves each item with cost to a text file.
    objFile.write(save)
print("Finished")
input("enter 'exit' to leave")


# strFile = open(objFile, "w")
strFile = open(objFile, "r")
for row in strFile:
    lstRow = row.split(",")
    # print(lstRow)
    # print(len(lstRow))
    # print(lstRow[0] + " | " + lstRow[1].strip())
    dicRow = {"task":lstRow[0],"priority":lstRow[1].strip()}
    print(dicRow)
strFile.close()    # diction = {lstRow[0], lstRow[1].strip()}
    # print(diction)


# TODO: Add Code Here
for objRow in lstTable:
    print(objRow)
# for myKey, myValue in dicRow.items():
#     print(myKey, " = ", myValue)
# strFile = open(objFile, "r")
# for row in strFile:
#     lstRow = row.split(",")
#     # print(lstRow[0] + " | " + lstRow[1].strip())
#     dicRow = {"task": lstRow[0], "priority": lstRow[1].strip()}
#     print(
#     print(dicRow)
# strFile.close()

  # print(lstTable.get("task") + ", " + lstTable.get("priority"))

        # print(dItem.get("task"))
        # print(dItem.get("priority"))
        # for task, priority in dItem.items():
        #     print(task, priority)
        # for objRow in lstTable:
        #     print(objRow)
            # print(frsRow[0] + ", " + frsRow[1].strip())

        # strFile.write(lstTable)
        # for item in lstTable:
        #     print(item)
            # dicRow = {"task": lstRow[0], "priority": lstRow[1].strip()}
            # print(dicRow)
            # for myKey, myValue in dicRow.items():
            #     print(myKey, ", ", myValue)
            # objFile.write(myKey, ", ", myValue)
        # for task, priority in dicRow.items():
        #     print(task, ", ", priority)
        # for row in lstTable:
        #     print(task, ", ", priority)
        # for task, priority in lstTable.items():
        #     print(task, ", ", priority)
        # objFile.write(myKey, ", ", myValue)
        # strFile.close()

        # for i in range(len(lstItems)):
        #     save = (lstItems[i] + ":\t\t$" + lstCosts[i] + "\n")
        #     # Saves each item with cost to a text file.
        #     objFile.write(save)


# for i in range(len(lstTable)):
#     # print(lstTable[i])
#     dItem = lstTable[i]
#     print(dItem.get("task") + ", " + dItem.get("priority"))
#     objFile.write(dItem.get("task") + ',' + dItem.get("priority") + "\n")


# while newTable.index(dicRow):
#     toDel = newTable.index(dicRow)
#     del newTable[toDel]

# if newTable.index(dicRow):
#     toDel = newTable.index(dicRow)
#     del newTable[toDel]

 # strFile = open(objFile, "w")
        # objFile = open("ToDoList.txt", "a")
        # print(lstTable[0])
        # dItem = lstTable[0]
        # print(dItem.get("task") + ", " + dItem.get("priority"))


# for i in range(len(lstTable)):
#     # print(lstTable[i])
#     dItem = lstTable[i]
#     print(dItem.get("task") + ", " + dItem.get("priority"))
#     objFile.write(dItem.get("task") + ',' + dItem.get("priority") + "\n")

    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here
        # newTable = lstTable.copy()

        # strFile = open(objFile, "r")
        # for row in strFile:
        #     lstRow = row.split(",")
        #     dicRow = {"task": lstRow[0], "priority": lstRow[1].strip()}
        #     newTable.index(dicRow)
        #     toDel = newTable.index(dicRow)
        #     del newTable[toDel]
        # strFile.close()