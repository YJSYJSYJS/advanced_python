# Chapter03-1
# Sequence type
# Container: 서로 다른 자료형 저장 가능 - list, tuple, collections.deque
# flat: 한 개의 자료형 - str, bytes, bytearray, array.array, memoryview
# 가변: list, bytearray, array,array, memoryview, deque
# 불변: tuple, str, bytes

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