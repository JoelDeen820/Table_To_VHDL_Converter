

class SingleInputGate:

    def __init__(self, value1): 
        self.value1 = value1.copy()
    
    def copy(self):
        return SingleInputGate(self.value1.copy())
    
    def toVHDL(self):
        pass