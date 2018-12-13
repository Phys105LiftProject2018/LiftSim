from CustomDataTypes import TickTimer
from uuid import uuid4 as GenID
import numpy as np


class Logger():
    SimulationBatchID = None
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
        Logger.recordedJourneyTicks[simId].append([person.departTick,journeyTicks,person.origin,person.destination])

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
    def getSimMeans():
        simMeans = []
        for sim in Logger.recordedJourneyTicks:
            
            mean = np.mean(sim,axis=0)
            simMeans.append(mean[1])

        return simMeans

    @staticmethod
    def LogLiftPosition(simId, id, currentLocation, targetLocation = None, currentTick = None):
        """
        Logs the current position of the lift.

        Paramiters:
            int simId - the id of th simulation the lift belongs to
            int id - the lift's id
            int currentLocation - the floor number of the floor where the lift currently is
            int targetLocation - the intended target of the lift (if applicable, None if not and by deafult)
            int currentTick - the current tick to be logged. Deafult is None which reads the tick from the TickTimer
        """

        if currentTick == None:
            currentTick = TickTimer.GetCurrentTick()

        liftID = 0

        Logger.LiftPosition[simId].append([currentTick, liftID, currentLocation, targetLocation])