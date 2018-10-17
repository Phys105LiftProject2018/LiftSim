# Imports
from CustomExeptions import *
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
        if usageType in UsageMethods:
            # If the argument provided is valid, store the value.
            self.UsageType = usageType
        else:
            # If the argument provided is invalid, raise an exeption.
            raise ArgumentExeption("The argument provided for \"usageType\" was invalid. In must be a valid item from the AjustableDataStore.UsageMethods enumeration.")

        self.ContenceType = usageType

        if size.getType() == int and (size > 0 and dynamic == False or size >= 0 and dynamic == True) or size == None:
            # If the arguments provided is valid, store the values.
            self.Size = size
            self.Dynamic = dynamic
        else:
            # If the arguments provided are invalid, raise an exeption.
            pass#TODO: throw error(s)

        if minSize != None:
            # Do this if an argument is provided for the minSize paramiter.
            if minSize.getType() == int and minSize >= 0:
                # If the argument provided is valid, store the value.
                self.MinimumSize = minSize

                if maxSize.getType() == int and maxSize >= minSize or maxSize == None:
                    # If the argument provided is valid, store the value.
                    self.MaximumSize = maxSize
                else:
                    # If the argument provided is invalid, raise an exeption.
                    raise ArgumentExeption("The argument provided for \"maxSize\" was invalid. In must be of type \"int\" and greater in value than the \"minSize\" argument.")
            else:
                # If the argument provided is invalid, raise an exeption.
                raise ArgumentExeption("The argument provided for \"minSize\" was invalid. In must be of type \"int\" and its value must be positive.")

        self.__data = []



#-  Methods
    def Push(self, item):
        """
        Add items to the structure using the predifined method.
        """
        if self.UsageType == UsageMethods.List:
            self.__data.append(item)

        elif self.UsageType == UsageMethods.Stack:
            self.__data.append(item)

        elif self.UsageType == UsageMethods.Queue:
            raise NotImplementedError()#TODO:

    def PushMany(self, items):
        """
        Add many items to the structure using the predifined method.
        """
        #TODO: check data type of item in items

        for item in items:
            self.Push(item)

    def Pop(self):
        """
        Remove items from the structure using the predifined method.

        Returns: A single data element of the contained data type.
        """
        if self.UsageType == UsageMethods.List:
            raise InvalidOperationException("This operation can't be done using the \"List\" usage method.")

        elif self.UsageType == UsageMethods.Stack:
            return self.__data.pop(len(self.__data) - 1)

        elif self.UsageType == UsageMethods.Queue:
            raise NotImplementedError()#TODO:

    def PopMany(self, total):
        """
        Remove many items from the structure using the predifined method.

        Returns: List of data elements of the contained data type.
        """
        #TODO: check data type of total

        items = []
        for i in range(total):
            items.append(self.Pop())

        return items

    #TODO: add [] syntax and overide "x in var"



#-  Static Methods
    #def StaticMethod():
    #    pass