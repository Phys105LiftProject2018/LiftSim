# Imports
from LiftBase import LiftBase
from LoggerFile import Logger
from CustomDataTypes import *

class Lift(LiftBase):
    """
    TODO: lift description
    """
    
    def __init__(self,simID,minFloor,maxFloor,maxCapacity,floors):
        LiftBase.__init__(self,simID,minFloor,maxFloor,maxCapacity,floors)
        self.ticksbetweenfloors = 10 # will set as seconds and convert to ticks
        self.lockforticks = 0

    def update(self):
        '''
        Updates the lift object. This is to be run inside a loop.

        Each tick will move the lift up or down a whole floor.
        '''
        raise NotImplementedError()#TODO: add logic here

    #TODO: add extra methods and classes here
