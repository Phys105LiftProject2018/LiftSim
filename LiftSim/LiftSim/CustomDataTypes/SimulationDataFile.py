import numpy as np
from uuid import uuid4 as GenID
import os
from CustomDataTypes import DirectoryManagerFile

class SimulationData(object):
    """
    """
    def __init__(self, propertiesData, floorWeightingsData, arrivalMeansData):
        self.BatchID = str(GenID())

        self.SimName = propertiesData[0]

        self.LiftClassName = propertiesData[1]
        self.LiftClassPath = os.path.join(DirectoryManagerFile.DirectoryManager.DirectoryRoot, self.LiftClassName + ".py")
        #self.LiftClassPath = self.LiftClassName

        self.MinimumFloor = int(propertiesData[2])
        self.MaximumFloor = int(propertiesData[3])
        self.NumberOfFloors = (self.MaximumFloor - self.MinimumFloor) + 1

        self.FloorWeightings = np.array(floorWeightingsData, float)
        self.ArrivalMeans = np.array(arrivalMeansData, float)

        self.SecondsPerTick = float(propertiesData[4])
        self.TotalTicks = int(propertiesData[5])

        self.NumberOfLifts = int(propertiesData[6])

        self.NumberOfItterations = int(propertiesData[7])



class SimulationResults(object):
    """
    """
    def __init__(self, id, propertiesData):
        self.BatchID = id

        self.LiftClassName = propertiesData[0]

        self.TotalMeanTime, = float(propertiesData[1])

        self.TotalMeanTime2 = float(propertiesData[2])

        self.SigmaWaitingTimes = float(propertiesData[3])

        self.SigmaMeanWaitingTimes = float(propertiesData[4])

        self.BestSim = str(propertiesData[5])

        self.BestMeanTime = float(propertiesData[6])

        self.WorstSim = str(propertiesData[7])

        self.WorstMeanTime = float(propertiesData[8])