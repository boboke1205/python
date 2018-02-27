# coding=utf-8

class Barista:
    orderList = []
    totalSales = 0
    menu = {"Americano" : 3000, "Caffe Latte": 4000, "Green Tea" : 4000}

    def showMenu(self):
        return self.menu

    def makeAndServe(self):
        if not self.orderList:
            print "주문 메뉴가 없습니다. "
        else:
            print "%s가 준비되었습니다 " % self.orderList[0]
            self.addSales()
            self.orderList.remove(self.orderList[0])

    def addSales(self):
        self.totalSales = self.totalSales + self.menu[self.orderList[0]]


    def addOrderList(self, order):
        if order in self.menu:
            self.orderList.append(order)
            self.makeAndServe()
        else:
            print "죄송합니다 해당 매뉴가 없습니다. "

    def checkSales(self):
        return self.totalSales()

    def checkOrderList(self):
        if not self.orderList:
            return "주문메뉴가 없습니다."
        else:
            return self.orderList
