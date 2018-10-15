# Imports
from enum import Enum
import numpy

class AjustableDataStore(object):
    """
    AjustableDataStore:
        A data store that can provide data sequentionaly or randomly and can change the method used to provide data.

        "AjustableDataStore(UsageMethods.List, int)" will produce a dynamic list of integers.

        __init__(list, of, paramiters):
            AjustableDataStore.UsageMethods usageType - The starting type of data structure.
            type dataType - The data type of the contentse.
            integer size - The starting size for the data structure. Deafult is None to allow for fully dynamic sizes.
            boolean dynamic - Can the data structure change length (True by deafult). False for a fixed size.
            integer minSize - The smallest legal size for the data structure. Deafult is None to allow for fully dynamic sizes.
            integer maxSize - The largest legal size for the data structure. Deafult is None to allow for fully dynamic sizes.

        Public Atributes:
            dataType Atribute1 - Description

            AjustableDataStore.UsageMethods UsageType
            type ContenceType
            integer Size
            boolean Dynamic
            integer MinimumSize
            integer MaximumSize

        Static Atributes:
            class UsageMethods - An enumaration containing the legal usage types for an AjustableDataStore object.
    """

#-  Static Atributes
    class UsageMethods(Enum):
        """
        """
        List = 0
        Stack = 1
        Queue = 2
        #RRQueue = 3
    

    
#-  Constructor
    def __init__(self, usageType, dataType, size = None, dynamic = True, minSize = None, maxSize = None):
        self.UsageType = usageType#TODO: Validation
        self.ContenceType = usageType
        self.Size = size
        self.Dynamic = dynamic
        self.MinimumSize = minSize
        self.MaximumSize = maxSize

        self.__data = []



#-  Methods
    def Push(self):
        """
        """
        pass

    def PushMany(self):
        """
        """
        pass

    def Pop(self):
        """
        """
        pass

    def PopMany(self):
        """
        """
        pass

    #TODO: add [] syntax and overide "x in var"



#-  Static Methods
    #def StaticMethod():
    #    pass