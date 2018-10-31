# Imports
from AjustableDataStore import AjustableDataStore as ads, UsageMethods as um
from CustomDataTypes import *
from CustomExeptions import *
import numpy as np
from Person import Person
#import random.randint
from  random import uniform

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
    FloorWeightings = None#TODO: create static initialisation function for these



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
        for i in count(randint(0, 3)):
            self.__people.Push(Person(__selectDest(), self.FloorNumber, TickTimer.GetCurrentTick()))

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

    def __selectDest(self):
        statValues = Floor.FloorWeightings[self.FloorNumber, int(TickTimer.GetCurrentSecondsOfDay() / 3600)]

        for prob in statValues:
            total = total + float(prob)

        chance = uniform(0, total)# Normal dist.?

        for value in statValues:
            iterator = iterator + float(value)

            if (iterator >= chance):
                break

            else:
                floor = floor + 1

        return floor

    

#-  Static Methods
    @staticmethod
    def Initialise(arrivalMeans, weightings):
        """
        Initialises the current tick, total ticks and seconds per tick values.

        Paramiters:
            int totalTicks - The total number of ticks being simulated.
            float secondsPerTick - The number of seconds in one simulated tick.
        """
        Floor.ArrivalMeans = arrivalMeans
        Floor.FloorWeightings = weightings




    #def __tickToTOD(tick):
    #    """
    #    Time of Day
    #    """
    #    #tickTime = tick/Ticks * 24
    #    #tickHours = int(tickTime)
    #    #tickMinutes = (tickTime - tickHours) * 60
    #    #return (tickHours,tickMinutes)
    #    return 13

    #def old__selectDestination(currentFloor,currentTick):
    #    realTime = __tickToTOD(currentTick)
    #    statValues = floorData[realTime[0]]
    #    statValues[currentFloor] = 0
    #    iterator = 0
    #    total = 0
    #    floor = 0
    #    for prob in statValues:
    #        total = total + float(prob)
    #    chance = uniform(0,total)
    #    for bob in statValues:
    #        iterator = iterator + float(bob)
    #        if (iterator >= chance):
    #            break
    #        else:
    #            floor = floor + 1
    #    return floor
