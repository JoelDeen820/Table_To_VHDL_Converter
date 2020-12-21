
class Variable:  # yes, this is a glorified sting

    def __init__(self, var_name):
        self.name = var_name
    
    def copy(self):
        return self.name
    
    def toVHDL(self):
        return self.name