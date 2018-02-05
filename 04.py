print "------- 1 ---------"
daum = 89000
naver = 751000
man = (100 * daum) + (20 * naver)
print man


print "------- 2 --------"
down = ((daum * 0.95) * 100) + ((naver * 90)*20)
print down

F = 50
# F = (1.8 * C) + 32
C = (F-32)/1.8
print C

print "------- 4--------"
for i in range(9):
    print "pizza!"


print "------- 5--------"
mon = 1000000
for i in range(3):
    wen = mon * 0.7
    mon = wen
print wen
# Todo Number5




print "------- 6 --------"
boke = {"Name" : "Python",
    "Birth" : "2014. 12. 12.",
    "SocialSecuritynumber" : "20141212-1623210"}

print boke

print "------- 7 --------"
S = "Daum Kakao"

print S[0:4]
print S[5:10]

print S[5:10] + " " + S[0:4]

print "------- 8 --------"
a = "hello world"
print a.replace("hello", "hi")

print "------- 9 --------"
x = "abcdef"
print x[1:7] + x[0]


print "------- 3_1 --------"
naver_end_price = [474500, 461500, 501000, 500500, 488500]
print max(naver_end_price)

print "------- 3_3 --------"
print min(naver_end_price)

print "------- 3_4 --------"
print max(naver_end_price) - min(naver_end_price)

print "------- 3_5 --------"
naver_end_price = {"mon" : 474500, "tue" : 461500, "wen" : 501000, "thr" : 500500, "fri" : 488500}
print naver_end_price["wen"]

print "------- 4_1--------"

for _ in range(5):
    print "*",
print

print "------- 4_2--------"
for _ in range(4):
    for _ in range(5):
        print "*",
    print


print "------- 4_3--------"
for i in range(5):
    for j in range(i+1):
        print "*",
    print


print "------- 4_4--------"
for i in range(5):
    for j in range(5-i):
        print "*",
    print

print "------- 4_5--------"
for i in range(5):
    x = (" " * (4-i))
    y = ("*" * ((2*i) + 1))
    print x + y
print

print "------- 4_6--------"
row = 7
for i in range(row):
    x = (" " * (i))
    y = ("*" * (((row * 2) - 1) - (2*i)))
    print x + y
print


print "------- 4_6--------"

n = [474500, 461500, 501000, 500500, 488500]


def max(list):
    max = 0
    for i in list:
        if max <= i:
            max = i
    return max


print max(n)



def min(list):
    min = 999999999
    for i in list:
        if min >= i:
            min = i
    return min

print min(n)
