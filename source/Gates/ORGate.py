from Gates.TwoInputOperator import TwoInputOperator

class ORGate(TwoInputOperator):

    def toVHDL(self):
        return "(" + value1.toVHDL() + " or " + value2.toVHDL() + ")"