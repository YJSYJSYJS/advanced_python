# Chapter02-2
# Advanced Python
# Special Method(Magic Method)
# ref1: https://docs.python.org/3/reference/datamodel.html#special-method-names
# ref2: https://www.tutorialsteacher.com/python/magic-methods-in-python

# magic method 실습
# 파이썬 핵심 framework -> Sequence, Iterator, Functions, Class

# Magic Meghod Basic Explanation

# 기본형
print(int)
print()

# 모든 속성 및 메소드 출력
print(dir(int))
print()

# 사용
n=100

print('Ex1_1: ', n+200)
print('Ex1_2: ', n.__add__(200))
print('Ex1_3: ', n.__doc__)
print('Ex1_4: ', n.__bool__(), bool(n))
print('Ex1_5: ', n*100, n.__mul__(100))

print()

# Class example1:
class Student:
    def __init__(self, name, height):
        self._name = name
        self._height = height

    def __str__(self):
        return 'Student Class Info: {}, {}'.format(self._name, self._height)

    def __ge__(self, x):
        print('Called. >> __ge__ Method.')
        if self._height >= x._height:
            return True

    def __le__(self, x):
        print('Called. >> __le__ Method.')
        if self._height <= x._height:
            return True

    def __sub__(self, x):
        print('Called. >> __sub__ Meghod.')
        return self._height - x._height
        
s1 = Student('James', 181)
s2 = Student('Mie', 165)

print('Ex2_1: ', s1._height >= s2._height, s1 >= s2)# >=: __ge__
print('Ex2_2: ', s1 <= s2)
print('Ex2_3: ', s1 - s2)
print('Ex2_4: ', s2 - s1)
print('Ex2_5: ', s1)
print('Ex2_6: ', s2)

print()

# Class Example2

class Vector(object):
    def __init__(self, *args):
        '''
        Create a vector, example: v = Vector(1,2)
        '''
        if len(args) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args
    
    def __repr__(self):
        '''
        Returns the vector informations
        '''
        return 'Vector(%r, %r)' % (self._x, self._y)

    def __add__(self, other):
        '''Returns the vector addition of self and other'''
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self, k):
        '''Returns the vector addition of self and k'''
        return Vector(self._x * k, self._y * k)

    def __bool__(self):
        return bool(max(self._x, self._y))

# Vector Instance
v1 = Vector(3, 5)
v2 = Vector(15, 20)
v3 = Vector() # 0, 0

# print Magic Method
print('Ex3_1: ', Vector.__init__.__doc__)
print('Ex3_2: ', Vector.__repr__.__doc__)
print('Ex3_3: ', Vector.__add__.__doc__)
print('Ex3_4: ', v1, v2, v3)
print('Ex3_5: ', v1 + v2)
print('Ex3_6: ', v1 * 4)
print('Ex3_7: ', v2 * 10)
print('Ex3_8: ', bool(v1), bool(v2))
print('Ex3_9: ', bool(v3))
print()

