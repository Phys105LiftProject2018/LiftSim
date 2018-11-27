"""
The main file in the project. The simulation is run and controlled from this file.
If not running from a command prompt, change the value of the "settingsFilePath" variable below to access different data directories.
"""

import os
directoryPath = os.path.abspath("./OliverLodge/OliverLodge")# Include the name of the file in the path but not the ".properties" extention!

# External Imports
import numpy as np

# Project Imports
from AjustableDataStore import AjustableDataStore as ads, UsageMethods as um
from CustomDataTypes import *
from CustomExeptions import *
from Floor import Floor
from Person import Person
from LiftOLL import LiftOLL
from LoggerFile import Logger
from GraphingClassFile import GraphingClass



# Read filepath from console arguments
import sys
if len(sys.argv) > 1:
    if os.path.isfile(os.path.abspath(sys.argv[1] + ".properties")):
        directoryPath = sys.argv[1]

    else:
        raise NoPathExistsException(sys.argv[1] + ".properties")

print("Using data from directory: \"{}\"".format(os.path.abspath(os.path.split(directoryPath)[0])))



# Methods



# Program Execution
if __name__ == "__main__":
#-  Expected Data Variables
    SimName = None

    minFloor = None
    maxFloor = None
    numberOfFloors = None

    floorWeightings = None
    arrivalMeans = None

    secondsPerTick = None
    totalTicks = None



#-  Load Data
    DirectoryManager.Initialise(os.path.abspath(directoryPath))

    dataObject = DirectoryManager.ReadData()



#-  Set Constant Values
    Logger.Initialise(dataObject.NumberOfItterations, DirectoryManager.DirectoryRoot)
    TickTimer.Initialise(dataObject.TotalTicks, dataObject.SecondsPerTick)
    Floor.Initialise(dataObject.ArrivalMeans, dataObject.FloorWeightings)



#-  Instantiate Objects
    allFloors = []# list of floors in all simulations
    for simNo in range(dataObject.NumberOfItterations):
        # Create an array with the floors
        floors = np.empty(dataObject.NumberOfFloors, Floor)
        for i in range(len(floors)):
            floors[i] = Floor(i)

        allFloors.append(floors)

    allLifts = []
    for simNo in range(dataObject.NumberOfItterations):
        # Create the lifts
        simLifts = []
        for liftNo in range(dataObject.NumberOfLifts):
            simLifts.append(LiftOLL(simNo, dataObject.MinimumFloor, dataObject.MaximumFloor, 10, allFloors[simNo]))

        allLifts.append(simLifts)
    


#-  Main Loop
    try:
        while TickTimer.GetCurrentTick() < TickTimer.GetTotalTicks():
        #-  Update all objects
            for simNumber in range(dataObject.NumberOfItterations):
                newCalls = []
                for index,floor in enumerate(allFloors[simNumber]):
                    if floor.Update():
                        newCalls.append(index)

                for floor in newCalls:
                    for lift in allLifts[simNumber]:
                        lift.addCall(floor)

                for lift in allLifts[simNumber]:
                    lift.update()
        
        

        #-  Increce the tick
            TickTimer.IncrementTick()

        #-  Output Progress
            percent = 100 * (TickTimer.GetCurrentTick() / (TickTimer.GetTotalTicks()))
            print("\r    [{}] Percentage Compleate = {:.2f}% Current Location = {}".format("|" * int(percent/10) + " " * (10 - int(percent/10)), percent, allLifts[0][0].currentFloor), end = "    ")

        #-  Debug code TODO: remove before submission!
            #print(TickTimer.GetCurrentTick())
            #print(lift.currentFloor)
            #print()

    except Exception as e:
        print(e)
    
#-  Log save the logs
    DirectoryManager.SaveLogs(dataObject)