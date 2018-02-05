# coding=utf-8

from Calculator2 import Calculator

boke = Calculator()

while(True):
    print "1.imput Data"
    print "2.plus"
    print "3.minus"
    print "4.multiply"
    print "5.divide"
    selectMenu = input("메뉴를 선택하세요 :")

    if selectMenu == 1:
        data1 = input("data1 : ")
        data2 = input("data2 : ")
        boke.setter(data1, data2)
        continue

    elif selectMenu == 2:
        print boke.plus()
        continue

    elif selectMenu == 3:
        print boke.minus()
        continue

    elif selectMenu == 4:
        print boke.multiply()
        continue

    elif selectMenu == 5:
        print boke.divide()
        continue

    else:
        print "Sorry. We didn't made it"
        continue
