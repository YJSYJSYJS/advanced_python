# Chapter02-1
# Data Model
# ref: https://docs.python.org/3/reference/datamodel.html
# Namedwtuple
# Sequence, Iterator, Function, Class

# 객체 -> 파이썬의 데이터 추상화
# 모든 객체 -> id, type -> value

a= 7
print(id(a), type(a), dir(a))

for a in dir(a):
    print(a)

# 파이썬 -> 일관성

# 일반적인 튜플 사용

pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from math import sqrt

leng = sqrt((pt2[0]-pt1[0])**2 + (pt2[1]-pt1[1])**2)

print('EX1_1: ', leng)


# 네임드 튜플 사용

from collections import namedtuple as nt

Point = nt('Point', 'x y')

pt1 = Point(1.0, 5.0)
pt2 = Point(2.5, 1.5)

leng2 = sqrt((pt2.x - pt1.x)**2 + (pt2.y-pt1.y)**2)

print('EX1_2:', leng2)

# 네임드 튜플 선언 방법
P1 = nt('Point', ['x', 'y'])
P2 = nt('Point', 'x, y')
P3 = nt('Point', 'x y')
P4 = nt('Point', 'x y x class', rename=True) # defaualt = False

# 출력
print('EX2_1: ', P1, P2, P3, P4)

# 객체 생성
p1 = P1(x=10, y=35)
p2 = P2(20, 40)
p3 = P3(45, y=20)
p4 = P4(10, 20, 30, 40)

print('Ex2_2: ', p1, p2, p3, p4)

# Dict to Unpacking
temp_dict = {'x': 75, 'y': 55}
p5 = P3(**temp_dict)

print(p5)

# 사용
print('Ex3_1: ', p1[0] + p2[1]) # Index Error 주의
print('Ex3_2: ', p1.x + p2.y) # 클래스 변수 접근방식

# Unpacking
x, y = p3
print('Ex3_3: ', x+y)

# Rename 테스트
print('Ex3_4: ', p4)

print()
print()

# Namedtuple Method
temp = [52, 38]

## _make(): 새로운 객체 생성
p4 = P1._make(temp)#(리스트를 nt에 넣어줌)

print('Ex4_1: ', p4)

## _fields: 필드 네임 확인
print('Ex4_2: ', p1._fields, p2._fields, p3._fields)# nt안에 어떤 것들이 들어있는지 확인 가능

## _asdict(): OrderedDict 반환

print('Ex4_3: ', p1._asdict(), p4._asdict())# dictionary 형태로

## _replace(): 수정된 '새로운' 객체 반환

print('Ex4_4: ', p2._replace(y=100)) # 기존의 y=40 -> 100으로 대체(수정)
