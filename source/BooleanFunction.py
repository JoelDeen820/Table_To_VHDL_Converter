from source.Gates.Variable import Variable
from source.Gates.ANDGate import ANDGate
from source.Gates.Inverse import Inverse
from source.Gates.ORGate import ORGate


# from Gates.Variable import Variable
# from Gates.ANDGate import ANDGate
# from Gates.Inverse import Inverse

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
        if inputVars.length() != results.len():
            raise Exception
        self.name = outputName
        self.inputs = []
        for element in inputVars:
            self.inputs.append(element)
    
    def __deriveFunctionFromInt(self, intValue):
        variableNames = self.inputs.copy()
        variableNames.reverse() # done as this algorithm adds items from right to left, not left to right
        i = 0
        resultant_value = None
        processed_value = Variable(variableNames[0])
        if (intValue % 2) == 0:
            resultant_value = Inverse(processed_value)
        else :
            resultant_value = processed_value
        intValue //= 2
        i += 1
        while ( intValue // 2 ) != 0 :
            processed_value = Variable(variableNames[i])
            if (intValue % 2) == 0 :
                resultant_value = ANDGate(resultant_value, Inverse(processed_value))
            else:
                resultant_value = ANDGate(resultant_value, processed_value)
            intValue // 2
            i += 1
        return processed_value.copy()


    def produceBooleanFunction(self):
        resultant_boolean_function = None
        minterm_list = []
        for minterm in self.minterms:
            minterm_list.append(self.__deriveFunctionFromInt(minterm))
        if len(minterm_list) > 1:
            resultant_boolean_function = ORGate(minterm_list[1], minterm_list[0])
            for i in range(2, len(minterm_list)):
                resultant_boolean_function = ORGate(resultant_boolean_function, minterm_list[i])
        elif len(minterm_list) == 1:
            resultant_boolean_function = minterm[0]
        else:
            return None

    def produceSimplifiedBooleanFunction(self):
        pass