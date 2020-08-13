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
tl2 = tl1 # 얕복
tl3 = list(tl1) # 깊복

print('Ex4_1: ', tl1 == tl2)
print('Ex4_2: ', tl1 is tl2)
print('Ex4_3: ', tl1 == tl3)
print('Ex4_4: ', tl1 is tl3)

# 증명
tl1.append(1000)
tl1[1].remove(105)

print('Ex4_5: ', tl1)
print('Ex4_6: ', tl2)
print('Ex4_7: ', tl3)

print()

print(id(tl1[2]))
tl1[1]+=[110,120]
tl1[2]+=(110,120)

print('Ex4_8: ', tl1)
print('Ex4_9: ', tl2) # 튜플 재 할당(객체 새로 생성됨)
print('Ex4_10: ', tl3)
print(id(tl1[2]))
print()

# Deep Copy

# 장바구니
class Basket:
    def __init__(self, products=None):
        if products is None:
            self._products = []
        else:
            self._products = list(products)
    
    def put_prod(self, prod_name):
        self._products.append(prod_name)

    def del_prod(self, prod_name):
        self._products.remove(prod_name)

import copy

basket1 = Basket(['Apple', 'Bag', 'TV', 'Snack', 'Water'])
basket2 = copy.copy(basket1)
basket3 = copy.deepcopy(basket1)

print('Ex5_1: ', id(basket1), id(basket2), id(basket3))
print('Ex5_2: ', id(basket1._products), id(basket2._products), id(basket3._products))
print()

basket1.put_prod('Orange')
basket2.del_prod('Snack')

print('Ex5-3: ', basket1._products)
print('Ex5-4: ', basket2._products)
print('Ex5-5: ', basket3._products)
print()

# 함수 매개변수 전달 사용법
def mul(x, y):
    x += y
    return x

x = 10
y = 5

print('Ex6_1: ', mul(x, y), x, y)
print()

a = [10, 100]
b = [5, 10]
print('Ex6_2: ', mul(a, b), a, b) # 가변형 a -> 원본 데이터 변경

c = (10, 100)
d = (5, 10)
print('Ex6_3: ', mul(c, d), c, d) # 불변형 c -> 원본 데이터 변경 안됨

# 파이썬 불변형 Exception
# str, bytes, frozenset, tuple: 사본 생성 없이 바로 참조 반환

tt1 = (1, 2, 3, 4, 5)
tt2 = tuple(tt1)
tt3 = tt1[:]

print('Ex7_1: ', tt1 is tt2, id(tt1), id(tt2))
print('Ex7_2: ', tt3 is tt1, id(tt3), id(tt1))

tt4 = (10,20,30,40,50)
tt5 = (10,20,30,40,50)
ss1 = 'Apple'
ss2 = 'Apple'

print('Ex7_3: ', tt4 is tt5, tt4==tt5, id(tt4), id(tt5))
print('Ex7_4: ', ss1 is ss2, ss1==ss2, id(ss1), id(ss2))
