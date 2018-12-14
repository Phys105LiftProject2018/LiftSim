# Imports
from CustomDataTypes import DirectoryManagerFile
import numpy as np
import os
from uuid import uuid4 as GenID



class SimulationData(object):
    """
    Holds the configuration properties for the simulation
    """
    def __init__(self, propertiesData, floorWeightingsData, arrivalMeansData):
        self.BatchID = str(GenID())

        self.SimName = propertiesData[0]

        self.LiftClassName = propertiesData[1]
        self.LiftClassPath = os.path.join(DirectoryManagerFile.DirectoryManager.DirectoryRoot, self.LiftClassName + ".py")

        self.MinimumFloor = int(propertiesData[2])
        self.MaximumFloor = int(propertiesData[3])
        self.NumberOfFloors = (self.MaximumFloor - self.MinimumFloor) + 1

        self.FloorWeightings = np.array(floorWeightingsData, float)
        self.ArrivalMeans = np.array(arrivalMeansData, float)

        self.SecondsPerTick = float(propertiesData[4])
        self.TotalTicks = int(propertiesData[5])

        self.NumberOfLifts = int(propertiesData[6])

        self.NumberOfItterations = int(propertiesData[7])

        # Private
        self.__maxCounter = 7# Maximum (index) value for the itteration counter

    def __iter__(self):
        self.__counter = 0

        return self

    def __next__(self):
        if self.__counter <= self.__maxCounter:
            
            if self.__counter == 0:
                result = self.BatchID
            elif self.__counter == 1:
                result = self.SimName
            elif self.__counter == 2:
                result = self.LiftClassName
            elif self.__counter == 3:
                result = self.LiftClassPath
            elif self.__counter == 4:
                result = self.MinimumFloor
            elif self.__counter == 5:
                result = self.MaximumFloor
            elif self.__counter == 6:
                result = self.NumberOfFloors
            elif self.__counter == 7:
                result = self.FloorWeightings
            elif self.__counter == 8:
                result = self.ArrivalMeans
            elif self.__counter == 9:
                result = self.SecondsPerTick
            elif self.__counter == 10:
                result = self.TotalTicks
            elif self.__counter == 11:
                result = self.NumberOfLifts
            elif self.__counter == 12:
                result = self.NumberOfItterations

            self.__counter += 1

            return result
            
        else:
            raise StopIteration



class SimulationResults(object):
    """
    Holds the results for a simulation batch
    """
    def __init__(self, id, propertiesData):
        self.BatchID = id

        self.LiftClassName = propertiesData[0]

        self.TotalMeanTime = float(propertiesData[1].split(" ")[0])

        self.SigmaMeanWaitingTimes = float(propertiesData[2].split(" ")[0])

        self.BestSim = int(propertiesData[3])

        self.BestMeanTime = float(propertiesData[4].split(" ")[0])

        self.WorstSim = int(propertiesData[5])

        self.WorstMeanTime = float(propertiesData[6].split(" ")[0])

        # Private
        self.__maxCounter = 7# Maximum (index) value for the itteration counter

    def __iter__(self):
        self.__counter = 0

        return self

    def __next__(self):
        if self.__counter <= self.__maxCounter:
            
            if self.__counter == 0:
                result = self.BatchID
            elif self.__counter == 1:
                result = self.LiftClassName
            elif self.__counter == 2:
                result = self.TotalMeanTime
            elif self.__counter == 3:
                result = self.SigmaMeanWaitingTimes
            elif self.__counter == 4:
                result = self.BestSim
            elif self.__counter == 5:
                result = self.BestMeanTime
            elif self.__counter == 6:
                result = self.WorstSim
            elif self.__counter == 7:
                result = self.WorstMeanTime

            self.__counter += 1

            return result
            
        else:
            raise StopIteration