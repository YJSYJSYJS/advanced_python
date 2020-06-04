# Chapter01-1
# 파이썬 심화
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지 등...
# Today: 
# 클래스 상세 설명
# 클래스 변수, 인스턴스 변수

# cf.절차지향
## 학생 집단을 표현
### 학생 1
student_name_1 = 'Kim'
student_number_1 = 1
student_grade_1 = 1
student_detail_1 = [{'gender': 'Male'}, 
{'score1': 95}, 
{'score2': 88}
]

### 학생 2
student_name_2 = 'Lee'
student_number_2 = 2
student_grade_2 = 2
student_detail_2 = [{'gender': 'Female'}, {'score1': 90}, {'score2': 89}]

### 학생 3
student_name_3 = 'Youn'
student_number_3 = 3
student_grade_3 = 3
student_detail_3 = [{'gender': 'Male'}, {'score1': 99}, {'score2': 99}]
###.......여러명 할 것 생각하면 머리가 아프다...

# List structure
student_names_list = ['Kim', 'Lee', 'Youn']
student_numbers_list = [1, 2, 3]
student_grades_list = [1, 2, 3]
student_details_list = [
    {'gender': 'Male', 'score1': 95, 'score2': 88},
    {'gender': 'Female', 'score1': 90, 'score2': 89},
    {'gender': 'Male', 'score1': 99, 'score2': 99}    
]

## member 1 delete at List structure
del student_names_list[1]
del student_numbers_list[1]
del student_grades_list[1]
del student_details_list[1]

print(student_names_list)
print(student_numbers_list)
print(student_grades_list)
print(student_details_list)
print()
print()
## Conclusion: hard to manage structure, must map the direct position of exact data

# Dictionary structure
students_dicts = [
    {'student_name': 'Kim', 'student_number': 1, 'student_grade': 1, 'student_detail': {'gender': 'Male', 'score1': 95, 'score2': 88}},
    {'student_name': 'Lee', 'student_number': 2, 'student_grade': 2, 'student_detail': {'gender': 'Female', 'score1': 90, 'score2': 89}},
    {'student_name': 'Youn', 'student_number': 3, 'student_grade': 3, 'student_detail': {'gender': 'Male', 'score1': 99, 'score2': 99}},
]

print(students_dicts)

## Delete at Dict structure

del students_dicts[1]

print(students_dicts)

## Conclusion: Easier and more comfortable than List structure but...
##              has repeating code structure problem
##              We can see these dict likely structures at database 
##              Usually we use dict structure when we transmit data to 3rd party(like Oracle, Mysql...)


# OOP(Object Oriented Program), Class structure
# We can express everything we feel in real world at a computer by Class structure
# Minimizes code repeat, Method, Easily Reusable after designed

class Student(object):
    def __init__(self, name, number, grade, details):
        self._name = name
        self._number = number
        self._grade = grade
        self._details = details

    def __str__(self):
        return 'str: {} - {}'.format(self._name, self._number)

    # __str__없을 때 __repr__(우선순위: str > repr)
    # repr(x)로 강제 호출도 가능
    def __repr__(self):
        return 'repr: {} - {}'.format(self._name, self._number)

student1 = Student('Kim', 1, 1, {'gender': 'Male', 'score1': 95, 'score2': 88})
student2 = Student('Lee', 2, 2, {'gender': 'Female', 'score1': 90, 'score2': 89})
student3 = Student('Youn', 3, 3, {'gender': 'Male', 'score1': 99, 'score2': 99})

print(student1.__dict__)
print(student2.__dict__)
print(student3.__dict__)


# List 선언
students_list = []

students_list.append(student1)
students_list.append(student2)
students_list.append(student3)

print()
print(students_list)

# 반복(__str__ 확인)
for s in students_list:
    print(repr(s))
    print(s)