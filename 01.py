# coding=utf-8
print "hello world"

data1 = 3
data2 = 2

print '---- Result----'
print data1 + data2  # 더하기
print data1 - data2  # 빼기
print data1 * data2  # 곱하기
print data1 / data2  # 나누기
print data1 ** data2  # 제곱
print data1 % data2  # 나머지

data1 = "hello"
data2 = "     world"

print '----------result---------'
print data1 + data2 # 더하기

print(data1 * 5)

data1 = "hello! \n"* 5
print data1


data1 = " \"hello\" "
print data1

data1 = "hello \tbye"
print(data1)

data = "hello world"
print data[4]
print data[8]
print (data[4])

print data[1:]

print '----result-----'
print data[0:4] # hell
print data[:5] #hello
print data[6:] #world
print data[-1] #d

data1 = "H1 %s !" % "Alex"
data2 = "Hi %s !" % "Anna"
data3 = "Hi %s and %s!" % ("alex", "anna")

print '----result-----'
print data1
print data2
print data3

alex = "alex"
anna = "anna"
print "Hi " + alex + " and " + anna

sample = "  My favorite language is Python  "
print '----result-----'
print len(sample)
print sample.count('a')
print sample.index('y')
print sample.upper()
print sample.lower()
print sample.strip()
print sample.replace("Python", "java" )
print sample.split(' ')

sampleList = [1, 2, 3, [4, 5, 6]]
print '-----result---------'
print sampleList[0]
print sampleList[1]
print sampleList[2]
print sampleList[3]
print sampleList[3][1]

sampleList = [1, 2, 3, [4, 5, 6, ['a', 'b', 'c']]]
print sampleList[3][3][1]

sampleList = [1, 2, 3, [4, 5, 6, ['a', 'b', 'c', 'd', 'e']]]
print sampleList[3][3][1:4]

list1 = [1, 2, 4]
list2 = [4, 5, 6]

print '----result-----'
print list1 + list2
print list1 * 2


list = [1, 2, 3]
print '----result-----'
print list

list[1] = 10 # 여기서 2 -> 10 을 바꿔줌
print '----result-----'
print list


list.append([1, 2, 3])
print list




print '-------result----'
list = [12, 5, 3, 12]
print list

list.append(27)
print(list)

list.sort()
print(list)

list.sort(reverse=True)
print list

list.sort(reverse=False)
print list

print list.index(12)

list.insert(3, 3)
print list

list.remove(3)
print list

print list.count(12)


list.extend(['p', 's', 'y', 'x'])
print list

# 안녕 나 git 테스트 중이야
