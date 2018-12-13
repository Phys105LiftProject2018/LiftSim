class Person:
    """
    Represents a person in the simulation

    Paramiters:
        int destination - the floor number of the person's intended destination
        int origin - the floor number the person calls the lift from
        int departTick - the tick on which the person calls the lift
    """

    def __init__(self, destination, origin, departTick):
        self.destination = destination
        self.origin = origin
        self.departTick = departTick
       

