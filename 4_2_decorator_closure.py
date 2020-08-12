# Chapter04-2
# 일급 함수(일급 객체)
# Decorator&Closure

# 파이썬 변수 범위(global)

# 예제 1
# def func_v1(a):
#     print(a)
#     print(b)

# # 예외
# func_v1(5) # NameError: name 'b' is not defined

# 예제 2
b=10

def func_v2(a):
    print(a)
    print(b)

func_v2(5)

# 예제 3
b=10

def func_v3(a):
    print(a)
    print(b)
    b=5

# func_v3(5) # UnboundLocalError: local variable 'b' referenced before assignment
# 지역변수가 전역변수보다 더 우선(b=5)
# 할당 전에 참조하기 때문에 에러 발생

from dis import dis

print('Ex1_1: ')
print(dis(func_v3))

# Closure
# 반환되는 내부 함수에 대해서 선언된 연결 정보를 가지고 참조하는 방식
# 반환 당시 함수 유효범위를 벗어난 변수 또는 메소드에 직접 접근이 가능하다

a = 10

print('Ex2_1: ', a+10)
print('Ex2_2: ', a+100)

# 결과를 누적시키려면?
print('Ex2_3: ', sum(range(1,51)))
print('Ex2_4: ', sum(range(51,101)))
print()

# 함수가 아니라 클래스 형태로 누적하려면?
class Averager():
    def __init__(self):
        self._series = []

    def __call__(self, v):
        self._series.append(v)
        print('class >>> {} / {}'.format(self._series, len(self._series)))
        return sum(self._series)/len(self._series)

# instance
avg_cls = Averager()

# 누적 확인
print('Ex3_1: ', avg_cls(10))
print('Ex3_2: ', avg_cls(35))
print('Ex3_3: ', avg_cls(40))
# values의 attribute로 저장을 계속 해주기 때문에 가능하다!

# Closure 사용

def closure_avg1():
    # Free variable(co_freevars)
    series = [] # 일급 객체
    # closure territory
    def averager(v):
        # series = [] # 여기 두면 유지가 되지 않는다.
        series.append(v)
        print('def >>> {} / {}'.format(series, len(series)))
        return sum(series) / len(series)
    
    return averager # ()를하면 함수의 실행결과가 반환되지만, 여기서는 함수 자체를 반환

avg_closure1 = closure_avg1()

print('Ex4_1: ', avg_closure1(15))
print('Ex4_2: ', avg_closure1(35))
print('Ex4_3: ', avg_closure1(40))

# 함수형 프로그램이나 누적횟수 저장, 인터넷 방문 로그(웹타이틀...) 저장에 활용
# 전역변수 사용을 감소시킬 수 있고
# 디자인 패턴 적용
# 외부에서는 보이지 않기 때문에 정보 은닉화 가능
# 또한, 함수의 실행이 끝나도 접근이 가능
print()

# check
print('Ex5_1: ', dir(avg_closure1))
print()
print('Ex5_2: ', dir(avg_closure1.__code__))
print()
print('Ex5_3: ', avg_closure1.__code__.co_freevars)
print()
print('Ex5_4: ', dir(avg_closure1.__closure__[0].cell_contents))
print()

# 잘못된 클로저 사용 예

def closure_avg2():
    # Free variable
    cnt = 0
    total = 0
    # closure 영역
    def averager(v):
        nonlocal cnt, total # 오류 해결을 위한 부분(없으면 에러 발생(UnboundLocalError))
        cnt+=1
        total+=v # 밖의 free variables와 별개 -> 초기화가 되어있지않으므로 연산이 불가
        print('def2 >>> {} / {}'.format(total, cnt))
        return total/cnt
    return averager

avg_closure2 = closure_avg2()
print('Ex5_5: ', avg_closure2(15))
print('Ex5_6: ', avg_closure2(35))
print('Ex5_7: ', avg_closure2(40))

# practice Decorator
# 장점
## 1. 중복 제거, 코드 간결
## 2. 클로저 보다 문법 간결
## 3. 조합에서 사용 용이

# 단점
# 1. 디버깅 어려움
# 2. 에러의 모호함
# 3. 에러 발생 지점 추적 어려움

import time

def perf_clock(func):
    def perf_clocked(*args):
        # 시작 시간
        st = time.perf_counter()
        result = func(*args)
        # 종료 시간
        et = time.perf_counter() - st
        # 함수명
        name = func.__name__
        # 매개변수
        arg_str = ','.join(repr(arg) for arg in args)
        # 출력
        print('[%0.5fs] %s(%s) -> %r' % (et, name, arg_str, result))
        return result
    return perf_clocked

def time_func(seconds):
    time.sleep(seconds)

def sum_func(*numbers):
    return sum(numers)

def fact_func(*numbers):
    return 1 if n<2 else n*fact_func(n-1)

# 데코레이터 미사용

non_deco1 = perf_clock(time_func)
non_deco2 = perf_clock(sum_func)
non_deco3 = perf_clock(fact_func)

print('Ex7_1: ', non_deco1, non_deco1.__code__.co_freevars)
print('Ex7_1: ', non_deco2, non_deco2.__code__.co_freevars)
print('Ex7_1: ', non_deco3, non_deco3.__code__.co_freevars)

print('*'*40, 'Called Non Deco -> time_func')
print('Ex7_4: ')
non_deco1(2)
print('*'*40, 'Called Non Deco -> sum_func')
print('Ex7_5: ')
non_deco2(100,200,300,500)