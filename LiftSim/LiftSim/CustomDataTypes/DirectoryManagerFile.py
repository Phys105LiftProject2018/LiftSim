import csv
import os
import string

from CustomDataTypes.SimulationDataFile import SimulationData

class DirectoryManager(object):
    """
    Handles the file operations for simulation directories.
    """
    propertiesBlankLines = [
                    "simulation_name=",
                    "lowest_floor_number=",
                    "highest_floor_number=",
                    "secconds_per_tick=",
                    "total_ticks="
                    ]

    DirectoryRoot = None

    __propertiesFilePath = None

    @staticmethod
    def Initialise(propertiesFilePath):
        DirectoryManager.__propertiesFilePath = propertiesFilePath
        DirectoryManager.DirectoryRoot = os.path.split(propertiesFilePath)[0]

    @staticmethod
    def ReadData():
        """
        """
        settings = DirectoryManager.ReadProperties(DirectoryManager.__propertiesFilePath)

        floorWeightingsData = DirectoryManager.ReadCsv(os.path.join(DirectoryManager.DirectoryRoot, settings[0] + "_weightings.csv"))# Floor, hour

        arrivalMeansData = DirectoryManager.ReadCsv(os.path.join(DirectoryManager.DirectoryRoot, settings[0] + "_arrivals.csv"))# Floor, hour

        return SimulationData(settings, floorWeightingsData, arrivalMeansData)

    @staticmethod
    def SaveLogs():
        pass

    @staticmethod
    def ReadProperties(filename):
        """
        Reads and returns as strings the data in the specified properties file.

        Paramiters:
            string filename - the name (and path if not in the same folder as this file) of the the ".properties" file for the simulation. Exclude the file extention.

        Returns - list of strings
        """
        with open(filename + ".properties") as file:
            lines = DirectoryManager.propertiesBlankLines.copy()

            for i, line in zip(range(len(lines)), file.readlines()):
                lines[i] = line[len(lines[i]):].strip("\n")

        return lines

    @staticmethod
    def ReadCsv(path):
        """
        Reads the csv data files.

        Returns - list of data
        """
        data = []

        with open(path, "r") as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')

            for row in spamreader:
                data.append(row)

        return data

    @staticmethod
    def CreateBlank():
        """
        Creates a blank simulation directory according to the user's specifications.
        """
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
            #lines = [
            #                "simulation name=",
            #                "lowest floor number=",
            #                "highest floor number=",
            #                "secconds per tick=",
            #                "total ticks="
            #                ]
            lines = DirectoryManager.propertiesBlankLines.copy()

            for i in range(len(lines)):
                file.write(lines[i])
                if i != len(lines) - 1:
                    file.write("\n")

        open(os.path.join(newDirectoryPath, name + "_weightings.csv"), "w").close()
        open(os.path.join(newDirectoryPath, name + "_arrivals.csv"), "w").close()

        print("A new blank directory has been created at \"" + newDirectoryPath + "\".")
        input("Press enter to exit... ")