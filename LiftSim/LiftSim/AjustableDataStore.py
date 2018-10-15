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
        An enumaration containing the legal usage types for an AjustableDataStore object.
        """
        List = 0
        Stack = 1
        Queue = 2
        #RRQueue = 3
    

    
#-  Constructor
    def __init__(self, usageType, dataType, size = None, dynamic = True, minSize = None, maxSize = None):
        #TODO: Add errors
        if usageType in UsageMethods:
            self.UsageType = usageType
        else:
            pass# Throw error (wrong type or not in enum)

        self.ContenceType = usageType

        if size.getType() == int and (size > 0 and dynamic == False or size >= 0 dynamic == True):
            self.Size = size
            self.Dynamic = dynamic
        else:
            pass# Throw error (???)

        if minSize != None:
            if minSize.getType() == int and minSize >= 0:
                self.MinimumSize = minSize

                if maxSize.getType() == int and maxSize >= minSize:
                    self.MaximumSize = maxSize
                else:
                    pass# Throw error (input must be int and more than minSize)
            else:
                pass# Throw error (input must be int and +ve)

        self.__data = []



#-  Methods
    def Push(self, item):
        """
        Add items to the structure using the predifined method.
        """
        if self.UsageType == UsageMethods.List:
            pass

        elif self.UsageType == UsageMethods.Stack:
            pass

        elif self.UsageType == UsageMethods.Queue:
            pass

    def PushMany(self, items):
        """
        Add many items to the structure using the predifined method.
        """
        if self.UsageType == UsageMethods.List:
            pass

        elif self.UsageType == UsageMethods.Stack:
            pass

        elif self.UsageType == UsageMethods.Queue:
            pass

    def Pop(self):
        """
        Remove items from the structure using the predifined method.

        Returns: A single data element of the contained data type.
        """
        if self.UsageType == UsageMethods.List:
            pass

        elif self.UsageType == UsageMethods.Stack:
            pass

        elif self.UsageType == UsageMethods.Queue:
            pass

    def PopMany(self):
        """
        Remove many items from the structure using the predifined method.

        Returns: List of data elements of the contained data type.
        """
        if self.UsageType == UsageMethods.List:
            pass

        elif self.UsageType == UsageMethods.Stack:
            pass

        elif self.UsageType == UsageMethods.Queue:
            pass

    #TODO: add [] syntax and overide "x in var"



#-  Static Methods
    #def StaticMethod():
    #    pass