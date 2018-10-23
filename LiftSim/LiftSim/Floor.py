# Imports
from AjustableDataStore import AjustableDataStore as aj, UsageMethods as um
from CustomExeptions import *
import numpy as np
from Person import Person
import random.randint

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
#-  Constructor
    def __init__(self, floorNum, weighting):
        self.FloorNumber = floorNum
        self.Weighting = weighting
        self.__people = aj(um.Queue, Person)

        

#-  Methods
    def Update(self, currentTick):
        """
        Updates the floor's state. Adds more people to the floor.
        
        Paramiters:
            int currentTick - The tick on which the update is being performed.
        """
        for i in count(randint(0, 3)):
            self.__people.Push(Person(randint(0, 6), self.FloorNumber, currentTick))

    def GetPeople(self, maxNumber):
        """
        Retrives a specified number of people at most from the floor.

        Paramiters:
            int maxNumber - The maximum number of people that can me returned.

        Returns:
            A list of Person objects: minimum length = 0, maximum length, "maxNumber"
        """
        if maxNumber >= self.__people.Count:
            return self.__people.PopMany(maxNumber)
        else:
            return self.__people.PopMany(self.__people.Count)