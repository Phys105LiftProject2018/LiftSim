import matplotlib.pyplot as plt
import numpy as np
import pandas as pand
from CustomDataTypes import *

class GraphingClass(object):
    """
    """

    @staticmethod
    def averageWaitingTimes(waitingTimes, interval = TickTimer.TimeUnit.Hours):
        waitingTimes.sort(key = lambda item: item[0], reverse = False)

        start_time = int(TickTimer.GetTime(waitingTimes[0][0], interval))
        stop_time = int(TickTimer.GetTime(waitingTimes[-1][0], interval))

        timeIntervals = np.linspace(start_time, stop_time, stop_time - start_time + 1, dtype = int).tolist()


        averageTimes = []# average waiting time for each interval
        for i in range(len(timeIntervals)):
            averageTimes.append([0, 0])

        for record in waitingTimes:
            index = timeIntervals.index(int(TickTimer.GetTime(record[0], interval)))
            averageTimes[index][0] += record[1]
            averageTimes[index][1] += 1

        averageTimes = [(item[0] / item[1] if item[1] != 0 else 0) for item in averageTimes]

        return [averageTimes, timeIntervals]

    @staticmethod
    def waitingTimeBarChart(waiting_times, interval = TickTimer.TimeUnit.Hours, bottomOffsetFromMin = None):
        """

        Paramiters:
            int bottomOffsetFromMin - number of seconds to be subtracted from the minimum avarage to set the starting y-axix value (deafult = None: starts at 0, recomended = 5)
        """
        #waiting_times.sort(key = lambda item: item[0], reverse = False)

        #start_time = int(TickTimer.GetTime(waiting_times[0][0], interval))
        #stop_time = int(TickTimer.GetTime(waiting_times[-1][0], interval))

        #timeIntervals = np.linspace(start_time, stop_time, stop_time - start_time + 1, dtype = int).tolist()


        #averageTimes = []# average waiting time for each interval
        #for i in range(len(timeIntervals)):
        #    averageTimes.append([0, 0])

        #for record in waiting_times:
        #    index = timeIntervals.index(int(TickTimer.GetTime(record[0], interval)))
        #    averageTimes[index][0] += record[1]
        #    averageTimes[index][1] += 1

        #averageTimes = [(item[0] / item[1] if item[1] != 0 else 0) for item in averageTimes]

        averageTimes, timeIntervals = GraphingClass.averageWaitingTimes(waiting_times, interval)

        timeOfDayIntervals = [TickTimer.GetTimeOfDay(tick, interval) for tick in [TickTimer.GetTicks(hour * 3600) for hour in timeIntervals]]
        
        barList = np.arange(len(timeIntervals))# Generates list of bar numbers (0?, 1, 2, 3, ect...)
        plt.bar(barList, averageTimes, align='center', alpha=0.5)
        plt.xticks(barList, timeOfDayIntervals)# Lables for the bars
        plt.ylabel('Seconds')
        plt.xlabel('Time of Day')
        plt.title('Average Waiting Times')
        smallestNonZeroTime = min([time for time in averageTimes if time != 0])
        if bottomOffsetFromMin == None:
            bottomOffsetFromMin = smallestNonZeroTime
        plt.ylim(bottom = smallestNonZeroTime - bottomOffsetFromMin, top = plt.ylim()[1])
        plt.show()


    @staticmethod
    def Distribution(averageWait, num_bins = None):
        Changebin = 0
        #Change value of Num_bins for bin size (Default: None)
        #num_bins = 20
    
        if num_bins == None:
            num_bins = int(np.sqrt(len(averageWait))) + Changebin

        plt.ylabel('Frequency')
        plt.xlabel('Average Waiting Time (s)')
        plt.hist(averageWait, num_bins, facecolor='blue', alpha=0.5)
   
        plt.show()
    
    #AverageWait is just the array of waiting times

    #@staticmethod
    #def LiftLocation(Ticks,Floor,scenarioType):
    @staticmethod
    def LiftLocation(data, liftNumber, scenarioType, minFloor, maxFloor):
    #-  Access data
        Ticks = [int(record[0]) for record in data if record[1] == liftNumber]

        Floor = [int(record[2]) for record in data if record[1] == liftNumber]

        #targets = [int(record[3]) if record not None else None for record in data if record[1] == liftNumber]
        targets = [[int(record[0]), int(record[2]), int(record[3])] for record in data if record[1] == liftNumber and record[3] != None]



        #plt.plot(ticks,floor)

    #-  Initalising Variables
        NoOfFloors = maxFloor - minFloor + 1
        i = -1
        PreviousGradient = 0
    
        ArrowCorrector = NoOfFloors*0.025
        


        #Declaring Arrays
        #CallPositions = np.zeros((2,3))
        #CallPositions[0,0], CallPositions[1,0] = 4,3
        #CallPositions[0,1], CallPositions[1,1] = 6,5
        #annotationPositions = np.zeros((2,int(np.size(CallPositions,1))))
        
        

    #-  Graph Data
        fig = plt.figure()
        ax = plt.subplot(1, 1, 1)
        
        ax.set_title(scenarioType + " Lift Graph")# Set the title
        plt.xlabel('Ticks')# Set the x-axis label
        plt.ylabel('Floor')# Set the y-axis label
        plt.yticks(np.arange(minFloor, maxFloor + 1, 1, int))# Set the sacle for the y axis to integer floor numbers
        
        line, = plt.plot(Ticks, Floor, 'k')

        for record in targets:
            if record[2] != None:
                plt.annotate(str(record[2]), xy=(record[0] + 50, record[1]))



    #-  Plots points of interest on graph. Such as Gradient Change and Elevator Calls
        #for index in range(0, len(Ticks)-1):
        #        #dy/dx

        #        #Gradient Check
        #        Gradient = (Floor[index+1]-Floor[index])/(Ticks[index+1]-Ticks[index])
        #        if PreviousGradient < Gradient:
        #            plt.annotate(" ", xy=(Ticks[index],Floor[index]+ArrowCorrector),
        #                         xytext=(Ticks[index],Floor[index]+ArrowCorrector), 
        #                         arrowprops=dict(facecolor="green", shrink = 1),)    
        #        elif PreviousGradient > Gradient:
        #            if Gradient != 0:
        #                #Floor[index+2]
        #                #Floor[index+1]
        #                #Ticks[index+2]
        #                #Ticks[index+1]
        #                GradientCheck = (Floor[index+2]-Floor[index+1])/(Ticks[index+2]-Ticks[index+1])
        #                if GradientCheck != Gradient:
        #                    plt.annotate(" ", xy=(Ticks[index],Floor[index]-ArrowCorrector), 
        #                                 xytext=(Ticks[index],Floor[index]+ArrowCorrector), 
        #                                 arrowprops=dict(facecolor="Red", shrink = 1),)    
        #        PreviousGradient = Gradient



    #-  Loop for placing Elevator Calls
        #Corrector = NoOfFloors/5

        #Corrector = 0
        #for i in range(0, np.size(CallPositions, 1) - 1):

        #    plt.annotate(str(CallPositions[1,i]), xy=(Ticks[int(CallPositions[0,i])], Floor[int(CallPositions[0,i])]+Corrector))
        
        #    annotationPositions[0,i], annotationPositions[1,i] = Ticks[int(CallPositions[1,i])],Floor[int(CallPositions[0,i])]
        
        
        
            #for row in 
        
            #Make a check to see if part of the array is 
            #already in that position if it is then increase the height of that call by an amount
        
        #TODO: ask ty if these are needed
        #print("Annotation Positions", annotationPositions)
        #print("Call Positions", CallPositions)
        #print("Ticks",Ticks[int(CallPositions[1,i])],"Floors",Floor[int(CallPositions[0,i])])
        
        

        plt.show() 