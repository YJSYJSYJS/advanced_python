# Chapter06-1
# Concurrency(흐름제어, 병렬처리)
# Generator, 반복형

# Python Iteratables: for, collections, text files, list, Dict, Set, Tuple, unpacking, *args
# 공부 내용: 반복형 객체 내부적으로 iter 함수 내용, 제네레이터 동작 원리, yield from

# 반복 가능한 이유 -> iter(x) 함수 호출

t = 'ABCDEF'

# for 사용
for c in t:
    print('Ex1_1: ', c)

print()

# while 사용

w = iter(t)

while True:
    try:
        print('Ex1_2: ', next(w))
    except StopIteration:
        break

print()

from collections import abc

# 반복형인지 확인
print('Ex1_3: ', hasattr(t, '__iter__'))
print('Ex1_4: ', isinstance(t, abc.Iterable))

print()

# next 사용

class WordSplitIter:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(' ')

    def __next__(self): # Overriding
        print('Called __next__')
        try:
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration()
        self._idx += 1
        return word

    def __iter__(self):
        print('Called __iter__')
        return self

    def __repr__(self):
        return 'WordSplit(%s)' % (self._text)

wi = WordSplitIter('who says the nights are for sleeping')
print('Ex2_1: ', wi)
print('Ex2_2: ', next(wi))
print('Ex2_3: ', next(wi))
print('Ex2_4: ', next(wi))
print('Ex2_5: ', next(wi))
print('Ex2_6: ', next(wi))
print('Ex2_7: ', next(wi))
print('Ex2_8: ', next(wi))
# print('Ex2_9: ', next(wi))


# Generator Pattern
# 1. 지능형 리스트, 딕셔너리, 집합 -> 데이터 셋이 증가 될 경우 메모리 사용량 증가 -> 제너레이터가 완화시켜줌
# 2. 단위 실행 가능한 코루틴(Coroutine) 구현에 아주 중요
# 3. dict, list 한 번 호추할 때 마다 하나의 값만 리턴 -> 아주 적은 메모리 양 필요
class WordSplitGenerator:
    def __init__(self, text):
        self._text = text.split(' ')

    def __iter__(self):
        for word in self._text:
            yield word

    def __repr__(self):
        return 'WordSplit(%s)' % (self._text)

wg = WordSplitGenerator('who says the nights are for sleeping')

wt = iter(wg)

print('Ex3_1: ', wt)
print('Ex3_2: ', next(wt))
print('Ex3_3: ', next(wt))
print('Ex3_4: ', next(wt))
print('Ex3_5: ', next(wt))
print('Ex3_6: ', next(wt))
print('Ex3_7: ', next(wt))
print('Ex3_8: ', next(wt))
# print('Ex3_9: ', next(wt))

print()

# Generator 예제1

def generator_ex1():
    print('start')
    yield 'AAA'
    print('continue')
    yield 'BBB'
    print('end')

temp = iter(generator_ex1())

print('Ex4_1: ', next(temp))
print('Ex4_1: ', next(temp))
# print('Ex4_1: ', next(temp))

for v in generator_ex1(): # for 문에서는 더 안전하게 사용 가능, 사실 마지막에 StopIteration이 발생한 것!
    print('Ex4_3: ', v)

print()

# Generator 에제 2

temp2 = [x*3 for x in generator_ex1()]
temp3 = (x*3 for x in generator_ex1())

print('Ex5_1: ', temp2)
print('Ex5_2: ', temp3) # next가 호출되지 않았기 때문에 아직 메모리에 올라가지 않았음!!!

for i in temp2:
    print('Ex5_3: ', i)

for i in temp3:
    print('Ex5_4: ', i) # for 문에서 내부적으로 next를 호출

print()

# Generator example3(frequently used function)

import itertools

gen1 = itertools.count(1, 2.5)

print('Ex6_1: ', next(gen1))
print('Ex6_2: ', next(gen1))
print('Ex6_3: ', next(gen1))
print('Ex6_4: ', next(gen1)) # next호출 되기 전에는 식만 가지고 있다!
# ... infinitly
print()
# 조건
gen2 = itertools.takewhile(lambda n: n<1000, itertools.count(1, 2.5))

for v in gen2:
    print('Ex6_5: ', v)

print()

# 필터 반대 역할
gen3 = itertools.filterfalse(lambda n: n<3, [1,2,3,4,5]) # 조건에 반대되는 사항들
for v in gen3:
    print('Ex6_6: ', v)

# 누적 합계
gen4 = itertools.accumulate([x for x in range(1, 101)])

for v in gen4:
    print('Ex6_7: ', v)
print()

# 연결1
gen5 = itertools.chain('ABCDE', range(1, 11, 2))

print('Ex6_8: ', list(gen5))

# 연결2
gen6 = itertools.chain(enumerate('ABCDE'))
print('Ex6_9: ', list(gen6))

# 개별로 쪼개주는 메서드
gen7 = itertools.product('ABCDE')
print('Ex6_10: ', list(gen7))

# 연산
gen8 = itertools.product('ABCDE', repeat=2) # 2개씩 묶을 수 있는 모든 조합
print('Ex6_11: ', list(gen8))

# 그룹화
gen9 = itertools.groupby('AAAABBCCCCDDEEEE')
# print('Ex6_12: ', list(gen9))
for chr, group in gen9:
    print('Ex6_12: ', chr, ':', list(group))

print()
