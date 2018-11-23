import numpy as np

class Trader(object):

    def __init__(self):
        raise NotImplementedError()

    def predict(self,historyDict):

        prediction = (1 / historyDict['numStocks']) * np.ones([historyDict['numStocks']],dtype=np.float32)

        return prediction


