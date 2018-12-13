"""
Script for outputting the data from a simulation batch and the graphs.
If not running from a command prompt, change the value of:
        the "settingsFilePath" variable below to access different data directories,
        the value of "batchID" to access the data from a specific batch,
        the value of "evaluateSim" to output the graphs for a specific simulation in a batch.
"""

# Settings
evaluateSim = None# Simulation number to display results for. Leave as None for best and worst simulations.
batchID = None# Batch to read data from
directoryPath = "./OliverLodge/OliverLodge"# Include the name of the file in the path but not the ".properties" extention!



# External Imports
from matplotlib import pyplot as plt
import numpy as np
import os
import sys

# Project Imports
from CustomDataTypes import *
from CustomExeptions import *
from GraphingClassFile import GraphingClass



# Make the directory setting an absolute filepath
directoryPath = os.path.abspath(directoryPath)



# Read filepath from console arguments
if len(sys.argv) > 1:
    if sys.argv[1] not in ["None", "none", "Null", "null"]:
        evaluateSim = int(sys.argv[1])

    if len(sys.argv) > 2:
        if sys.argv[2] not in ["None", "none", "Null", "null"]:
            batchID = sys.argv[2]

        if len(sys.argv) > 3:
            if sys.argv[3] not in ["None", "none", "Null", "null"]:
                if os.path.isfile(os.path.abspath(sys.argv[3]) + ".properties"):
                    directoryPath = sys.argv[3]

                else:
                    raise NoPathExistsException(sys.argv[1] + ".properties")



# Output the location of the specified data directory to inform the user
print("Using data from directory: \"{}\"".format(os.path.abspath(os.path.split(directoryPath)[0])))



#-  Load logs and graph data
DirectoryManager.Initialise(directoryPath)

data, times, positions, properties = DirectoryManager.ReadLogs()



#-  Initialise classes reliant on data
TickTimer.Initialise(properties.TotalTicks, properties.SecondsPerTick)


if __name__ == "__main__":
#- Output the raw data from the properties file
    print("Results:")
    for index, item in enumerate(data):
        if index == 0:
            print("    Batch ID = " + str(item))
        else:
            print("    " + DirectoryManager.batchDataProperties[index - 1][:-1].replace("_", " ").capitalize() + " = " + str(item))



#-  Output graphs
    # General data
    simAverageData = [GraphingClass.averageWaitingTimes([data[0:2] for data in simulation], TickTimer.TimeUnit.Hours) for simulation in times]
    simAverageTimes, simTimeIntervals = [simulation[0] for simulation in simAverageData], [simulation[1] for simulation in simAverageData]
    
    averageData = []
    for i in range(len(simAverageTimes)):
        for j in range(len(simAverageTimes[i])):
            averageData.append([TickTimer.GetTicks(simTimeIntervals[i][j] * 3600, True), simAverageTimes[i][j]])

    GraphingClass.Distribution([record[1] for record in averageData])

    GraphingClass.waitingTimeBarChart(averageData, TickTimer.TimeUnit.Hours, 5)



    # Selected or deafult simulation data
    if evaluateSim != None:
    #-  Selected sim
        # Lift Location - Disabled as not compatable with Juypter Notebooks. Uncomment and run file or .bat file from console to access graph
        #GraphingClass.LiftLocation(positions[evaluateSim], 0, "Simulation " + str(evaluateSim), properties.MinimumFloor, properties.MaximumFloor)#tick, lift, current, dest.
    
        # Average waiting time histogram
        GraphingClass.Distribution([record[1] for record in times[evaluateSim]])

        # Average waiting time each hour
        GraphingClass.waitingTimeBarChart([record[0:2] for record in times[evaluateSim]], TickTimer.TimeUnit.Hours, bottomOffsetFromMin = 5)



    else:# Do both best and worst sims
    #-  Best
        # Lift Location - Disabled as not compatable with Juypter Notebooks. Uncomment and run file or .bat file from console to access graph
        #GraphingClass.LiftLocation(positions[data.BestSim], 0, "Best Simulation", properties.MinimumFloor, properties.MaximumFloor)

        # Average waiting time histogram
        GraphingClass.Distribution([record[1] for record in times[data.BestSim]])

        # Average waiting time each hour
        GraphingClass.waitingTimeBarChart([record[0:2] for record in times[data.BestSim]], TickTimer.TimeUnit.Hours, bottomOffsetFromMin = 5)

    #-  Worst
        # Lift Location - Disabled as not compatable with Juypter Notebooks. Uncomment and run file or .bat file from console to access graph
        #GraphingClass.LiftLocation(positions[data.WorstSim], 0, "Worst Simulation", properties.MinimumFloor, properties.MaximumFloor)

        # Average waiting time histogram
        GraphingClass.Distribution([record[1] for record in times[data.WorstSim]])

        # Average waiting time each hour
        GraphingClass.waitingTimeBarChart([record[0:2] for record in times[data.WorstSim]], TickTimer.TimeUnit.Hours, bottomOffsetFromMin = 5)