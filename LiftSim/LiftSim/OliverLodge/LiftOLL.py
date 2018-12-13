# Imports
from LiftBase import LiftBase
from LoggerFile import Logger
from CustomDataTypes import *

class Lift(LiftBase):
    """
    LiftOLL:
        This class is the lift that models the one in the Oliver Lodge Lab.

    """
    

    def __init__(self,simID,minFloor,maxFloor,maxCapacity,floors):
        LiftBase.__init__(self,simID,minFloor,maxFloor,maxCapacity,floors)
        self.ticksbetweenfloors = 5 # will set as seconds and convert to ticks
        self.lockforticks = 0

    def update(self):
        '''
        Updates the lift object. This is to be run inside a loop.

        Each tick will move the lift up or down a whole floor.
        '''
            
        # Is the lift moving? If it isn't the lift can act
        if self.lockforticks == 0:
            # If the current floor is a lift target, remove it from being a lift target
            if self.currentFloor in self.targets:
                Logger.LogLiftPosition(self.simID,0,self.currentFloor,None)


                self.lockforticks += 9 #Admin time for opening

                # remove current floor from targets
                self.targets = [target for target in self.targets if target != self.currentFloor]

                # --------- Handle passangers
                # self.passengers - remove people who want this floor -> (arrival tick = current tick + lock for ticks)
                # This is because of the time is takes for the door to open. 

                peopleGettingOut = [person for person in self.passengers if person.destination == self.currentFloor]

                # +2 on arrival tick is from the admin time of opening doors to get out
                for person in peopleGettingOut:
                    Logger.recordJourney(self.simID,person,arrivalTick = TickTimer.GetCurrentTick() + 9)

                self.passengers = [person for person in self.passengers if person.destination != self.currentFloor]
                # accept passengers from the floor
                
                capacityRemaining = self.maxCapacity - len(self.passengers)

                newPassengers = self.floors[self.currentFloor].GetPeople(capacityRemaining)
                
                for person in newPassengers:
                    self.addCall(person.destination)

                self.passengers += newPassengers

                self.lockforticks += 8
           
            # ---------- Set the lift moving

            # Filter the lift targets, if currently going up, only supply targets above current position and vice versa for down
            if self.state == LiftBase.LiftState.UP:
                targets = [floor for floor in self.targets if floor > self.currentFloor]
                targets.sort()
            elif self.state == LiftBase.LiftState.DOWN:
                targets = [floor for floor in self.targets if floor < self.currentFloor]
                targets.sort(reverse=True)
            elif self.state == LiftBase.LiftState.STANDING:
                targets = self.targets
                if targets:
                    if targets[0] > self.currentFloor:
                        self.state = LiftBase.LiftState.UP
                    elif targets[0] < self.currentFloor:
                        self.state = LiftBase.LiftState.DOWN

        

            # Move the lift if there are targets
            if targets:
                #Logger.LogLiftPosition(self.simID,0,self.currentFloor,targets[0])
                if targets[0] > self.currentFloor:
                    self.currentFloor += 1
                    self.lockforticks += self.ticksbetweenfloors
                elif targets[0] < self.currentFloor:
                    self.currentFloor -= 1
                    self.lockforticks += self.ticksbetweenfloors
                     
            else:
                # No targets for the lift
                self.state = LiftBase.LiftState.STANDING
                self.lockforticks = 0 # no targets, lift ready to move so lock is 0
        
        else:
            self.lockforticks -= 1

