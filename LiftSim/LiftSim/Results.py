"""
The main file in the project. The simulation is run and controlled from this file.
If not running from a command prompt, change the value of the "settingsFilePath" variable below to access different data directories.
"""

directoryPath = "./OliverLodge/OliverLodge"# Include the name of the file in the path but not the ".properties" extention!

# External Imports
import numpy as np
from matplotlib import pyplot as plt
import os

# Project Import
from CustomDataTypes import *
from CustomExeptions import *
from GraphingClassFile import GraphingClass



# Read filepath from console arguments
import sys
if len(sys.argv) > 1:
    if os.path.isfile(sys.argv[1] + ".properties"):
        directoryPath = sys.argv[1]

    else:
        raise NoPathExistsException(sys.argv[1] + ".properties")

print("Using data from directory: \"{}\"".format(os.path.abspath(os.path.split(directoryPath)[0])))


#-  Load logs and graph data
DirectoryManager.Initialise(directoryPath)
data = DirectoryManager.ReadLogs()
GraphingClass.graphData(data[1], "Sim 1")
GraphingClass.waitingTimeBarChart(data[0])