# Imports
from AjustableDataStore import AjustableDataStore as ads, UsageMethods as um
from CustomDataTypes import *
from CustomExeptions import *
import numpy as np
from Person import Person
from random import uniform



class Floor(object):
    """
    Floor:
        Description of class.

        __init__(self, floorNum, weighting):
            int floorNum - The floors number in the building.
            float weighting - The weighting determining how likeley people are to want to arrive at the floor.

        Public Atributes:
            int FloorNumber - The floors number in the building.
            float Weighting - The weighting determining how likeley people are to want to arrive at the floor.
    """

#-  Static Atributes
    ArrivalMeans = None
    FloorWeightings = None



#-  Constructor
    def __init__(self, floorNum):
        """
        Paramiters:
            int floorNum - the floor number of the floor.
        """
        self.FloorNumber = floorNum
        
        self.__people = ads(um.Queue, Person)



#-  Methods
    def Update(self):
        """
        Updates the floor's state. Adds more people to the floor.
        """
        numberOfNewPeople = np.random.poisson(Floor.ArrivalMeans[int(TickTimer.GetCurrentSecondsOfDay() / 3600), self.FloorNumber] / 3600)
        for i in range(numberOfNewPeople):
            self.__people.Push(Person(self.__selectDest(), self.FloorNumber, TickTimer.GetCurrentTick()))

        if numberOfNewPeople > 0:
            return True
        else:
            return False

    def GetPeople(self, maxNumber):
        """
        Retrives a specified number of people at most from the floor.

        Paramiters:
            int maxNumber - The maximum number of people that can me returned.

        Returns:
            A list of Person objects: minimum length = 0, maximum length, "maxNumber"
        """
        if maxNumber <= self.__people.Count:
            return self.__people.PopMany(maxNumber)
        else:
            return self.__people.PopMany(self.__people.Count)

    def __selectDest(self):
        """
        Selects a destination floor using the weightings data.
        """
        # Copy the weightings for the current hour
        statValues = Floor.FloorWeightings[int(TickTimer.GetCurrentSecondsOfDay() / 3600)].copy()

        # Set properbility of current floor being destination to 0
        statValues[self.FloorNumber] = 0

        # Get the total proberbility (not nessessaraly 1!)
        total = 0
        for prob in statValues:
            total = total + float(prob)

        # Select a random float in the probability range
        chance = uniform(0, total)

        # Count up the floors untill the random is encompased by the addition of the probability of a single floor
        iterator = 0
        floor = 0
        for value in statValues:
            iterator = iterator + float(value)

            if (iterator >= chance):
                break

            else:
                floor = floor + 1

        # Return the selected floor
        return floor

    

#-  Static Methods
    @staticmethod
    def Initialise(arrivalMeans, weightings):
        """
        Initialises the statistical data for the floors.

        Paramiters:
            np.ndarray arrivalMeans - The mean data for people ariving at a floor on a given hour of the day. Format: (Hour, Floor)
            np.ndarray weightings - The mean data for destination floor on a given hour of the day. Format: (Hour, Floor)
        """
        Floor.ArrivalMeans = arrivalMeans
        Floor.FloorWeightings = weightings