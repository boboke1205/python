# coding=utf-8
sample= " My favorite language is python"

print "----result_ 문자열 함수------"
print len(sample)
print sample.count("a")
print sample.index("y")
print sample.upper()
print sample.strip()
print sample.replace("python", "java")
print sample.split()

print "----result_ 리스트 함수------"

# 준비
list = [12, 5, 3, 12]
print list

#리스트 맨 뒷부분에 추가할 값 추가
list.append(27)
print list

# 리스트 정렬
list.sort()
print list

# 리스트 정렬 (역순)
list.sort(reverse=True)
print list

#리스트에서 찾을 값의 위치를 반환
print list.index(12)

#리스트에서 넣을 위치에 넣을 값을 넣어준다 .
list.insert(0, 3)
print list

#리스트에서 삭제할 값을 찾아서 삭제 (가장 먼저 나온 값)
list.remove(3)
print list

#리스트에서 찾을 값이 몇개 있는지 개수를 세서 반환
print list.count(12)

#리스트에서 확장할리스트 붙임
list.extend(['p', 's', 'y'])
print list


print "--------dictionary--------------"

leeboke = {'name':'leebokyung', 'phone':'01010', 'birth':'1205'}
print leeboke
print leeboke['name']
print leeboke['phone']
print leeboke['birth']


#추가하기
leeboke["age"] = 20
print leeboke

#같은 key에 추가하기
leeboke['age'] = 25
print leeboke

#삭제하기
del leeboke['phone']
print leeboke

#key만 출력하기
print leeboke.keys()

#key만 출력하기
print leeboke.values()



##p102
a, b = ('python', 'life')
print a
print b

(a, b) = 'python', 'life'
print a
print b

[a, b] = ['python', 'life']
print a
print b
print [a, b]

a = b = 'python'
print [a, b]

a = 3
b = 5
a, b = b, a
print [a, b]

pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass
else:
    print ("카드를 꺼내라")

#
# prompt = """
#     1. Add
#     2. Del
#     3. List
#     4. Quit
#
#     Enter number: """
#
# number = 0
# while number != 4:
#     print(prompt)
#     number = int(input())
#


print "---------for + list -----------"
#
# a = [1, 2, 3, 4]
# result = []
# for num in a:
#     result.append(num*3)
#
# print result
#
#
# result = [num * 3 for num in a]
# print result
#
# result = [num * 3 for num in a if num % 2 == 0]
# print result


print "---------for + list -----------"
result = [x*y for x in range (2,10)
            for y in range(1, 10)]
print result