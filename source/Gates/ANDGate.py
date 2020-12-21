from Gates.TwoInputOperator import TwoInputOperator

class ANDGate(TwoInputOperator):

    gateType = "AND"

    def toVHDL(self):
        return "(" + value1.toVHDL() + " and " + value2.toVHDL() + ")"
    