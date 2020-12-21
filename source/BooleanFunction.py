import BinaryFunctions



class BooleanFunction:




    def __deriveMinterms(self, inputs, results):
        if 2 ** (self.inputs) == inputs.length():
            if inputs.length() == results.length():
                self.__deriveMintermsFromFullTable(results)
            else:
                raise Exception
        else:
            self.__deriveMintermsFromHalfTable(inputs, results)


    def __deriveMintermsFromHalfTable(self, inputs, results):
        pass

    def __deriveMintermsFromFullTable(self, results):
        self.minterms = []
        self.dont_cares = []  # these can be both 0 and a 1, putting this on a separate list fixes some things
        for i in range(0, results.length()): 
            if results[i] == '1':
                self.minterms.append(i)
            elif results[i] == 'x': 
                self.dont_cares.append(i)
        

    def __init__(self, inputVars, inputs, results, outputName : str): 
        if inputVars.length() != results.length():
            raise Exception
        self.name = outputName
        self.inputs = []
        for element in inputVars:
            self.inputs.append(element)
    

    def produceBooleanFunction(self):
        pass

    def produceSimplifiedBooleanFunction(self):
        pass