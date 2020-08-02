# namedtuple 실 사용 실습
# 학생 전체 그룹 생성
# 반 20명, 4개의 반 -> (A,B,C,D) 번호

# nt 선언
from collections import namedtuple as nt

Classes = nt('Classes', ['rank', 'number'])

# 그룹 리스트 선언
numbers = [str(n) for n in range(1, 21)]

'''
for n in range(1,21):
    numbers2.append(str(n))
print(numbers)
'''
ranks = 'A B C D'.split()

# List Comprehension
students = [Classes(rank, number) for rank in ranks for number in numbers]
print('Ex5_1: ', len(students))
print()
print('Ex5_2: ', students)

print()
print()

# 너무 긴 List comprehension은 가독성을 떨어트린다
students2 = [Classes(rank, number) for rank in 'A B C D'.split() 
                                        for number in [str(n) 
                                            for n in range(1, 21)]]
print('Ex6_1: ', len(students2))
print()
print('Ex6_2: ', students2)

print()
print()
# 출력
for s in students:
    print('Ex7_1: ', s)