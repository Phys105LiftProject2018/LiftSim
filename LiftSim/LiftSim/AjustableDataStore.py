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

    
    
#-  Constructor
    def __init__(self, usageType, dataType, size = 0, dynamic = True, minSize = None, maxSize = None):
        if usageType in UsageMethods:
            # If the argument provided is valid, store the value.
            self.UsageType = usageType
        else:
            # If the argument provided is invalid, raise an exeption.
            raise ArgumentExeption("The argument provided for \"usageType\" was invalid. In must be a valid item from the AjustableDataStore.UsageMethods enumeration.")

        self.ContenceType = dataType
        
        if type(size) == int and (size > 0 and dynamic == False or size >= 0 and dynamic == True) or size == None:
            # If the arguments provided is valid, store the values.
            self.Size = size
            self.Dynamic = dynamic
        else:
            # If the arguments provided are invalid, raise an exeption.
            pass#TODO: throw error(s)

        if minSize != None:
            # Do this if an argument is provided for the minSize paramiter.
            if type(minSize) == int and minSize >= 0:
                # If the argument provided is valid, store the value.
                self.MinimumSize = minSize

                if type(maxSize) == int and maxSize >= minSize or maxSize == None:
                    # If the argument provided is valid, store the value.
                    self.MaximumSize = maxSize
                else:
                    # If the argument provided is invalid, raise an exeption.
                    raise ArgumentExeption("The argument provided for \"maxSize\" was invalid. In must be of type \"int\" and greater in value than the \"minSize\" argument.")
            else:
                # If the argument provided is invalid, raise an exeption.
                raise ArgumentExeption("The argument provided for \"minSize\" was invalid. In must be of type \"int\" and its value must be positive.")

        else:
            self.MinimumSize = 0
            if self.Dynamic == True:
                self.MaximumSize = None
            else:
                self.MaximumSize = self.Size
            
        self.__data = list()
        for i in range(size):
            self.__data.append(None)

        if self.Size == 0:
            self.__front = None
            self.__back = None
        else:
            self.__front = 0
            self.__back = 0

        self.Count = 0

    @property
    def Full(self):
        return self.Count == self.Size and self.Dynamic == False

    @property
    def Empty(self):
        return self.Count == 0

    #temp
    def getData(self):
        return self.__data

