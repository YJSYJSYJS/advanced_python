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

n_code1 = {country: code for country, code in NA_codes}
n_code2 = {country.upper(): code for country, code in NA_CODES}
print()

print('EX2_2:', )
print(n_code1)
print()

print('EX2_3:', )
print(n_code2)

# Dict Setdefault ex

source = (('k1', 'val1'), 
            ('k1', 'val2'),
            ('k2', 'val3'),
            ('k2', 'val4'),
            ('k2', 'val5'))

new_dict1 = {}

# No use setdefault
