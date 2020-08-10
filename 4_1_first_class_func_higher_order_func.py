# Chapter04-1
# 일급 함수(일급 객체)
# 함수 또한 객체 취급
# 사용하는 모든 것들이 사실 객체!
# 파이썬 함수 특징
# 1. 런타임 초기화(실행시에 초기화 가능)
# 2. 변수 등에 할당 가능(데코레이터나 클로저 사용에 활용)
# 3. 함수 인수 전달가능(ex: keys = len)
# 4. 함수 결과로 반환 가능 return funcs

# 함수 객체 예제
def factorial(n):
    '''
    Factorial Function -> n:int
    '''
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

print('Ex1_1: ', factorial(5))
print('Ex1_2: ', factorial.__doc__)

class A:
    pass

print('Ex1_3: ', type(factorial), type(A))
# function도 class다!

print('Ex1_4: ', dir(factorial))
print()
print('Ex1_5: ', dir(A))
print()
print('Ex1_6: ', set(dir(factorial))-set(dir(A))) # function만 가지고 있는 attributes
print()
print('Ex1_7: ', set(sorted(dir(A)))-set(sorted(dir(factorial)))) # class만 가지고 있는 attributes
print()
print('Ex1_8: ', factorial.__name__)
print('Ex1_9: ', factorial.__code__)
print()

# 변수에 함수 할당
var_func = factorial
print('Ex2_1: ', var_func)
print('Ex2_2: ', var_func(5))
print()
print('Ex2_3: ', list(map(var_func, range(1, 6))))

# 함수의 인수 전달 및 함수로 결과 반환 -> 고위 함수(Higher-order function)
print('Ex3_1: ', list(map(var_func, filter(lambda x: x%2, range(1,6)))))
print('Ex3_2: ', [var_func(i) for i in range(1,6) if i%2])
# 3_1과 3_2 중 주관적으로 가독성이 좋은 표현으로 사용! 보편적으로 comprehension이 보기 편하다.
print()

# reduce()
from functools import reduce
from operator import add

print('Ex3_3: ', reduce(add, range(1, 11))) # 누적, 그리 자주 쓰이진 않음
print('Ex3_4: ', sum(range(1,11)))

# Lambda(익명함수)
## 주석 사용 권장
## 그냥 함수로 사용하길 권장(가독성, 해독성)
## 일반 함수 형태로 리팩토링 권장

print('Ex3_5: ', reduce(lambda x, t: x+t, range(1,11))) # 3_3의 add -> lambda
print()

# Callable(핵심): 호출 연산자
## 메소드 형태로 호출 가능한지 확인
## Magic Method __call__ 있는지

# 로또 추첨 클래스 선언
import random

class LottoGame:
    def __init__(self):
        self._balls = [n for n in range(1, 46)]

    def pick(self):
        random.shuffle(self._balls)
        return sorted([random.choice(self._balls) for n in range(6)])

    def __call__(self):
        return self.pick()


# 객체 생성
game = LottoGame()

# 게임 실행
# is Callable?
print('Ex4_1: ', callable(str), callable(list), callable(factorial), callable(3.14))
print('Ex4_2: ', game.pick())

# game() # LottoGame object is not callable
# -> __call__

print('Ex4_3: ', game())
print('Ex4_4: ', callable(game))
print()
# 함수로도 변수로도 클래스 자체로도 다룰 수 있다!!

# 다양한 매개변수 입력(*args, **kwargs)
def args_test(name, *contents, point=None, **attrs):
    return '<args_test> -> ({}) ({}) ({}) ({})'.format(name, contents, point, attrs)

print('Ex5_1: ', args_test('test1'))
print('Ex5_2: ', args_test('test1', 'test2'))
print('Ex5_3: ', args_test('test1', 'test2', 'test3', id='admin'))
print('Ex5_4: ', args_test('test1', 'test2', 'test3', id='admin', point=7))
print('Ex5_4: ', args_test('test1', 'test2', 'test3', id='admin', point=7, password='1234'))
print()

# 함수 Signatures
from inspect import signature # inspect 패키지는 꽤 사용된다.
sg = signature(args_test)
print('Ex6_1: ', sg)
print('Ex6_2: ', sg.parameters)
print()

# 모든 정보 출력
for name, param in sg.parameters.items():
    print('Ex6_3: ', name, param.kind, param.default) 

# Partial 사용법: 인수 고정 -> 주로 특정 인수 고정 후 Callback 함수에 사용
# official description: 하나 이상의 인수가 이미 할당된 함수의 새 버전 반환
# 함수의 새 객체 타입은 이전 함수의 자체를 기술하고 있다.
from operator import mul
from functools import partial

print('Ex7_1: ', mul(10, 100))
# 인수 고정
five = partial(mul, 5)

# 고정 추가
six = partial(five, 6)

print('Ex7_2: ', five(1000))
print('Ex7_3: ', six())
print('Ex7_4: ', [five(i) for i in range(1,11)])
# 이외에도 partial을 인자로 요구하는 함수들이 있기도 하다

print('Ex7_5: ', list(map(five, range(1,11))))
