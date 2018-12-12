import csv
import os
import string
from shutil import copyfile
import uuid
import datetime
import numpy as np


from CustomDataTypes.SimulationDataFile import SimulationData, SimulationResults
from LoggerFile import Logger

class DirectoryManager(object):
    """
    Handles the file operations for simulation directories.
    """
    propertiesBlankLines = [
                    "simulation_name=",
                    "lift_class_name=",
                    "lowest_floor_number=",
                    "highest_floor_number=",
                    "secconds_per_tick=",
                    "total_ticks=",
                    "number_of_lifts=",
                    "simulation_itterations="
                    ]

    #batchDataProperties = [
    #                        "lift_class_name=",
    #                        "mean_waiting_time_across_all_sims=",
    #                        "mean_waiting_time_across_all_sims2=",
    #                        "standard_deviation_of_waiting_times=",
    #                        "standard_deviation_of_mean_waiting_times=",
    #                        "lowest_mean_waiting_time_sim=",
    #                        "maximum_mean_waiting_time_sim="
    #                        ]

    batchDataProperties = [
                            "lift_class_name=",
                            "total_mean_time=",
                            #"total_mean_time2=",
                            #"sigma_waiting_times=",
                            "sigma_mean_waiting_times=",
                            "best_sim=",
                            "best_mean_time=",
                            "worst_sim=",
                            "worst_mean_time="
                            ]

    #file.write("Lift Class (algoritm): "+algorithm+"\n")
    #file.write("Mean Waiting Time across all sims: " +str( allMean)+"s\n")
    #file.write("Mean Waiting Time across all sims2: " +str( totalMean)+"s\n")
    #file.write("Standard Deviation of Waiting Time: "+str(totalStd)+"s\n")
    #file.write("Standard Deviation of Mean Waiting Time: "+str(totalStd)+"s\n")
    #file.write("Lowest Mean Waiting Time Sim: "+str(minMeanSim)+" -- "+str(round(simMeans[minMeanSim],2))+"s\n" )
    #file.write("Maximum Mean Waiting Time Sim: "+str(maxMeanSim)+" -- "+str(round(simMeans[maxMeanSim],2))+"s\n" )

    DirectoryRoot = None

    ApplicationRoot = os.path.split(os.path.split(__file__)[0])[0]

    __propertiesFilePath = None

    BooleanResponces = ("Y", "y", "Yes", "yes", "N", "n", "No", "no")
    TrueBooleanResponces = ("Y", "y", "Yes", "yes")
    FalseResponces = ("N", "n", "No", "no")

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
    def SaveLogs(dataObject):
        # Copy data from varius external sources
        timeData = Logger.recordedJourneyTicks
        positionData = Logger.LiftPosition
        algorithm = dataObject.LiftClassName

        # Create the subdirectory to hold the results
        DirectoryManager.CreateBlankLogBatch(dataObject.BatchID, dataObject.NumberOfItterations)
        
        # Update the file with this batch's ID
        file = open(os.path.join(DirectoryManager.DirectoryRoot, "Logs", "latest.txt"), "w")
        file.write(dataObject.BatchID)# + ";" + datetime.datetime.now().strftime('%d/%m/%Y'))
        file.close()

        # Write the data for each paralell simulation to its corisponding file
        for i in range(dataObject.NumberOfItterations):# For each paralell simulation
            with open(os.path.join(DirectoryManager.DirectoryRoot, "Logs", dataObject.BatchID, str(i), "WaitingTimeData.csv"), "a", newline = "") as file:
                fileWriter = csv.writer(file, "excel")
                for row in timeData[i]:
                    fileWriter.writerow(row)

            with open(os.path.join(DirectoryManager.DirectoryRoot, "Logs", dataObject.BatchID, str(i), "LiftPositionData.csv"), "a", newline = "") as file:
                fileWriter = csv.writer(file, "excel")
                fileWriter.writerows(positionData[i])
        
        # Write the data file in the root of the new subdirectory
        with open(os.path.join(DirectoryManager.DirectoryRoot, "Logs", dataObject.BatchID, "BatchData.properties"), "a") as file:
            simMeans = Logger.getSimMeans()
            totalMean = round(np.mean(simMeans),2)
            totalStd = round(np.std(simMeans),2)

            minMeanSim = np.argmin(simMeans)
            maxMeanSim = np.argmax(simMeans)

            #allTimes = Logger.getJourneyTimes()
            #allMean = round(np.mean(allTimes),2)
            #print(allTimes)
            #allStd = round(np.std(allTimes),2)

            writeData = [algorithm, str(totalMean) + " s", str(totalStd) + " s", str(minMeanSim), str(round(simMeans[minMeanSim],2)) + " s", str(maxMeanSim), str(round(simMeans[maxMeanSim],2)) + " s"]

            lines = DirectoryManager.batchDataProperties.copy()
            for i in range(len(lines)):
                lines[i] += writeData[i]

            for i in range(len(lines)):
                file.write(lines[i])
                if i != len(lines) - 1:
                    file.write("\n")

        # Copy data files to preserve data
        copyfile(os.path.join(DirectoryManager.DirectoryRoot, dataObject.SimName +  ".properties"), os.path.join(DirectoryManager.DirectoryRoot, "Logs", dataObject.BatchID, "simulation.properties"))
        copyfile(os.path.join(DirectoryManager.DirectoryRoot, dataObject.LiftClassName + ".py"), os.path.join(DirectoryManager.DirectoryRoot, "Logs", dataObject.BatchID, "lift.py"))
        copyfile(os.path.join(DirectoryManager.DirectoryRoot, dataObject.SimName + "_arrivals.csv"), os.path.join(DirectoryManager.DirectoryRoot, "Logs", dataObject.BatchID, "arrivals.csv"))
        copyfile(os.path.join(DirectoryManager.DirectoryRoot, dataObject.SimName + "_weightings.csv"), os.path.join(DirectoryManager.DirectoryRoot, "Logs", dataObject.BatchID, "weightings.csv"))


                
    @staticmethod
    def ReadLogs(batchID = None):
        """
        Reads the logs and data for a given batch.

        Paramiters:
            string batchID - the UUID of the batch (deafult is None for the latest batch)
        """
        if batchID == None:
            with open(os.path.join(DirectoryManager.DirectoryRoot, "Logs", "latest.txt"), "r") as file:
                batchID = file.readline()

        properties = SimulationData(DirectoryManager.ReadProperties(os.path.join(DirectoryManager.DirectoryRoot, "Logs", str(batchID), "simulation")), DirectoryManager.ReadCsv(os.path.join(DirectoryManager.DirectoryRoot, "Logs", str(batchID), "weightings.csv")), DirectoryManager.ReadCsv(os.path.join(DirectoryManager.DirectoryRoot, "Logs", str(batchID), "arrivals.csv")))
        analysisData = SimulationResults(str(batchID), DirectoryManager.ReadProperties(os.path.join(DirectoryManager.DirectoryRoot, "Logs", str(batchID), "BatchData"), True))

        timeData = []
        positionData = []

        for simulation in range(properties.NumberOfItterations):
            simTimeData = DirectoryManager.ReadCsv(os.path.join(DirectoryManager.DirectoryRoot, "Logs", str(batchID), str(simulation), "WaitingTimeData.csv"))
            simPositionData = DirectoryManager.ReadCsv(os.path.join(DirectoryManager.DirectoryRoot, "Logs", str(batchID), str(simulation), "LiftPositionData.csv"))

            simTimeData = np.array(simTimeData, float)

            for i in range(len(simPositionData)):
                if simPositionData[i][3] is "":
                    simPositionData[i][3] = 0.1

            simPositionData = np.array(simPositionData, float)

            for i in range(len(simPositionData)):
                if simPositionData[i][3] is 0.1:
                    simPositionData[i][3] = ""

            timeData.append(simTimeData)
            positionData.append(simPositionData)


        return (analysisData, timeData, positionData, properties)

    @staticmethod
    def ReadProperties(filename, batchData = False):
        """
        Reads and returns as strings the data in the specified properties file.

        Paramiters:
            string filename - the name (and path if not in the same folder as this file) of the the ".properties" file for the simulation. Exclude the file extention.
            boolean batchData - whether the file is a bach data file or a simulation properties file (deafult)

        Returns - list of strings
        """
        with open(filename + ".properties") as file:
            lines = None
            if batchData:
                lines = DirectoryManager.batchDataProperties.copy()
            else:
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
    def CreateNew():
        """
        Creates a blank simulation directory according to the user's specifications.
        """
        #booleanResponces = ("Y", "y", "Yes", "yes", "N", "n", "No", "no")
        #trueBooleanResponces = ("Y", "y", "Yes", "yes")
        #falseResponces = ("N", "n", "No", "no")

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

                if responce in DirectoryManager.BooleanResponces:
                    break
                else:
                    print("Invalid responce. Please enter either \"Y\" or \"N\".")

            if responce in DirectoryManager.TrueBooleanResponces:
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
                DirectoryManager.CreateBlankDirectory(name, newDirectoryPath)
                break
    
    @staticmethod
    def CreateBlankDirectory(name, newDirectoryPath):
        """
        Creates a blank data directory
        """
        os.mkdir(newDirectoryPath)

        with open(os.path.join(newDirectoryPath, name + ".properties"), "w") as file:
            lines = DirectoryManager.propertiesBlankLines.copy()

            for i in range(len(lines)):
                file.write(lines[i])

                if i == 1:
                    file.write("Lift")

                if i != len(lines) - 1:
                    file.write("\n")

        open(os.path.join(newDirectoryPath, name + "_weightings.csv"), "w").close()
        open(os.path.join(newDirectoryPath, name + "_arrivals.csv"), "w").close()

        copyfile(os.path.join(DirectoryManager.ApplicationRoot, "TEMPLATE Lift.py"), os.path.join(newDirectoryPath, "Lift.py"))

        os.mkdir(os.path.join(newDirectoryPath, "Logs"))

        open(os.path.join(newDirectoryPath, "Logs", "latest.txt"), "w").close()

        print("A new blank directory has been created at \"" + newDirectoryPath + "\".")
        input("Press enter to exit... ")

    @staticmethod
    def CreateBlankLogBatch(batchGuid, noSims):
        #with open(os.path.join(DirectoryManager.DirectoryRoot, "Logs", "latest.txt"), "w") as file:
        #    file.writelines(batchGuid)

        os.mkdir(os.path.join(DirectoryManager.DirectoryRoot, "Logs", str(batchGuid)))

        for i in range(noSims):
            os.mkdir(os.path.join(DirectoryManager.DirectoryRoot, "Logs", str(batchGuid), str(i)))