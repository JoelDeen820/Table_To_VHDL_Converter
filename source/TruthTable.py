import csv


class Circuit:

    def __init__(self, fileName):
        file = open(filename, "r")
        tempTuple = csv.reader(file)
        self.table = (list)tempTuple
        for row in self.table:

    def __processHeader(self):
        self.header = self.table.pop(0)
        self.inputVars = []
        self.outputVars = []
        i = 0
        while self.header[i] != ' ' and i != self.header.length():
            self.inputVars.append(self.header[i])
            i += 1