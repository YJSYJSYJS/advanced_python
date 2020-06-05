# Chapter01-2
# 파이썬 심화
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지 등...
# Today: 
# 클래스 상세 설명
# 클래스 변수, 인스턴스 변수

# 클래스 재 선언
class Student():
    """
    Student Class
    Author: Youn
    Date: 2020.06.04
    """

    # class var
    student_cnt = 0

    def __init__(self, name, number, grade, details, email=None):
        # instance var
        self._name = name
        self._number = number
        self._grade = grade
        self._details = details
        self._email = email 
        
        Student.student_cnt += 1

    def __str__(self):
        return 'str {}'.format(self._name)


    def __repr__(self):
        return 'str {}'.format(self._name)

    def detail_info(self):
        print('Current ID: {}'.format(id(self)))
        print('Student Detail Info: {} {} {}'.format(self._name, self._email, self._details))

    def __del__(self):
        Student.student_cnt -= 1


# self의 의미
student1 = Student('Youn', 2, 3, {'gender': 'Male', 'score1': 100, 'score2': 100})
student2 = Student('Yoo', 4, 1, {'gender': 'Female', 'score1': 90, 'score2': 80}, 'stud2@google.com')

# ID 확인

print(id(student1))
print(id(student2))

# id가 다르다 -> data 값이 다르다? -> 모른다 -> 하지만 최소한 객체는 다르다

print(student1 == student2)
print(student1._name == student2._name)
print(student1 is student2) # id 값(reference label)이 같은지?

a = 'ABC'
b = a
print(a is b)
print(a == b)

# dir & dict 확인
# dict를 먼저 확인하고 없으면 dir로 확인
# dir이 정보(all attr)의 범위가 더 넓다
# dict는 값까지 보여주지만, class 정의 시에 설정해놓은 것들만 알려준다.

print(dir(student1))
print(student1.__dict__)
print(student2.__dict__)

# Docstring: 협업시 문제가 발생했을 때, 클래스나 함수를 정의한 담당자를 확인 가능
print(Student.__doc__)

# 실행
student1.detail_info()
student2.detail_info()

# 에러
# Student.detail_info()
# self라는 argument가 없다
# self: instance
Student.detail_info(student1)
Student.detail_info(student2)

# 비교
print(student1.__class__, student2.__class__)
print(id(student1.__class__)==id(student2.__class__))

# 인스턴스 변수
# 직접 접근 권장하지 않는다(PEP 문법 기준)
# 직접 접근 예시
# student1._name = 'Kim'
# print(student1._name)

print(student1._name, student2._name)
print(student1._email, student2._email)
print()
print()

# 클래스 변수
# 접근: 클래스든 인스턴스든 다 접근 가능
print(student1.student_cnt)
print(student2.student_cnt)
print(Student.student_cnt)
print()
print()


# 클래스 변수 공유 확인
print(Student.__dict__)
print(student1.__dict__)
# 인스턴스 검색 후 인스턴스에 없으면, 상위 클래스에 가서 찾아본다. 거기도 없으면 쭉 올라가서 object 까지
# 역은 성립하지 않는다!!!