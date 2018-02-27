# coding=utf-8

class Barista:
    order = 0
    orderList = []
    totalSales = 0
    Menu = {"Americano": 3000, "Caffe Latte": 4000, "Green Tea": 4000}

    def showMenu(self):
        print "안녕하세요? 무엇을 주문 하시겠습니까?"
        while (True):
            print "Americano"
            print "Caffe Latte"
            print "Green Tea"

    def makeAndServe(self):
        print " %s 가 준비되었습니다. 맛있게 드세요" % self.order
        self.orderList.remove(self.order)

    def checkOrderlist(self):
        return "현재 주문은 %s 입니다 " % self.orderList

    def checkSales(self):
        return "매출 현황 : %s " % self.totalSales


class Customer:
    def order(self, barista):
        print barista.checkSales()

        # order = input("메뉴를 선택하세요 :")
        #
        # if order == "Americano":
        #     self.orderList.append(order)
        #     self.totalSales = self.totalSales + self.Menu["Americano"]
        #     continue
        #
        # elif order == "Caffe Latte":
        #     self.orderList.append(order)
        #     self.totalSales = self.totalSales + Menu["Caffe Latte"]
        #     continue
        #
        # elif order == "Green Tea":
        #     self.orderList.append(order)
        #     self.totalSales = self.totalSales + Menu["Green Tea"]
        #     continue
        #
        # else:
        #     print "죄송해요 그건 못만들어요"
        #     continue

boke = Barista()
# boke.showMenu()

Jungwoon = Customer()
Jungwoon.order(boke)






    # ##포인트라는 변수가 필요하고, 이 포인트들을 주거니 받거니, 충전이 가능해야해
    #
    # def __init__(self, point, name):
    #     self.point = point
    #     self.name = name
    #
    # def use(self, minusPoint):
    #     self.point = self.point - minusPoint
    #
    # def charge(self, plusPoint):
    #     self.point = self.point + plusPoint
    #
    # def discount(self, price):
    #     self.point = self.point - price * 0.3

#
# boke = Barista(3000, "boke")
# boke.use(1000)
# print boke.checkPoint()
# boke.charge(100000)
# print boke.checkPoint()
# boke.discount(10000)
# print boke.checkPoint()
#
#
# Jungwoon = Barista(3000, "Jungwoon")
# Jungwoon.use(1000)
# print Jungwoon.checkPoint()
#
#
# boke.sendPoint(Jungwoon, 3000)
# print boke.checkPoint()
