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
next(c1)

