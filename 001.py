# coding=utf-8

def printMyname():
    print "jungwoon"

printMyname()


def calculationPlus(a, b):
    print "Sum is %d" % (a + b)

calculationPlus(19, 32)


def getMyBirthDay():
    return "12.05."

print 'My birth is %s' % getMyBirthDay()

def plus(a, b):
    return  a + b
print "Sum is %d" % plus(12, 78)


def plus(*values):
    tot = 0

    for value in values:
        tot = tot + value

    return tot

print "Sum is %d" % plus(12, 89, 45 ,66)



def sayNickname(nickname):
    if nickname == "idiot":
        return

    return nickname

print "My nickname is %s" % sayNickname("Pretty")
print "MY nickname is %s" % sayNickname("idiot")


def calculate(a, b):
    return a + b, a * b

print calculate(12, 23) #결과값이 여러개일때는 '한 개'의 튜플로 받는다
print calculate(12, 23)[0] #더하기한 결과 값만 가져오기
print calculate(12, 23)[1] #곱하기한 결과 값만 가져오기


def checkBreakfast(name, room, meal=True):
    print "Name :%s" % name
    print "Room :%d" % room

    if meal:
        print "include breakfacst"
    else:
        print "no breakfast"

checkBreakfast("jungwoon", 302)
print "-----------------------"
checkBreakfast("bokyung", 303, False)

a = 123
def checkLocalValue():
    global a # 글로벌 변수 a 를 사용하겠다는 의미입니다.
    a = 32
    print a

checkLocalValue()
print a

# data = input()
# print data
#
# number = input("숫자를 입력하세요 : ")
# print number


newFile = open("C:\coding\python\python_lecture\hello.txt", "w")

for i in range(20):
    newFile.write("%d Hello World\n" % i)

newFile.close()

newFile = open("C:\coding\python\python_lecture\hello.txt", "r")
print newFile.read()
newFile.close()

newFile = open("C:\coding\python\python_lecture\hello.txt", "r")
print newFile.readline()
print newFile.readline()
print newFile.readline()
newFile.close()

newFile = open("C:\coding\python\python_lecture\hello.txt", "r")
while True:  #무한루프도는 아이
    line = newFile.readline()
    if not line:
        break
    print line

newFile.close()


newFile = open("C:\coding\python\python_lecture\hello.txt", "r")
lines = newFile.readlines()

for line in lines:
    print line

newFile.close()


with open("C:\coding\python\python_lecture\hello.txt", "r") as newFile:
    lines = newFile.readlines()

    for line in lines:
        print line
