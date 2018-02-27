class Calculator:
    data1 = 0
    data2 = 0
    result = 0

    def setData(self, data1, data2):
        self.data1 = data1
        self.data2 = data2
        return (self.data1, self.data2)

    def Plus(self):
        self.result = self.data1 + self.data2
        return "result: %d" % self.result

    def Minus(self):
        self.result = self.data1 - self.data2
        return "result: %d" % self.result

    def Multiply(self):
        self.result = self.data1 * self.data2
        return "result: %d" % self.result

    def Divide(self):
        self.result = self.data1 / self.data2
        return "result: %d" % self.result




