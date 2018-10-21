# Imports
from LiftBase import LiftBase

class LiftOLL(LiftBase):
    """
    LiftOLL:
        This class is the lift that models the one in the Oliver Lodge Lab.

    """
    

    def __init__(self,minFloor,maxFloor,maxCapacity):
        LiftBase.__init__(self,minFloor,maxFloor,maxCapacity)

    def tick(self):
        '''
        Updates the lift object. This is to be run inside a loop.

        Each tick will move the lift up or down a whole floor.
        '''
        
        # If the current floor is a lift target, remove it from being a lift target
        try:
             self.targets.remove(self.floor) 
             # Open the lift doors to alight passengers??
        except ValueError:
            # Current floor is not a target
            pass


        # Filter the lift targets, if currently going up, only supply targets above current position and vice versa for down
        if self.state == LiftState.UP:
            targets = [floor for floor in self.targets if floor > self.floor]
            targets.sort()
        elif self.state == LiftState.DOWN:
            targets = [floor for floor in self.targets if floor < self.floor]
            targets.sort(reverse=True)
        elif self.state == LiftState.STANDING:
            targets = self.targets
            if targets:
                if targets[0] > self.floor:
                    self.state = LiftState.UP
                elif targets[0] < self.floor:
                    self.state = LiftState.DOWN


        # Move the lift if there are targets
        if targets:
            if targets[0] > self.floor:
                self.floor += 1
            elif targets[0] < self.floor:
                self.floor -= 1
            elif targets[0] == self.floor:
                self.targets.remove(self.floor)       
        else:
            # No targets for the lift
            self.state = LiftState.STANDING
        
