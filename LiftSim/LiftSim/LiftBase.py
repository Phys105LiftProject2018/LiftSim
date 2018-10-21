# Imports
from enum import Enum

class LiftBase:
    """
    LiftBase:
        This class is the base class for a lift, which can then be inherited by another lift class for another algorithm.

    """
    class LiftState(Enum):
        '''
        An Enum for representing clearly the current state of a lift.
        
        Valid enums are UP , DOWN and STANDING.
        '''
        UP = 1
        DOWN = 2
        STANDING = 3

    

    def __init__(self,minFloor,maxFloor,maxCapacity):
        self.floor = 0
        self.state = self.LiftState.STANDING
        self.targets = []
        self.maxCapacity = maxCapacity
        self.passangers = []
        self.minFloor = minFloor
        self.maxFloor = maxFloor

    def addCall(self,floor):
        '''
        Request that the lift travels to the floor passed as an argument.

        Returns a boolean with the value of whether the call was accepted or not.
        '''
        if floor >= self.minFloor and floor <= self.maxFloor:
            self.targets.append(floor)
            return True
        else:
            return False
            # Handle the error of the floor not being a real floor inside the building

    def tick(self):
        '''
        --|| This method MUST be overridden. ||--
        Updates the lift object. This is to be run inside a loop.
         
        '''
        raise NotImplementedError
        