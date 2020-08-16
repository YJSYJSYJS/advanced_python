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
