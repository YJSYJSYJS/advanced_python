# Chapter05-1
# Python Object Reference (객체 참조)

print('Ex1_1: ')
print(dir()) # 현재 scope의 속성값
print(__name__)

# id vs __eq__ (==) 증명
x = {'name': 'Youn', 'age': 28, 'city': 'Seoul'}
y = x

print('Ex2_1: ', id(x), id(y))
print('Ex2_2: ', x==y)
print('Ex2_3: ', x is y)
print('Ex2_4: ', x, y)

x['class'] = 10
print('Ex2_5: ', x, y)
print()
# y에 x를 할당한 후에 x를 수정 추가하여도 y에 똑같이 반영된다 (깊은 복사!)
# id 값이 같다

z = {'name': 'Youn', 'age': 28, 'city': 'Seoul', 'class': 10}

print('Ex2_6: ', x, z)
print('Ex2_7: ', x is z)
print('Ex2_8: ', x is not z)
print('Ex2_9: ', x==z)
# 내용은 같아도 id 값이 다르다!

# 객체 생성 후 완전 불변 -> 즉, id는 객체 주소(정체성)비교, ==(__eq__) 는 값 비교
# dictionary의 key가 수백만개일 경우, ==으로 비교를 해버리면, 모든 key value에 접근해야하지만
# is는 객체의 주소만 바로 비교하기 때문에, ==에 is부터 사용해서 비교하는 것이 좋다!
print()

# 튜플 불변형의 비교
tuple1 = (10, 15, [100, 1000])
tuple2 = (10, 15, [100, 1000])

print('Ex3_1: ', id(tuple1), id(tuple2))
print('Ex3_2: ', tuple1 is tuple2)
print('Ex3_3: ', tuple1 == tuple2)
print('Ex3_4: ', tuple1.__eq__(tuple2))
print()

# Copy, Deepcopy(얕은 복사, 깊은 복사)
# Copy
tl1 = [10, [100, 105], (5, 10, 15)]
tl2 = tl1
tl3 = list(tl1)

print('Ex4_1: ', tl1 == tl2)
print('Ex4_1: ', tl1 is tl2)
print('Ex4_1: ', tl1 == tl3)
print('Ex4_1: ', tl1 is tl3)
