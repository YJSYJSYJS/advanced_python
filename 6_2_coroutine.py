# Chapter06-2
# 흐름제어, 병행처리(Concurrency)
# Coroutine

# yield: 메인 루틴 <--> 서브 루틴(서브루틴을 동시에 여러개)
# 코루틴 제어, 코루틴 상태, 양방향 값 전송
# yield from

# <서브루틴> 
# - 메인루틴에서 
# - 리턴에 의해 호출 부분으로 돌아와 
# - 다시 프로세스 시작

# <코루틴> 
# - 루틴 실행 중 멈춤 가능, 
# - 특정 위치로 돌아갔다가 
# - 다시 원래 위치로 돌아와 수행
# -> 동시성 프로그래밍 가능
# - 가독성이 좀 떨어짐, 높은 이해도 요구
# - 하나의 쓰레드에서 실행하기 때문에 스케쥴링 오버헤드가 매우 적다.

# <쓰레드>
# - 운영체제에서 생성해줌
# - 이전까지는 싱글쓰레드 사용했었음
# - 멀티쓰레드: 복잡, 공유되는 자원의 교착상태 발생 가능성이 있다. -> 주의 깊게 진행(lock)해야 한다.
# -- 컨텍스트 스위칭 비용 발생, 자원 소비 증가


# 코루틴 예제1
def coroutine1():
    print('>>> coroutine started.')
    i = yield # 양방향 전송!
    print('>>> coroutine received: {}'.format(i))

# def coroutine1():
#     print('>>> coroutine started.')
#     i = yield # 양방향 전송!
#     print('>>> coroutine received: {}'.format(i))

# def coroutine1():
#     print('>>> coroutine started.')
#     i = yield # 양방향 전송!
#     print('>>> coroutine received: {}'.format(i))

# def coroutine1():
#     print('>>> coroutine started.')
#     i = yield # 양방향 전송!
#     print('>>> coroutine received: {}'.format(i))

# def coroutine1():
#     print('>>> coroutine started.')
#     i = yield # 양방향 전송!
#     print('>>> coroutine received: {}'.format(i))

# -> 여러개의 함수를 비동기, 흐름제어
# 동시성 프로그래망 가능하게함
# 엄밀히 말하면 Generator를 활용하여 진행

# 제네레이터 선언
c1 = coroutine1()
print('Ex1_1: ', c1, type(c1)) # class generator!

# yield 실행 전까지 진행
# next(c1)
# next(c1) # 기본으로 None 전달 - error

# 값 전송
# c1.send(100) # 여러 코루틴이 yield에서 멈춰있을 때, send를 통해 무엇을 먼저 수행할지 자유롭다

# 잘못된 사용 예시
c2 = coroutine1()

# c2.send(100) 예외 발생

# 코루틴 예제2
# GEN_CREATED: 처음 대기 상태, next 메소드를 아직 호출하지 않은 상태
# GEN_RUNNING: 실행 상태
# GEN_SUSPENDED: yield 대기 상태
# GEN_CLOSED: 실행 완료 상태

def coroutine2(x):
    print('>>> coroutine started: {}'.format(x))
    y = yield x
    print('>>> coroutine received: {}'.format(y))
    z = yield x + y
    print('>>> coroutine received: {}'.format(z))

c3 = coroutine2(10)

from inspect import getgeneratorstate

print('Ex1_2: ', getgeneratorstate(c3))
print(next(c3))
print('Ex1_3: ', getgeneratorstate(c3))
print(c3.send(15))

# print(c3.send(20)) # stopiteration 예외 발생

# 데코레이터 패턴을 사용하면 꼭 next로만 시작하지 않아도 된다!
from functools import wraps

def coroutine(func):
    '''
    Decorator run util yield
    '''
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return primer

@coroutine
def sumer():
    total = 0
    term = 0
    while True:
        term = yield total
        total += term

su = sumer()
print('Ex2_1: ', su.send(100))
print('Ex2_2: ', su.send(40))
print('Ex2_3: ', su.send(60))


# 코루틴 예제 3(예외처리)

class SampleException(Exception):
    '''설명에 사용할 예외 유형'''

def coroutine_except():
    print('>> coroutine started.')
    try:
        while True:
            try:
                x = yield
            except SampleException:
                print('-> SampleException handled. Continuing..')
            else:
                print('-> coroutine received: {}'.format(x))
    finally:
        print('-> coroutine ending')

exe_co = coroutine_except()
print('Ex3_1: ', next(exe_co))
print('Ex3_2: ', exe_co.send(10))
print('Ex3_3: ', exe_co.send(100))
print('Ex3_4: ', exe_co.throw(SampleException))
print('Ex3_5: ', exe_co.send(1000))
print('Ex3_3: ', exe_co.close()) # GEN_CLOSED state
# print('Ex3_3: ', exe_co.send(5))
print()

# 코루틴 예제4(return)

def averager_re():
    total = 0.0
    cnt = 0
    avg = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        cnt += 1
        avg = total/cnt
    return 'Average: {}'.format(avg)

avger2 = averager_re()

next(avger2)

avger2.send(10)
avger2.send(30)
avger2.send(50)

try:
    avger2.send(None)
except StopIteration as e:
    print('Ex4_1: ', e.value)

# Coroutine Ex5(yield from)
# StopIteration 자동처리(3.7 이후 yield from -> await)
# 중첩 코루틴 처리

def gen1():
    for x in 'AB':
        yield x
    for y in range(1, 4):
        yield y

t1 = gen1()

print('Ex5_1: ', next(t1))
print('Ex5_2: ', next(t1))
print('Ex5_3: ', next(t1))
print('Ex5_4: ', next(t1))
print('Ex5_5: ', next(t1))
# print('Ex5_6: ', next(t1)) # StopIteration

t2 = gen1()

print('Ex5_7: ', list(t2))
print()

# 중첩인 경우 좀 더 빠르게 사용할 수 있다!
def gen2():
    yield from 'ABCDEFG'
    yield from range(1, 4)

t3 = gen2()

print('Ex5_1: ', next(t3))
print('Ex5_2: ', next(t3))
print('Ex5_3: ', next(t3))
print('Ex5_4: ', next(t3))
print('Ex5_5: ', next(t3))
print('Ex5_6: ', next(t3)) 
print('Ex5_6: ', next(t3)) 
# print('Ex5_6: ', next(t3)) # StopIteration


t4 = gen2()

print('Ex5_7: ', list(t4))
print()

def gen3_sub():
    print('Sub coroutine.')
    x = yield 10
    print('Recieve: ', str(x))
    x = yield 100
    print('Recieve: ', str(x))

def gen4_main():
    yield from gen3_sub()

t5 = gen4_main()

print('Ex7_1: ', next(t5))
print('Ex7_1: ', t5.send(7))
# print('Ex7_1: ', t5.send(77)) # StopIteration
