


class TwoInputOperator:
    
    def __init__(self, value1, value2):
        self.val1_is_nested = isinstance(value1, TwoInputOperator)
        self.val2_is_nested = isinstance(value2, TwoInputOperator)
        if self.val1_is_nested:
            self.value1 = value1.copy()
        if self.val2_is_nested:
            self.value2 = value2.copy()


    def copy(self):
        val1 = self.value1
        val2 = self.value2
        if self.val1_is_nested:
            val1 = self.value1.copy()
        if self.val2_is_nested:
            val1 = self.value2.copy()
        return TwoInputOperator(val1, val2)
    
    def toString(self):
        pass
    
    def toVHDL(self):
        pass