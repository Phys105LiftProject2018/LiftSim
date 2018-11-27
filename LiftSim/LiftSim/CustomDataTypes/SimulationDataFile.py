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
        #self.LiftClassPath = os.path.join(DirectoryManagerFile.DirectoryManager.DirectoryRoot,self.LiftClassName)
        self.LiftClassPath = self.LiftClassName

        self.MinimumFloor = int(propertiesData[2])
        self.MaximumFloor = int(propertiesData[3])
        self.NumberOfFloors = (self.MaximumFloor - self.MinimumFloor) + 1

        self.FloorWeightings = np.array(floorWeightingsData, float)
        self.ArrivalMeans = np.array(arrivalMeansData, float)

        self.SecondsPerTick = float(propertiesData[4])
        self.TotalTicks = int(propertiesData[5])

        self.NumberOfLifts = int(propertiesData[6])

        self.NumberOfItterations = int(propertiesData[7])
