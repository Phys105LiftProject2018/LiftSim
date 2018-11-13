#TODO: Chris to delete this file and contence!
import matplotlib.pyplot as plt
import numpy as np
import pandas as pand

def graphData(ticks,floor,scenarioType):
    #plt.plot(ticks,floor)

    #Initalising Variables
    NoOfFloors = 10 
    i = -1
    PreviousGradient = 0
    
    ArrowCorrector = NoOfFloors*0.025
    
    #Declaring Arrays
    CallPositions = np.zeros((2,3))
    CallPositions[0,0], CallPositions[1,0] = 4,3
    CallPositions[0,1], CallPositions[1,1] = 6,5
    annotationPositions = np.zeros((2,int(np.size(CallPositions,1))))
    
    
    #Graph Data
    fig = plt.figure()
    ax = plt.subplot(111)
    
    plt.xlabel('Ticks')
    plt.ylabel('Floor')
    ax.set_title(scenarioType + " Lift Graph")
    
    line, = plt.plot(Ticks,Floor, 'b')

    #Plots points of interest on graph
        #Such as Gradient Change and Elevator Calls
    for index in range(0, len(Ticks)-1):
            #dy/dx

            #Gradient Check
            Gradient = (Floor[index+1]-Floor[index])/(Ticks[index+1]-Ticks[index])
            if PreviousGradient < Gradient:
                plt.annotate(" ", xy=(Ticks[index],Floor[index]+ArrowCorrector),
                             xytext=(Ticks[index],Floor[index]+ArrowCorrector), 
                             arrowprops=dict(facecolor="green", shrink = 1),)    
            elif PreviousGradient > Gradient:
                if Gradient != 0:
                    GradientCheck = (Floor[index+2]-Floor[index+1])/(Ticks[index+2]-Ticks[index+1])
                    if GradientCheck != Gradient:
                        plt.annotate(" ", xy=(Ticks[index],Floor[index]-ArrowCorrector), 
                                     xytext=(Ticks[index],Floor[index]+ArrowCorrector), 
                                     arrowprops=dict(facecolor="Red", shrink = 1),)    
            PreviousGradient = Gradient


    #Loop for placing Elevator Calls
    #Corrector = NoOfFloors/5
    Corrector = 0
    for i in range(0, np.size(CallPositions,1)-1):

        plt.annotate(str(CallPositions[1,i]), 
        xy=(Ticks[int(CallPositions[0,i])],
        Floor[int(CallPositions[0,i])]+Corrector))
        
        annotationPositions[0,i], annotationPositions[1,i] = \
        Ticks[int(CallPositions[1,i])],Floor[int(CallPositions[0,i])]
        
        
        
        #for row in 
        
        #Make a check to see if part of the array is 
        #already in that position if it is then increase the height of that call by an amount
    
    print("Annotation Positions", annotationPositions)
    print("Call Positions", CallPositions)
    print("Ticks",Ticks[int(CallPositions[1,i])],"Floors",Floor[int(CallPositions[0,i])])
    
    
    plt.show()
   
    
def waitingTimeBarChart(timeWaiting):
    time = ('8', '9', '10', '11', '12', '13', '14','15','16','17','18')
    y_pos = np.arange(len(time))
    plt.bar(y_pos, timeWaiting, align='center', alpha=0.5)
    plt.xticks(y_pos, time)
    plt.ylabel('Minutes')
    plt.xlabel('Time of Day')
    plt.title('Average Waiting Times')
    plt.show()
    

#ticks = np.arange(0.0, 2.0, 0.01)
#floor = 1 + np.sin(2*np.pi*ticks)*12*np.cos(ticks)
ticks = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
floor = [2,3,4,5,5,5,6,7,8,8,8,8,8,7,7,7,7,6,5,4,4,3,3,3,3]
Scenario = "Best"

graphData(ticks,floor,Scenario)