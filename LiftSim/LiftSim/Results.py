"""
The main file in the project. The simulation is run and controlled from this file.
If not running from a command prompt, change the value of the "settingsFilePath" variable below to access different data directories.
"""

import os
directoryPath = os.path.abspath("./OliverLodge/OliverLodge")# Include the name of the file in the path but not the ".properties" extention!

# External Imports
import numpy as np
from matplotlib import pyplot as plt

# Project Import
from CustomDataTypes import *
from CustomExeptions import *
from GraphingClassFile import GraphingClass



# Read filepath from console arguments
import sys
if len(sys.argv) > 1:
    if os.path.isfile(os.path.abspath(sys.argv[1]) + ".properties"):
        directoryPath = sys.argv[1]

    else:
        raise NoPathExistsException(sys.argv[1] + ".properties")

print("Using data from directory: \"{}\"".format(os.path.abspath(os.path.split(directoryPath)[0])))

#-  




#-  Load logs and graph data
DirectoryManager.Initialise(directoryPath)

data, times, positions, properties = DirectoryManager.ReadLogs()



#-  Initialise classes reliant on data
TickTimer.Initialise(properties.TotalTicks, properties.SecondsPerTick)



#- Output the raw data from the properties file
print("Results:")
for index, item in enumerate(data):
    if index == 0:
        print("    Batch ID = " + str(item))
    else:
        print("    " + DirectoryManager.batchDataProperties[index - 1][:-1].replace("_", " ").capitalize() + " = " + str(item))



#-  Output graphs
GraphingClass.Distribution([record[1] for record in times])

GraphingClass.graphData([int(record[0]) for record in positions if record[1] == 0], [float(record[2]) for record in positions if record[1] == 0], "Sim 1")#tick, lift, current, dest.

GraphingClass.waitingTimeBarChart([record[0:2] for record in times], TickTimer.TimeUnit.Hours, bottomOffsetFromMin = 5)#tick, time, start, dest.