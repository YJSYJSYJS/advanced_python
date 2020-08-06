# Chapter03-1
# Sequence type
# Container: 서로 다른 자료형 저장 가능 - list, tuple, collections.deque
# flat: 한 개의 자료형 - str, bytes, bytearray, array.array, memoryview
# 가변: list, bytearray, array,array, memoryview, deque -> id값 유지
# 불변: tuple, str, bytes -> id값 변동

# 지능형 리스트(Comprehending Lists)

# Non Comprehending Lists
chars = '!@#$%^&*()_+'
temp=[]

for c in chars:
    temp.append(ord(c))

print('Ex1_1: ', temp)

# Comprehending Lists
compl1 = [ord(s) for s in chars]
print('Ex1_2: ', compl1)

# 데이터가 많아질 수록 Comprehended list가 빠르다

compl2 = [ord(s) for s in chars if ord(s) > 40]

print('Ex1_3: ', compl2)

# Comprehending Lists with Map, Filter
compl3 = list(map(ord, chars))
print('Ex1_4: ', compl3)
compl4 = list(filter(lambda x: x>40, map(ord, chars)))
print('Ex1_5: ', compl4)

# compl4보다 compl2의 속도가 약간 우세하다는 benchmark

print('Ex1_6: ', [chr(s) for s in compl1])
print('Ex1_7: ', [chr(s) for s in compl2])
print('Ex1_8: ', [chr(s) for s in compl3])
print('Ex1_9: ', [chr(s) for s in compl4])

print()

# Generator

import array

# Generator: 한 번에 한 개의 항목()을 생성(메모리 유지하지 않음 -> 좋은 성능)
# 실행 시점의 값만 반환

tuple_g = (ord(s) for s in chars)
print('Ex2_1: ', tuple_g) # generator object
# why? : ()안에 list comprehension
# ()가 아닌 [](list)인 경우 메모리를 사용해야한다.

print('Ex2_2: ', next(tuple_g))
print('Ex2_3: ', next(tuple_g)) # next를 쓸 때마다 한칸씩 이동한다.(메모리사용X)
# Conclusion: 하나씩 받아서 처리시에는 generator가 좋다!

# Array
array_g = array.array('I', (ord(s) for s in chars))

print('Ex2_4: ', array_g)
print('Ex2_5: ', array_g.tolist()) # array에서 list로 변환
print()

# Generator Examples
print('Ex3_1: ', ('%s' %c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1,11)))

for s in ('%s' %c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1,11)):
    print('Ex3_2: ', s) 
print()

# 리스트 주의할 점
marks1 = [['~']*3 for n in range(3)]
marks2 = [['~']*3]*3
print('Ex4_1: ', marks1)
print('Ex4_2: ', marks2)
print()
# two results above are the same?
# No!
marks1[0][1] = 'X'
marks2[0][1] = 'X'
print('Ex4_3: ', marks1) # 첫번째의 가운데만 수정됨
print('Ex4_4: ', marks2) # 모든 가운데가 다 수정됨
# 큰 차이가 있으므로 주의!
# reason of Difference!
# Proof
print('Ex4_5: ', [id(i) for i in marks1]) # 리스트 원소들의 id가 각각 다르다.
print('Ex4_6: ', [id(i) for i in marks2]) # 리스트 원소들의 id가 동일

# Tuple Advanced
## Packing and Unpacking, "*"
print('Ex5_1: ', divmod(100, 9))
print('Ex5_2: ', divmod(*(100, 9)))
### divmod는 원래 2개의 인자를 받지만 Packing을 통해 알아서 풀어서 쓰게 함

print('Ex5_3: ', *(divmod(100, 9))) # unpacking 발생 11과 1로 풀려서 반환

x, y, *rest = range(10)
print('Ex5_4: ', x, y, rest)
x, y, *rest = range(2)
print('Ex5_5: ', x, y, rest)
x, y, *rest = 1,2,3,4,5
print('Ex5_6: ', x, y, rest)
print()

# Mutable VS Immutable
l = (10, 15, 20)
m = [10, 15, 20]

print('Ex6_1: ', id(l), l, id(m), m)

l = l*2 # 값변경이 아닌 expand이기 때문에 가능
m = m*2
print('Ex6_2: ', id(l), l, id(m), m) # 변수에 새롭게 할당했기 때문에 id가 둘다 변경됨

l*=2
m*=2 # 새로운 할당이 아닌 기존 객체를 활용
print('Ex6_3: ', id(l), l, id(m), m) # 리스트는 id가 변경되지 않았다
print()

# sort vs sorted
# reverse, key=len, key=str.lower, key=func

f_list = ['orange', 'apple', 'mango', 'papaya', 'lemon', 'strawberry', 'coconut']

# sorted: 정렬 후 '새로운' 객체 반환
print('Ex7_1: ',sorted(f_list))
print('Ex7_2: ',sorted(f_list, reverse=True)) # 반대로
print('Ex7_3: ',sorted(f_list, key=len)) # 길자 길이순
print('Ex7_4: ',sorted(f_list, key=lambda x:x[-1])) # 요소의 특정 인덱스를 기준으로 정렬

print('Ex7_5: ', f_list) # 변경 없음

# sort: 정렬 후 객체 직접 변경
# 반환 값 확인 (None)

a = f_list.sort()
print(a, f_list)
print('Ex7_6: ', f_list.sort(), f_list)
print('Ex7_7: ', f_list.sort(reverse=True), f_list)
print('Ex7_8: ', f_list.sort(key=len), f_list)
print('Ex7_9: ', f_list.sort(key=lambda x: x[-1]), f_list)
print('Ex7_10: ', f_list.sort(key=lambda x: x[-1], reverse=True), f_list)




