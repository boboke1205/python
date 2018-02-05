# coding=utf-8
def getAvg(a, b):
    return (a + b) / 2

print getAvg(3, 5)


print "---------------------------"
def getMaxmin(list):
    max = 0
    min = 9999999999

    for i in list:
        if i <= min:
            min = i

        if i >= max:
            max = i

    return (max, min)

print getMaxmin([3, 0, 3, 9, 948, 590, 4, 9, 22, 3503, 4, 5])



# print "---------------------------"
# def getBMI(yourWeight, height):
#     bmi = yourWeight / pow(height, 2)
#
#     if bmi < 18.5:
#         return "마른체형", bmi
#     elif bmi < 25.0:
#         return "표준", bmi
#     elif bmi < 30.0:
#         return "비만", bmi
#     else:
#         return "고도비만", bmi
#
# getBMI(48, 1.63)
#
# print "---------------------------"
#
# while(True):
#     print "안녕하세요 여러분의 건강관리를 위해 BMI를 측정하겠습니다. 거짓 없이 작성해주세요"
#     yourWeight = input("당신의 몸무게는 무엇입니까?")
#     height = input("당신의 키는 무엇입니까?")
#
#     print "당신은 현재 %s BMI 이며, %s 인 상태입니다. 감사합니다 " % (getBMI(yourWeight, height)[1], getBMI(yourWeight, height)[0])
#     print


def getTotalSum (start, end):
    sum = 0
    for i in range(start, end + 1):
        sum += i
    return sum

print getTotalSum(1, 10)


class Point:
    def __init__(self, input_x, input_y):
        self.x = input_x
        self.y = input_y