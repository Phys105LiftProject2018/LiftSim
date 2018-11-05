import os
import string

booleanResponces = ("Y", "y", "Yes", "yes", "N", "n", "No", "no")
trueBooleanResponces = ("Y", "y", "Yes", "yes")
falseResponces = ("N", "n", "No", "no")

os.system("cls")

name = ""
pathToDir = ""

while True:
    while True:
        responce = input("Please enter the name of the simulation (spaces will be replaced with a \"_\"). The name must be a valid file name:\n>>> ")

        responce = responce.replace(" ","_")

        valid = True
        for char in responce:
            if char in ("*", ".", "\"", "/", "\\", "[", "]", ":", ";", "|", "=", ","):# Not a comprehensive test but should help prevent most issues.
                valid = False
                break

        if valid:
            name = responce
            break

        else:
            print("Invalid filename.")

    print()
    while True:
        responce = input("Create the directory in the current folder (\"Y\") or in a different folder (\"N\"):\n>>> ")

        if responce in booleanResponces:
            break
        else:
            print("Invalid responce. Please enter either \"Y\" or \"N\".")

    if responce in trueBooleanResponces:
        pathToDir = os.path.abspath(os.path.curdir)

    else:
        print()
        while True:
            responce = input("Please enter the absolute path of the file location in which the new directory should be created:\n>>> ")

            if os.path.isdir(responce):
                pathToDir = responce
                break

            else:
                print("The path provided is invalid. Please try again.")

    newDirectoryPath = os.path.join(pathToDir, name)

    if os.path.isdir(newDirectoryPath):
        os.system("cls")
        print("There is allready a directory called \"" + name + "\" at the location \"" + pathToDir + "\". Please try a different location or name.")
        continue

    else:
        break

os.mkdir(newDirectoryPath)

with open(os.path.join(newDirectoryPath, name + ".properties"), "w") as file:
    lines = [
                    "simulation name=",
                    "lowest floor number=",
                    "highest floor number=",
                    "secconds per tick=",
                    "total ticks="
                    ]

    for i in range(len(lines)):
        file.write(lines[i])
        if i != len(lines) - 1:
            file.write("\n")

open(os.path.join(newDirectoryPath, name + "_weightings.csv"), "w").close()
open(os.path.join(newDirectoryPath, name + "_arrivals.csv"), "w").close()

print("A new blank directory has been created at \"" + newDirectoryPath + "\".")
input("Press enter to exit... ")

