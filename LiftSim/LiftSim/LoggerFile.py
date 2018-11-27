from CustomDataTypes import TickTimer
from uuid import uuid4 as GenID


class Logger():
    SimulationBatchID = None
    #DirectoryRoot = None
    recordedJourneyTicks = []
    LiftPosition = []
    idCounter = 0

    @staticmethod
    def Initialise(numSims,directoryRootPath):
        """
        Initialise the static variables in the Logger class.

        Paramiters:
            string directoryRootPath - The filepath of the root directory for the current directory.
        """
        DirectoryRoot = directoryRootPath
        SimulationBatchID = GenID().hex

        for i in range(numSims):
            Logger.recordedJourneyTicks.append([])
            Logger.LiftPosition.append([])

    @staticmethod
    def recordJourney(simId, person, arrivalTick = TickTimer.GetCurrentTick()):
        '''
        Adds a persons journey length to the log.

        Parameters:
        Person Object
        arrivalTick, defaults to current tick but can be supplied
        '''
        journeyTicks = arrivalTick - person.departTick
        Logger.recordedJourneyTicks[simId].append([person.origin, person.destination, person.departTick,journeyTicks])

    @staticmethod
    def getJourneySeconds():
        array = []
        for sim in Logger.recordedJourneyTicks:
            times = []
            for ticks in sim:
                times.append(TickTimer.GetSeconds(ticks))
            array.append(times)
        return array

    @staticmethod
    def LogLiftPosition(simId,id, currentLocation, targetLocation, currentTick = None):
        if currentTick == None:
            currentTick = TickTimer.GetCurrentTick()
        liftID = 0
        Logger.LiftPosition[simId].append([currentTick, liftID, currentLocation, targetLocation])
    
    #@staticmethod
    #def SaveLogs():
    #    """
    #    RootDirectory\Logs\Batch_[uuid]\Simulation_[sim index]\
    #                                                          \simulation logs here
    #    				  			   \general logs here e.g. outcome, date, etc.
    #                      \latest batch in txt file
    #    """
    #    pass# Write to the directory
      