#-  Methods
    def Push(self, item):
        """
        Add items to the structure using the predifined method.
        """
        # Check the data type of the item
        if type(item) != self.ContenceType:
            raise ArgumentExeption("The argument for the paramiter \"item\" must be of type " + str(self.ContenceType) + ", not of type " + str(type(item)))
        
        if not self.Full:
            if self.Count == 0:
                self.__front = 0
                self.__back = -1

            # Lists, Stacks and Queues
            if self.UsageType == UsageMethods.List or self.UsageType == UsageMethods.Stack or self.UsageType == UsageMethods.Queue:
                self.__back += 1
                if self.Dynamic:
                    if self.__back < self.Size:
                        self.__data[back] = item



                    if self.__back == self.Size:
                        self.__data.append(item)
                        self.__increceSize()
                            

                    
                else:
                    if self.__back == self.Size and self.Dynamic == False:# If the structure isn't but the index would be outside the avalable range for a static structure
                        self.__back = 0# Loop back to the front of the data list

                    self.__data[self.__back] = item

            self.Count += 1
        else:
            raise StructureFullException("The data structure is full. An item can't be added.")

    def PushMany(self, items):
        """
        Add many items to the structure using the predifined method.
        """
        for item in items:
            self.Push(item)

    def Pop(self):
        """
        Remove items from the structure using the predifined method.

        Returns: A single data element of the contained data type.
        """
        if not self.Empty:
            # Lists
            if self.UsageType == UsageMethods.List:
                raise InvalidOperationException("This operation can't be done using the \"List\" usage method.")# Make remove and shuffle back

            # Stacks
            elif self.UsageType == UsageMethods.Stack:
                data = self.__data[self.__back]
                self.__back -= 1

                if self.__back == -1:
                    self.__back = self.Count - 1

                returnData = data

            # Queues
            elif self.UsageType == UsageMethods.Queue:
                data = self.__data[self.__front]
                self.__data[self.__front] = "Removed!"
                #print(data)

                if self.Dynamic == False:
                    self.__front += 1

                    if self.__front == self.Size:# If the structure isn't but the index would be outside the avalable range for a static structure
                        self.__front = 0# Loop back to the front of the data list

                else:# Dynamic must be true
                    self.__data = self.__data[1: self.Count]
                    self.__back -= 1

                returnData = data
                #raise NotImplementedError()#TODO: make so if dynamic everything shuffles

            self.Count -= 1
            if self.Count == 0:
                self.__front = None
                self.__back = None

            self.__decreaseSize()

            return returnData

        else:
            raise StructureEmptyException("The data structure is empty. An item can't be removed.")

    def PopMany(self, total):
        """
        Remove many items from the structure using the predifined method.

        Returns: List of data elements of the contained data type.
        """
        if type(total) != int:
            raise ArgumentExeption("The argument for the paramiter \"total\" must be of type \"int\", not of type " + str(type(total)))

        items = []
        for i in range(total):
            items.append(self.Pop())

        return items

    def __setitem__(self, key, value):# Overloads "object[key] = value"
        self.__data[self.__RealIndex(key)] = value

    def __getitem__(self, key):# Overloads "object[key]"
        return self.__data[self.__RealIndex(key)]

    def __RealIndex(self, virtualIndex):
        """
        Provides the real index given the virtual index.
        """
        if virtualIndex > self.Count - 1:
            raise IndexError()

        real = virtualIndex + self.__front

        if real >= len(self.__data):
            real -= len(self.__data)

        return real

    def __VirtualIndex(self, realIndex):
        """
        Provides the virtual index given the real index.
        """
        if realIndex > self.Count - 1:
            raise IndexError()

        virtual = realIndex - self.__front

        if virtual < 0:
            virtual += len(self.__data)

        return virtual

    def __len__(self):# Overloads "len(object)"
        return self.Count

    def __contains__(self, value):# Overloads "value in object"
        return value in self.__data

    def __increceSize(self):
        if self.MaximumSize != None and self.Size == self.MaximumSize:
            raise SizeBoundryExcededException("This operation would excede the fixed upper size boundry of the structure. Please report this error.")
        self.Size += 1

    def __decreaseSize(self):
        if self.Size == self.MinimumSize:
            raise SizeBoundryExcededException("This operation would excede the fixed lower size boundry of the structure. Please report this error.")
        self.Size -= 1

    # Preps use as an itterable
    def __iter__(self):
        self.__iterCount = 0
        return self

    # Gives the next value in the active itteration
    def __next__(self):
        if self.__iterCount < self.Count:
            result = self.__data[self.__RealIndex(self.__iterCount)]
            self.__iterCount += 1
            return result
        else:
            raise StopIteration



#-  Static Methods
    #def StaticMethod():
    #    

class UsageMethods(Enum):
    """
    An enumaration containing the legal usage types for an AjustableDataStore object.
    """
    List = 0
    Stack = 1
    Queue = 2
    #RRQueue = 3

if __name__ == "__main__":
    test = AjustableDataStore(UsageMethods.Queue, int, 10, True, 0, 10)
    
    for i in range(10):
        test.Push(i)

        print("")
        print(test.getData())
        print(test.Count)
        print(test.Size)
        print(test.Empty)

    test.Pop()
    test.Push(11)

    print(test.getData())

    for item in test:
        print(item)

    test.UsageType = UsageMethods.Stack

    while test.Count > 0:
        print(test.Pop())

    print("")
    print(test.Count)
    print(test.Size)
    print(test.Empty)

    for item in test:
        print(item)