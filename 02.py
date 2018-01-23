# coding=utf-8

# tuple1 = () # 빈 값으로 초기화
# tuple2 = (1,) # 값이 하나일때는 반드시 뒤에 콘마를 붙여야 함
# tuple3 = (1, 2, 3) # 가장 기본적인 초기화 및 값 생성 방법
# tuple4 = 1, 2, 3 # 괄호 생략 가능
# tuple5 = ('a', 'b', ('ab', 'cd')) # 튜플안에 튜플이 들어갈 수 잇다
#
# print "---- Result ----"
# print tuple1
# print tuple2
# print tuple3
# print tuple4
# print tuple5


tuple7 = ('a', 'b', ['ab', 'cd'])  # 튜플안에 튜플이 들어갈 수 잇다
tuple8 = ['a', 'b', ('ab', 'cd')]  # 튜플안에 튜플이 들어갈 수 잇다

print tuple7
print tuple8

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (11, 22, 33)

print "-----result------"
print(tuple1[0])
print(tuple1[1:3])
print(tuple1 + tuple2)
print tuple2 * 3

# del tuple1[1]
# print(tuple)

# -----------------

leebokyung = {'name': 'bokyung', 'phone': '01010', 'birth': 23}

print("\n------Result----\n")
print leebokyung
print leebokyung['name']
print leebokyung['phone']
print leebokyung['birth']

print("\n------Result2----\n")
# 추가하기
leebokyung['age'] = 20
print leebokyung

# 같은 key에 추가하기
leebokyung['age'] = 25
print leebokyung

# 삭제하기
del leebokyung['phone']
print leebokyung

# key 만 출력하기
print leebokyung.keys()

# 값만 출력하기
print leebokyung.values()

set1 = {1, 2, 3}
set2 = set("hello")

print "\n-----------Result-------\n"

print set1
print set2  # 중복을 허용하지 않음.

set3 = {1, 2, 3, 4}
set4 = set("hello1")

print "\n-----------Result2-------\n"

print set3
print set4  # 중복을 허용하지 않음.

set1 = {1, 2, 3, 4, 5, 6}
set2 = set([4, 5, 6, 7, 8, 9])

print "\n---- Result ----\n"

print set1 & set2  # 교집합
print set1.intersection(set2)  # 교집합

print '\n'

print set1 | set2  # 합집합
print set1.union(set2)  # 합집합

print '\n'

print set1 - set2  # 차집합
print set1.difference(set2)  # 차집합


a = 8
b = 10

if a>b:
    print("a is larger than b")
else:
    print("b is larger than a")

money = 4000
card = 1
if money >= 2000:
    print("택시를 타야해")
else:
    print("걸어가야겠어")

if not False:
    print "ghj"


print money >= 2000



pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고가렴")
else:
    print("걸어가야지")

index = 0
while index <= 10:
    print(index)
    index= index + 1
    # index+=1

# tree = 1
# if tree <=10:
#     print "나무를" + tree


tree = 1
while tree<= 11:
    if tree<= 10:
        print "나무를 %d번 찍었습니다" % tree
        tree = tree + 1
    else:
        print "나무 넘어갑니다"
        tree = tree + 1

# tree = 1
# while tree <= 10:
#     if tree <= 10 :
#         print "나무를 %d번 찍었습니다" % tree
#         tree = tree + 1
# print "나무 넘어갑니다"


# 정답
# tree = 1
# while tree < 11:
#     if tree <= 10:
#         print "나무를 %d번 찍었습니다" % tree
#         tree = tree + 1
# print "나무 넘어갑니다"



index = 0
while index <= 10:
    print index

    if index == 5:
        break

    index = index + 1

print "------ "
index = 0
while index < 10:
    index = index + 1

    if index % 2 == 0:
        continue

    print index


scores = [90, 25, 67, 45, 80]
for I in scores:
    print I


scores = [90, 25, 67, 45, 80]

total = 0
count = 0

for score in scores:
    print score
    total = total + score
    count = count + 1

print "Sum : %d" % total
print "Avg : %d" % (total / count)


for i in range(1, 10):
    print i


for _ in range(1, 10):
    print "Hello"


print("--- 구구단====")
for i in range(2, 10):
    print("-%s단---" % i)
    for j in range(1, 10):
        print "%s * %s = %s" % (i, j, i*j)