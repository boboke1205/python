class Calculator:

    data1 = 0
    data2 = 0

    def setter(self,data1, data2):
        self.data1 = data1
        self.data2 = data2

    def plus(self):
        return self.data1 + self.data2

    def minus(self):
        return self.data1 - self.data2

    def multiply(self):
        return self.data1 * self.data2

    def divide(self):
        if self.data2 == 0:
            return -1
        else:
            return self.data1 / self.data2


