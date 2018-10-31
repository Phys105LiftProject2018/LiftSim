class TickTimer(object):
    """
    Holds the tick state of the simulation as well as static methods for conversion between ticks and simulated time.

    Static Methods:
        Initialise
        GetCurrentTick
        GetCurrentTime
        GetTotalTicks
        GetSecondsPerTick
        IncrementTick
        GetTicks
        GetTime
        GetMilliseconds
        GetSeconds
        GetMinutes
        GetHours
        GetDays
    """
    __currentTick = None
    __totalTicks = None
    __secondsPerTick = None

    @staticmethod
    def Initialise(totalTicks, secondsPerTick):
        """
        Initialises the current tick, total tick and seconds per tick values.

        Paramiters:
            int totalTicks - The total number of ticks being simulated.
            float secondsPerTick - The number of seconds in one simulated tick.
        """
        TickTimer.__currentTick = 0
        TickTimer.__totalTicks = totalTicks
        TickTimer.__secondsPerTick = secondsPerTick

    @staticmethod
    def GetCurrentTick():
        """
        Retreives the current tick.

        Returns - int
        """
        return TickTimer.__currentTick

    @staticmethod
    def GetCurrentTime():
        """
        Retreives the current number of simulated seconds.

        Returns - float
        """
        return TickTimer.GetSeconds(TickTimer.__currentTick) 

    @staticmethod
    def GetTotalTicks():
        """
        Retreives the total number of ticks being simulated.

        Returns - int
        """
        return TickTimer.__totalTicks

    @staticmethod
    def GetSecondsPerTick():
        """
        Retreives the number of seconds in one simulated tick.

        Returns - float
        """
        return TickTimer.__secondsPerTick

    @staticmethod
    def IncrementTick(ammount = 1):
        """
        Increments the current tick by the specified ammount (1 by deafult).

        Paramiters:
            int ammount - the number of ticks to increce the current tick value by (deafult is 1).
        """
        TickTimer.__currentTick += ammount

    @staticmethod
    def GetTicks(seconds, flaw = False):
        """
        Converts a number of seconds into an equivilant number of ticks.

        Paramiters:
            float seconds - the number of seconds to be converted.
            boolean flaw - Suppress the ValueError produced by a result of a non-whole number of ticks and flaw the result (False by deafult).

        Returns - int
        """
        result = seconds / TickTimer.__secondsPerTick

        if flaw == False and result != float(int(result)):
            raise ValueError("The number of seconds supplied didn't corispond to an exact tick and automatic flawing of the result wasn't requested.")

        return int(result)

    @staticmethod
    def GetTime(ticks, unit = TimeUnit.Seconds):
        """
        Converts a number of ticks into an equivilant ammount of time.

        Paramiters:
            int ticks - the number of ticks to be converted.
            TimeUnit unit - The unit of time in which the result will be returned (deafult is TimeUnit.Seconds).

        Returns - float
        """
        if unit == TimeUnit.Milliseconds:
            result = TimeUnit.GetMilliseconds(ticks)
        elif unit == TimeUnit.Seconds:
            result = TimeUnit.GetSeconds(ticks)
        elif unit == TimeUnit.Minutes:
            result = TimeUnit.GetMinutes(ticks)
        elif unit == TimeUnit.Hours:
            result = TimeUnit.GetHours(ticks)
        elif unit == TimeUnit.Days:
            result = TimeUnit.GetDays(ticks)

        return result

    @staticmethod
    def GetMilliseconds(ticks):
        """
        Converts a number of ticks into an equivilant ammount of milliseconds.

        Paramiters:
            int ticks - the number of ticks to be converted.

        Returns - float
        """
        return ticks * TickTimer.__secondsPerTick * 1000

    @staticmethod
    def GetSeconds(ticks):
        """
        Converts a number of ticks into an equivilant ammount of seconds.

        Paramiters:
            int ticks - the number of ticks to be converted.

        Returns - float
        """
        return ticks * TickTimer.__secondsPerTick

    @staticmethod
    def GetMinutes(ticks):
        """
        Converts a number of ticks into an equivilant ammount of minutes.

        Paramiters:
            int ticks - the number of ticks to be converted.

        Returns - float
        """
        return ticks * TickTimer.__secondsPerTick / 60

    @staticmethod
    def GetHours(ticks):
        """
        Converts a number of ticks into an equivilant ammount of hours.

        Paramiters:
            int ticks - the number of ticks to be converted.

        Returns - float
        """
        return ticks * TickTimer.__secondsPerTick / 3600

    @staticmethod
    def GetDays(ticks):
        """
        Converts a number of ticks into an equivilant ammount of days.

        Paramiters:
            int ticks - the number of ticks to be converted.

        Returns - float
        """
        return ticks * TickTimer.__secondsPerTick / 86400

    class TimeUnit(Enum):
        """
        An enumaration containing a set of units of time.
        """
        Milliseconds = 0
        Seconds = 1
        Minutes = 2
        Hours = 3
        Days = 4