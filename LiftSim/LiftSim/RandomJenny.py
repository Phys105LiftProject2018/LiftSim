import random
import numpy as np

class RandomJenny:
    @staticmethod
    def chooseDestination(origin):
        #Currently hardcoded but can be read from CSV, also then can be time dependent
        probabilities = [1,0.3,0.3,0.3,0.3]
        # current floor has zero probability
        probabilities[origin] = 0.0
        sumProbs = sum(probabilities)
        # Normalise from 0-1, so they all add to one.
        normalisedProbs = [float(i)/sumProbs for i in probabilities]
        # Perform a cumulative sum on the list so it starts at 0 and ends at 1
        cumSumProbs = np.cumsum(normalisedProbs)
        # Generate float from 0-1
        randno = random.uniform(0,1)
        # Test which item this is equivalent to and return the floor number
        for floor,prob in enumerate(cumSumProbs):
            if randno <= prob:
                #This has been chosen by the generator, return index of current item in list
                #Current index is given by 'floor', if this is unclear, look up enumerate() :)
                return floor
        # No item was selected so raise an error
        raise RuntimeError



