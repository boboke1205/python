# coding=utf-8
class Barista:
    orderList = []
    totalSales = 0
    menu = {'Americano': 3000, 'Caffe Latte': 4000, 'Green Tea': 4000}

    def showMenu(self):
        return self.menu

    def makeAndServe(self):
        if not self.orderList:
            print '주문 메뉴가 없습니다'
        else:
            print '%s가 준비 되었습니다.' % self.orderList[0]
            self.addSales()
            self.orderList.remove(self.orderList[0])

    def addSales(self):
        self.totalSales = self.totalSales + self.menu[self.orderList[0]]

    def addOrderList(self, order):   #궁금한 사항 _ 여기서 order 를 비즈니스 로직에서 입력하는 것인지
        if order in self.menu:
            self.orderList.append(order)
            self.makeAndServe()
        else:
            print "죄송합니다 해당 메뉴가 없습니다"

    def checkSales(self):
        return self.totalSales()

    def checkOrderList(self):
        if not self.orderList:
            return '주문 메뉴가 없습니다'
        else:
            return self.orderList
