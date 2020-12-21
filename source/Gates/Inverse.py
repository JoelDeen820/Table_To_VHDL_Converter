from Gates import *

class Inverse(SingleInputGate):

    def toVHDL(self):
        return "( not " + value1.toVHDL() + " )"
