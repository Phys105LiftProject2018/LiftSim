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

        #TODO: add extra variable initialisation here

    def addCall(self,floor):
        '''
        Request that the lift travels to the floor passed as an argument.

        Returns a boolean with the value of whether the call was accepted or not.
        '''
        raise NotImplementedError()#TODO: add logic here

    def update(self):
        '''
        Updates the lift object. This is to be run inside a loop.

        Each tick will move the lift up or down a whole floor.
        '''
        raise NotImplementedError()#TODO: add logic here

    #TODO: add extra methods and classes here
