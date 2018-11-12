import numpy as np
from uuid import uuid4 as GenID

class SimulationData(object):
    """
    """
    def __init__(self, propertiesData, floorWeightingsData, arrivalMeansData):
        self.BatchID = str(GenID())

        self.SimName = propertiesData[0]

        self.MinimumFloor = int(propertiesData[1])
        self.MaximumFloor = int(propertiesData[2])
        self.NumberOfFloors = (self.MaximumFloor - self.MinimumFloor) + 1

        self.FloorWeightings = np.array(floorWeightingsData, float)
        self.ArrivalMeans = np.array(arrivalMeansData, float)

        self.SecondsPerTick = float(propertiesData[3])
        self.TotalTicks = int(propertiesData[4])

        self.NumberOfLifts = int(propertiesData[5])

        self.NumberOfItterations = int(propertiesData[6])
