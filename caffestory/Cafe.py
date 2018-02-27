# coding=utf-8
# 인스턴스 생성
from Barista import Barista
from Customer import Customer

boboke = Barista()
jungwoon = Customer()


print boboke.showMenu()
boboke.makeAndServe()
jungwoon.order('Americano2', boboke)
jungwoon.order('Caffe Latte', boboke)
jungwoon.order('Americano', boboke)
jungwoon.order('Americano', boboke)
jungwoon.order('Americano', boboke)
print boboke.totalSales