# Sequence type
# Hash table -> 적은 리소스로 많은 데이터 효율적으로 관리
# Dictionary -> Key 중복 허용 X
# Set -> Key 중복 허용 X
# Dict 및 Set 심화

# Dict structure
print('Ex1_1: ',)
print(__builtins__.__dict__)
print()

# Hash 값 확인
t1 =(10,20,(30,40,50))
t2 = (10,20,[30,40,50])

print('Ex1_2: ', hash(t1))
# print('Ex1_3: ', hash(t2)) # 리스트는 변경이 가능하기 때문에 unhashable 
print()

# 지능형 딕셔너리(Comprehending Dict)
import csv

# 외부 csv to list of tuple
with open('./resources/test1.csv', 'r', encoding='UTF-8') as f:
    temp = csv.reader(f)
    # Header Skip
    next(temp)
    # 변환
    NA_CODES = [tuple(x) for x in temp]

print('Ex2_1: ', )
print(NA_CODES)

n_code1 = {country: code for country, code in NA_CODES}
n_code2 = {country.upper(): code for country, code in NA_CODES}
print()

print('EX2_2:', )
print(n_code1)
print()

print('EX2_3:', )
print(n_code2)
print()
# Dict Setdefault ex

source = (('k1', 'val1'), 
            ('k1', 'val2'),
            ('k2', 'val3'),
            ('k2', 'val4'),
            ('k2', 'val5'))

new_dict1 = {}

# No use setdefault
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]

print('Ex3_1: ', new_dict1)
print()

# Use setdefault -> 위 작업을 한줄에 수행, 성능도 더 좋음!
new_dict2={}
for k, v in source:
    new_dict2.setdefault(k, []).append(v) 
    ## 기본값으로 키를 그대로 사용하는데, 비어있으면 빈 리스트 반환 후 append, 있으면 해당 키에 리스트 append

print('Ex3_2: ', new_dict2)
print()

# 사용자 정의 dict 상속(UserDict 가능)

class UserDict(dict):
    def __missing__(self, key):
        print('Called: __missing__')
        if isinstance(key, str):
            raise KeyError
        return self[str(key)]

    def get(self, key, default=None):
        print('Called: __getitem__')
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        print('Called: __contains__')
        return key in self.keys() or str(key) in self.keys()

user_dict1 = UserDict(one=1, two=2)
user_dict2 = UserDict({'one': 1, 'two': 2})
user_dict3 = UserDict([('one', 1), ('two', 2)])
# 출력
print('Ex4_1: ', user_dict1, user_dict2, user_dict3)
print('Ex4_2: ', user_dict2.get('two')) # getitem
print('Ex4_3: ', 'one' in user_dict3) # contains True
# print('Ex4_4: ', user_dict3['three']) # raise KeyError
print('Ex4_5: ', user_dict3.get('three'))
print('Ex4_6: ', 'three' in user_dict3)
print()

# immutable Dict: 수정되지 않길 원하는 원본을 숨기는 기능!
from types import MappingProxyType
d = {'key1': 'TEST1'}

# immutable(read only)
d_frozen = MappingProxyType(d)

print('Ex5_1: ', d, id(d))
print('Ex5_2: ', d_frozen, id(d_frozen))
print('Ex5_3: ', d is d_frozen, d==d_frozen) # id와 value비교

# 수정 불가
# d_frozen['key1'] = 'TEST2' # 에러

d['key2'] = 'TEST2'

print('Ex5_4: ', d)

# Set 구조(Frozen set): 한번 정해지면 수정 불가
s1 = {'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'}
s2 = set(['Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'])
s3 = {3}
s4 = set() # not {} -> dictionary
s5 = frozenset({'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'})

# 추가
s1.add('Melon')
print('Ex6_1: ', s1, type(s1))

# 추가불가
# s5.add('Melon')

print('Ex6_1: ', s1, type(s1))
print('Ex6_2: ', s2, type(s2))
print('Ex6_3: ', s3, type(s3))
print('Ex6_4: ', s4, type(s4))
print('Ex6_5: ', s5, type(s5))

# 선언 최적화

from dis import dis

print('Ex6_6: ')
print(dis('{10}'))
print('Ex6_7: ')
print(dis('set([10])'))


# 지능형 집합(Comprehending Set)
from unicodedata import name
print('Ex7_1: ')
# print({chr(i) for i in range(0, 256)})
print({name(chr(i), '') for i in range(0,256)})