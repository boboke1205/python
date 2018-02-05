# coding=utf-8
class PointBoke:
    point = 3000

    ##포인트라는 변수가 필요하고, 이 포인트들을 주거니 받거니, 충전이 가능해야해

    def __init__(self, point, name):
        self.point = point
        self.name = name

    def use(self, minusPoint):
        self.point = self.point - minusPoint

    def charge(self, plusPoint):
        self.point = self.point + plusPoint

    def discount(self, price):
        self.point = self.point - price * 0.3

    def checkPoint(self):
        return "%s 의 포인트는 %d 입니다 " % (self.name, self.point)

    def sendPoint(self, someone, sendPoint):
        if someone.name == "Jungwoon":
            self.point = self.point - sendPoint
            someone.point = self.point + sendPoint
        else:
            print "포인트 전송에 실패했습니다. 다시 처음부터 시작해주세요"


boke = PointBoke(3000, "boke")
boke.use(1000)
print boke.checkPoint()
boke.charge(100000)
print boke.checkPoint()
boke.discount(10000)
print boke.checkPoint()


Jungwoon = PointBoke(3000, "Jungwoon")
Jungwoon.use(1000)
print Jungwoon.checkPoint()


boke.sendPoint(Jungwoon, 3000)
print boke.checkPoint()
