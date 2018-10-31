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

def ReadProperties(filename):
    """
    Reads and returns as strings the data in the specified properties file.

    Paramiters:
        string filename - the name (and path if not in the same folder as this file) of the the ".properties" file for the simulation. Exclude the file extention.

    Returns - list of strings
    """
    with open(filename + ".properties") as file:
        lines = [
                "simulation name=",
                "lowest floor number=",
                "highest floor number=",
                "secconds per tick=",
                "total ticks="
                ]

        for i, line in file.readlines():
            lines[i] = line[len(lines[i]):]

        return lines



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
    propertiesData = ReadProperties("./OliverLodge/OliverLodge")
    
    SimName = propertiesData[0]

    minFloor = int(propertiesData[1])
    maxFloor = int(propertiesData[2])

    secondsPerTick = float(propertiesData[3])
    totalTicks = int(propertiesData[4])
    
    floorWeightingsData = ReadCsv(SimName + "_weightings.csv")# Floor, hour
    arrivalMeansData = ReadCsv(SimName + "_arrivals.csv")# Floor, hour



#-  Format Data for Processing
    floorWeightings = np.array(floorWeightingsData)
    floorWeightings = np.array(arrivalMeansData)
    
    
    
#-  Set Constant Values
    TickTimer.Initialise(totalTicks, secondsPerTick)#TODO: change values to loaded data
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