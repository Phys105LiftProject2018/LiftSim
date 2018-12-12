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
        self.ticksbetweenfloors = 5 # will set as seconds and convert to ticks
        self.lockforticks = 0
        self.forceFloor = -1

        #TODO: add extra variable initialisation here

    def addCall(self,floor):
        '''
        Request that the lift travels to the floor passed as an argument.

        Returns a boolean with the value of whether the call was accepted or not.
        '''
        if floor >= self.minFloor and floor <= self.maxFloor:
            if len(self.targets) > 0: 
                if self.shouldReturn(self.currentFloor,self.targets[0],floor):
                    self.targets.insert(0,floor)
                    self.forceFloor = floor
                else:    
                    self.targets.append(floor)
            else:
                self.targets.append(floor)  
            return True
        else:
            return False
            # Handle the error of the floor not being a real floor inside the building

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

                if self.forceFloor == self.currentFloor:
                    self.forceFloor = -1
           
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
                if self.forceFloor != -1:
                    if self.forceFloor > self.currentFloor:
                        self.currentFloor += 1
                        self.lockforticks += self.ticksbetweenfloors
                    elif self.forceFloor < self.currentFloor:
                        self.currentFloor -= 1
                        self.lockforticks += self.ticksbetweenfloors
                else:
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

    def shouldReturn(self,currentFloor,requestedFloor,newRequestUpFrom):
        '''
        Calculates if quicker overall to go back when a request does not follow current path 
        '''
        adminTime = 17.5
        floorGapTime = 4.65
        maxFloors = self.maxFloor
        friendlyMultiplierMax = 2
        
        newReqDir = "down"
        if newRequestUpFrom == 0:
            newReqDir = "up"

            
        if requestedFloor > currentFloor:
            direction = "up"
            if newRequestUpFrom > currentFloor or newReqDir != "up":
                return False
            averageFloorNewFrom = (maxFloors - newRequestUpFrom)/2
            noBack = (abs(requestedFloor - currentFloor) * floorGapTime) + (abs(requestedFloor - newRequestUpFrom) * floorGapTime) + (averageFloorNewFrom * floorGapTime)+ (adminTime * 3)
            if (averageFloorNewFrom + newRequestUpFrom) < requestedFloor:
                goBack = (abs(currentFloor - newRequestUpFrom) * floorGapTime) + adminTime + (abs(requestedFloor - newRequestUpFrom) * floorGapTime) + adminTime
            else:
                goBack = (abs(currentFloor - newRequestUpFrom) * floorGapTime) + adminTime + (abs(averageFloorNewFrom + newRequestUpFrom) * floorGapTime) + adminTime
        else:
            direction = "down"
            if newRequestUpFrom < currentFloor or newReqDir != "down":
                return False
            averageFloorNewFrom = (0 + newRequestUpFrom)/2
            noBack = (abs(requestedFloor - currentFloor) * floorGapTime) + (abs(requestedFloor - newRequestUpFrom) * floorGapTime) + ((currentFloor - averageFloorNewFrom) * floorGapTime)+ (adminTime * 3)
            if averageFloorNewFrom > requestedFloor:
                goBack = (abs(currentFloor - newRequestUpFrom) * floorGapTime) + (abs(requestedFloor - newRequestUpFrom) * floorGapTime) + (adminTime * 3)
            else:
                goBack = (abs(currentFloor - newRequestUpFrom) * floorGapTime) + (abs(newRequestUpFrom - averageFloorNewFrom) * floorGapTime) + (adminTime * 3)

        
        originalCompletion = (abs(requestedFloor - currentFloor) * floorGapTime) + adminTime
        originalCompletionBack = (abs(currentFloor - newRequestUpFrom) * floorGapTime) + (abs(requestedFloor - newRequestUpFrom) * floorGapTime) + (adminTime * 2) 
        if (goBack < noBack) and (originalCompletionBack < originalCompletion * friendlyMultiplierMax):
            return True
        else:
            return False


