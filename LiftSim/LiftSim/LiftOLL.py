# Imports
from LiftBase import LiftBase

class LiftOLL(LiftBase):
    """
    LiftOLL:
        This class is the lift that models the one in the Oliver Lodge Lab.

    """
    

    def __init__(self,minFloor,maxFloor,maxCapacity,floors):
        LiftBase.__init__(self,minFloor,maxFloor,maxCapacity,floors)
        self.ticksbetweenfloors = 10 # will set as seconds and convert to ticks
        self.lockforticks = 0

    def update(self):
        '''
        Updates the lift object. This is to be run inside a loop.

        Each tick will move the lift up or down a whole floor.
        '''
            
        # Is the lift moving? If it isn't the lift can act
        if self.lockforticks == 0:
            # If the current floor is a lift target, remove it from being a lift target
            if self.floor in self.targets:
                self.lockforticks += 2 #Admin time for opening

                # remove current floor from targets
                self.targets = [target for target in self.targets if target != self.floor]

                # --------- Handle passangers
                # self.passengers - remove people who want this floor -> (arrival tick = current tick + lock for ticks)
                # This is because of the time is takes for the door to open. 

                peopleGettingOut = [person for person in self.passengers if person.destination == self.floor]

                # +2 on arrival tick is from the admin time of opening doors to get out
                #for person in peopleGettingOut:
                #    person.arrivalTick = TickTimer.GetCurrentTick() + 2

                self.passengers = [person for person in self.passengers if person.destination != self.floor]
                # accept passengers from the floor
                
                capacityRemaining = self.maxCapacity - len(self.passengers)

                self.floors[self.currentFloor].GetPeople(capacityRemaining)


                self.lockforticks += 2
           
            # ---------- Set the lift moving

            # Filter the lift targets, if currently going up, only supply targets above current position and vice versa for down
            if self.state == LiftBase.LiftState.UP:
                targets = [floor for floor in self.targets if floor > self.floor]
                targets.sort()
            elif self.state == LiftBase.LiftState.DOWN:
                targets = [floor for floor in self.targets if floor < self.floor]
                targets.sort(reverse=True)
            elif self.state == LiftBase.LiftState.STANDING:
                targets = self.targets
                if targets:
                    if targets[0] > self.floor:
                        self.state = LiftBase.LiftState.UP
                    elif targets[0] < self.floor:
                        self.state = LiftBase.LiftState.DOWN

        

            # Move the lift if there are targets
            if targets:
                if targets[0] > self.floor:
                    self.floor += 1
                    self.lockforticks += self.ticksbetweenfloors
                elif targets[0] < self.floor:
                    self.floor -= 1
                    self.lockforticks += self.ticksbetweenfloors
                     
            else:
                # No targets for the lift
                self.state = LiftBase.LiftState.STANDING
                self.lockforticks = 0 # no targets, lift ready to move so lock is 0
        
        else:
            self.lockforticks -= 1

