# coding=utf-8

tuple1 = () # 빈 값으로 초기화
tuple2 = (1,) # 값이 하나일때는 반드시 뒤에 콘마를 붙여야 함
tuple3 = (1, 2, 3) # 가장 기본적인 초기화 및 값 생성 방법
tuple4 = 1, 2, 3 # 괄호 생략 가능
tuple5 = ('a', 'b', ('ab', 'cd')) # 튜플안에 튜플이 들어갈 수 잇다

print "---- Result ----"
print tuple1
print tuple2
print tuple3
print tuple4
print tuple5


for i in range(1, 6):
    print i

for i in range(6):
    print i