# coding=utf-8
print "--------"
try:
    a = 12
    print 144 / a
except ZeroDivisionError:
    print "0으로 나누었음"
finally:
    print "무조건 실행 되는 부분"

print "--------"
try:
    a = 12
    print 144 / 0
except ZeroDivisionError:
    print "0으로 나누었음"
finally:
    print "무조건 실행 되는 부분"
