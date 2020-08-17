# Chapter05-2
# 파이썬 클래스 특별 메소드 심화 활용 및 상속
# Class ABC

# class 선언
class VectorP(object):
    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    def __iter__(self):
        return (i for i in (self.__x, self.__y)) # Generator! ()말고 [] 쓰면 리스트로 통채로 반환

    @property # instance 은닉화
    def x(self):
        print('Called Property X')
        return self.__x # __x로 부르면 오류발생하지만, x로 부르면 가능!

    @x.setter
    def x(self, v):
        print('Called Property X Setter')
        self.__x = float(v)

    @property
    def y(self):
        print('Called Property Y')
        return self.__y # __y로 부르면 오류발생하지만, y로 부르면 가능!

    @x.setter
    def y(self, v):
        print('Called Property Y Setter')
        if v<30:
            raise ValueError('y below 30 is not allowed')
        self.__y = float(v)

# 객체 선언
v = VectorP(20, 40)

# print('Ex1_1: ', v.__x, v.__y) 
# 변수 앞이 _ 두개(__)이면 위의 방법으로는 접근 불가

# Getter, Setter
# notice about decorator name!
print('Ex1_2: ', dir(v), v.__dict__)
print('Ex1_3: ', v.x, v.y)

# Iter 확인
for val in v:
    print('Ex1_4: ', val)

# Private
# ------------------------------------------
# Slot
# __slot__: 파이썬 인터프리터에게 통보
# 해당 클래스가 가지는 속성을 제한
# __dict__속성 최적화 -> 다수 객체 생성시 메모리 사용공간 대폭 감소
# # 해당 클래스에 만들어진 인스턴스 속성 관리에 딕셔너리 대신 Set 형태를 사용
# 데이터가 많은 머신러닝 같은 경우 클래스에 slot을 사용하는 경우가 굉장히 많음

class TestA(object):
    __slots__ = ('a',)

class TestB(object):
    pass

use_slot = TestA()
no_slot = TestB()

print('Ex2_1: ', use_slot)
# print('Ex2_2: ', use_slot.__dict__)
print('Ex2_3: ', no_slot)
print('Ex2_4: ', no_slot.__dict__)

# 메모리 사용량 비교
import timeit

# 측정을 위한 함수 선언
def repeat_outer(obj):
    def repeat_inner():
        obj.a = 'TEST'
        del obj.a
    return repeat_inner

# print(min(timeit.repeat(repeat_outer(use_slot), number=1000000)))
# print(min(timeit.repeat(repeat_outer(no_slot), number=1000000)))
print()

# 객체 슬라이싱

class ObjectS:
    def __init__(self):
        self._numbers = [n for n in range(1, 10000, 3)]

    def __len__(self):
        return len(self._numbers)

    def __getitem__(self, idx):
        return self._numbers[idx]

s = ObjectS()

# print('Ex3_1: ', s.__dict__)
print('Ex3_2: ', len(s)) # __len__ method 없으면 에러발생
print('Ex3_3: ', len(s._numbers))
print('Ex3_4: ', s[1:100])
print('Ex3_5: ', s[-1])
print('Ex3_6: ', s[::10])
print()

# 파이썬 추상 클래스!
# ref: https://docs.python.org/3/library/collections.abc.html
# collections 가 필수로 포함해야 하는 필수 메소드들 확인 가능
# 개발과 관련된 공통된 내용(필드, 메소드...) 추출 및 통합해서 공통된 내용으로 작성하게 하는 것
# 언어에 따라 다르지만 자체적으로 객체생성 불가!
# -> 상속을 통해 자식 클래스에서 인스턴스를 생성해야 한다!
    # ex Phone ABC -> 전화걸다, 끊다, 베터리 충전... -> 갤럭시s9, v30...

# 강제성이 있는 경우 실습
# Sequence 관련된 것을 상속받아서 사용해보자!
# 요구사항인 추상메소드를 모두 구현해야 동작함!
# Sequence 상속 받지 않았지만 자동으로 기능(__iter__, __contain__)을 작동(파이썬이)하는 경우
# 객체 전체를 자동으로 조사 -> 시퀀스 프로토콜

class IterTestA():
    def __getitem__(self, idx):
        return range(1, 50, 2)[idx] # range(1, 50, 2)

i1 = IterTestA()
print('Ex4_1: ', i1[4])
print('Ex4_2: ', i1[4:10])
print('Ex4_3: ', 3 in i1[1:10])
# contain이 작동했다는 것이 확인됨(by sequence protocol)

# print('Ex4_4: ', [i for i in i1])

# Sequence 상속받고 하는 경우(기존에 했던 방법)
# 요구사항인 추상메소드를 모두 구현해야 동작한다!

from collections.abc import Sequence

class IterTestB(Sequence):
    def __getitem__(self, idx):
        return range(1, 50, 2)[idx] # range(1, 50, 2)

# i2 = IterTestB() # len을 구현해야된다는 에러발생!, getitem이 없어도 에러 발생한다
# 전의 케이스에서는 내부적으로 알아서 해준 것이였다!
# 여기서는 FM대로 구현을 해줘야함

class IterTestC(Sequence):
    def __getitem__(self, idx):
        return range(1, 50, 2)

    def __len__(self, idx):
        return len(range(1, 50, 2)[idx])

i3 = IterTestC()

print('Ex4_5: ', i3[4])
print('Ex4_6: ', i3[4:10])
print('Ex4_7: ', 3 in i3[1:10])

# abc 활용 예제 (뽑기 기계)
import abc

class RandomMachine(abc.ABC): # metaclass=abc,ABCMeta(3.4이하는 이걸로 대체)
    # __metaclass__ = abc.ABCMeta(3.4이하)
    
    # Abstract Method
    # Decoration
    @abc.abstractmethod
    def load(self, iterobj):
        '''add Iterable object'''

    @abc.abstractclassmethod
    def pick(self, iterobj):
        '''picking random object'''

    def inspect(self):
        items = [] # self가 아님!
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
            return tuple(sorted(items))

import random

class CraneMachine(RandomMachine):
    def __init__(self, items):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self, items): # 상위인 추상클래스에 구현부가 없기 떄문에 자식에서 구현!
        self._items.extend(items)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('Empty Crane Box')

    def __call__(self):
        return self.pick()


# Sub class check
print('Ex5_1: ', issubclass(RandomMachine, CraneMachine))
print('Ex5_2: ', issubclass(CraneMachine, RandomMachine))

# 상속 구조 확인
print('Ex5_3: ', CraneMachine.__mro__)       

cm = CraneMachine(range(1, 100)) # 추상 메소드 오버라이딩으로 구현 안하면 에러 발생!

print('Ex5_4: ', cm._items)
print('Ex5_5: ', cm.pick())
print('Ex5_6: ', cm())
print('Ex5_7: ', cm.inspect())

