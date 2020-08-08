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

# Lambda
## 주석 사용 권장
## 그냥 함수로 사용하길 권장(가독성, 해독성)
## 일반 함수 형태로 리팩토링 권장

print('Ex3_5: ', reduce(lambda x, t: x+t, range(1,11)))

