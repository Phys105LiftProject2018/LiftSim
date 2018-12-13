"""
The main file in the project. The simulation is run and controlled from this file.
If not running from a command prompt, change the value of the "settingsFilePath" variable below to access different data directories.
"""

import os
#directoryPath = os.path.abspath("./OliverLodge/OliverLodge")# Include the name of the file in the path but not the ".properties" extention!
#directoryPath = os.path.abspath("./bob/bob")
directoryPath = os.path.abspath("./CapacityDependantLiftOLL/CapacityDependantLiftOLL")

# External Imports
import numpy as np
import importlib
import sys
import traceback

# Project Imports
from AjustableDataStore import AjustableDataStore as ads, UsageMethods as um
from CustomDataTypes import *
from CustomExeptions import *
from Floor import Floor
from Person import Person
#from LiftOLL import LiftOLL
from LoggerFile import Logger
from GraphingClassFile import GraphingClass



# Read filepath from console arguments
if len(sys.argv) > 1:
    if os.path.isfile(os.path.abspath(sys.argv[1] + ".properties")):
        directoryPath = sys.argv[1]

    else:
        raise NoPathExistsException(sys.argv[1] + ".properties")

# Check existance of directory - if it dosen't exist, offer to create a blank one
if not os.path.isdir(os.path.split(directoryPath)[0]):
    result = None
    while True:
        result = input("The simulation directory provided dosen't exist. Would you like to create a blank simulation directory?\n>>> ")

        if result in DirectoryManager.BooleanResponces:
            break

    if result in DirectoryManager.TrueBooleanResponces:
        DirectoryManager.CreateBlankDirectory(os.path.split(os.path.split(directoryPath)[0])[1], os.path.split(directoryPath)[0])

    sys.exit()# Stop execution to allow the user to add data to the directory

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

# - Import Lift Class
#    try:
#        liftClassFile = __import__(dataObject.LiftClassPath)
#        liftClass = liftClassFile.Lift
#   except Exception as e:
#        print(e)
#       sys.exit()
    try:
        spec = importlib.util.spec_from_file_location(dataObject.LiftClassName + ".Lift", dataObject.LiftClassPath)
        liftClassFile = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(liftClassFile)

        #liftClassFile = __import__(dataObject.LiftClassPath)

        liftClass = liftClassFile.Lift
    except Exception as e:
        print(e)
        sys.exit()


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
            simLifts.append(liftClass(simNo, dataObject.MinimumFloor, dataObject.MaximumFloor, 10, allFloors[simNo]))

        allLifts.append(simLifts)
    

    
#-  Main Loop
    try:
        while TickTimer.GetCurrentTick() < TickTimer.GetTotalTicks():
        #-  Update all objects
            for simNumber in range(dataObject.NumberOfItterations):
                newCalls = []
                for index, floor in enumerate(allFloors[simNumber]):
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
            print("\r    [{}] Percentage Complete = {:.2f}% Current Location = {}".format("|" * int(percent/10) + " " * (10 - int(percent/10)), percent, allLifts[0][0].currentFloor), end = "    ")

        #-  Debug code TODO: remove before submission!
            #print(TickTimer.GetCurrentTick())
            #print(lift.currentFloor)
            #print()

    except Exception as e:
        print("\n--|  ERROR  |-- >>> Fatal error during simulation >>> " + str(e) + "\n")
        traceback.print_tb(e.__traceback__)
        print()

    print()
    
#-  Log save the logs
    try:
        DirectoryManager.SaveLogs(dataObject)

    except Exception as e:
        print("\n--|  ERROR  |-- >>> Fatal error during logging >>> " + str(e) + "\n")
        traceback.print_tb(e.__traceback__)
        print()