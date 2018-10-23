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

        __init__(list, of, paramiters):
            dataType param1 - Description
            dataType param2 - Description
            dataType param3 - Description

        Public Atributes:
            dataType Atribute1 - Description

        Static Atributes:
            dataType StaticAtribute1 - Description
    """
#-  Constructor
    def __init__(self, floorNum, weighting):
        self.FloorNumber = floorNum
        self.weighting
        self.__people = aj(um.Queue, Person)



#-  Methods
    def Update(self, currentTick):
        for i in count(randint(0, 3)):
            self.__people.Push(Person(randint(0, 6), self.FloorNumber, currentTick))

    def GetPeople(self, number):
        return self.__people.PopMany(number)