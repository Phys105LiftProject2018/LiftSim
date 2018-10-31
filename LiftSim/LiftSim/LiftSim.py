# External Imports
import numpy as np
from matplotlib import pyplot as plt

# Project Imports
from AjustableDataStore import AjustableDataStore as ads, UsageMethods as um
import csv
from CustomDataTypes import *
from CustomExeptions import *
from Floor import Floor
from Person import Person
from LiftOLL import LiftOLL

def ReadCsv(path):
    data = []

    with open(path, "r") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')

        for row in spamreader:
            data.append(row)

    return data

# Program Execution
if __name__ == "__main__":
#-  Expected Data Variables
    SimName = None

    minFloor = None
    maxFloor = None
    numberOfFloors = None

    floorWeightings = None
    arrivalMeans = None



#-  Load Data
    SimName = "OliverLodge"

    minFloor = 0
    maxFloor = 4
    
    floorWeightingsData = ReadCsv(SimName + "_weightings.csv")# Floor, hour
    arrivalMeansData = ReadCsv(SimName + "_arrivals.csv")# Floor, hour



#-  Format Data for Processing
    floorWeightings = np.array(floorWeightingsData)
    floorWeightings = np.array(arrivalMeansData)
    
    
    
#-  Set Constant Values
    TickTimer.Initialise(100, 1)#TODO: change values to loaded data
    Floor.Initialise(np.ones((numberOfFloors, 24)), floorWeightings)
    numberOfFloors = (maxFloor - minFloor) + 1



#-  Instantiate Objects
    # Create the lift
    lift = LiftOLL(0, numberOfFloors, 10)

    # Create an array with the floors
    floors = np.empty(numberOfFloors, Floor)
    for i in range(lenfloors):
        floors[i] = Floor(i)
    


#-  Main Loop
    while TickTimer.GetCurrentTick() < TickTimer.GetTotalTicks():
    #-  Update all objects
        lift.tick()
        
        for floor in floors:
            floor.Update()

    #-  Increce the tick
        TickTimer.IncrementTick()