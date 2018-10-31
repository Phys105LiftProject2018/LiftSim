# Imports
from AjustableDataStore import AjustableDataStore as aj, UsageMethods as um
from CustomExeptions import *
import numpy as np
from Person import Person
import random.randint
import random.uniform

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
    FloorWeightings = None
    ArrivalMeans = None

#-  Constructor
    def __init__(self, floorNum):
        self.FloorNumber = floorNum
        
        self.__people = aj(um.Queue, Person)




        

        #floorData = []
        #with open('oliverLodge.csv', 'r') as csvfile:
        #    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        #    for row in spamreader:
        #        floorData.append(row)



        

#-  Methods
    def Update(self, currentTick):
        """
        Updates the floor's state. Adds more people to the floor.
        
        Paramiters:
            int currentTick - The tick on which the update is being performed.
        """
        for i in count(randint(0, 3)):
            self.__people.Push(Person(randint(0, 6), self.FloorNumber, currentTick))




        currentFloor = 0
        TickNow = 73
        Ticks = 2000

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

    def __tickToTOD(tick):
        """
        Time of Day
        """
        #tickTime = tick/Ticks * 24
        #tickHours = int(tickTime)
        #tickMinutes = (tickTime - tickHours) * 60
        #return (tickHours,tickMinutes)
        return 13

    def __selectDestination(currentFloor,currentTick):
        realTime = __tickToTOD(currentTick)
        statValues = floorData[realTime[0]]
        statValues[currentFloor] = 0
        iterator = 0
        total = 0
        floor = 0
        for prob in statValues:
            total = total + float(prob)
        chance = uniform(0,total)
        for bob in statValues:
            iterator = iterator + float(bob)
            if (iterator >= chance):
                break
            else:
                floor = floor + 1
        return floor
