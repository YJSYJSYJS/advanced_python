# Chapter01-3
# 파이썬 심화
# 클래스 메소드, 인스턴스 메소드, 스테틱 메소드

# 기본 인스턴스 메소드

class Student(object):
    '''
    Student Class
    Author: Youn
    Date: 20.06.10
    Description: Class, Static, Instance Method
    '''

    # Class Variable
    tuition_per = 1.0

    def __init__(self, id, first_name, last_name, email, grade, tuition, gpa):
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._grade = grade
        self._tuition = tuition
        self._gpa = gpa

    # Instance Method
    def full_name(self):
        return '{}, {}'.format(self._first_name, self._last_name)

    # Instance Method
    def detail_info(self):
        return 'Student Detail Info: {}, {}, {}, {}, {}, {}'.format(self._id, self.full_name(), self._email, self._grade, self._tuition, self._gpa)

    # Instance Method
    def get_fee(self):
        return 'Before Tuition -> Id: {}, fee: {}'.format(self._id, self._tuition)

    # Instance Method
    def get_fee_calc(self):
        return 'After Tuition -> Id: {}, fee: {}'.format(self._id, self._tuition * Student.tuition_per)        

    def __str__(self):
        return 'Student Info -> name: {}, grade: {}, email: {}'.format(self.full_name(), self._grade, self._email)

    # Class Method
    @classmethod
    def raise_fee(cls, per):
        if per < 1:
            print('Please Enter 1 or More')
            return
        cls.tuition_per = per
        print('tuition raised successfully')

    # class method
    @classmethod
    def student_const(cls, id, first_name, last_name, email, grade, tuition, gpa):
        return cls(id, first_name, last_name, email, grade, tuition*cls.tuition_per, gpa)

    # Static Method -> flexible(parameter)
    @staticmethod
    def is_scholarship(inst):
        if inst._gpa>=3.5:
            return 'congrats {}!'.format(inst._last_name)
        return 'Doosan is so happy!'

student_1 = Student(1, 'Kim', 'Sarang', 'student1@naver.com', '1', 500, 3.5)
student_2 = Student(2, 'Youn', 'Jongsu', 'student2@daum.net', '2', 400, 4.3)

# 기본 정보
print(student_1.__dict__)
print(student_2) # str method 수행

# 전체 정보
print(student_1.detail_info())
print(student_2.detail_info())

# 학비 정보
print(student_1.get_fee())
print(student_2.get_fee())

print()
# 학비 인상
# Student.tuition_per = 1.2 # 직접 접근하면 안좋음! ---> 캡슐화(보호) 필요

# print(student_1.get_fee_calc())
# print(student_2.get_fee_calc())

# 학비 인상(클래스 메소드)
Student.raise_fee(1.2)
print(student_1.get_fee_calc())
print(student_2.get_fee_calc())

# 클래스 메소드 인스턴스 생성 실습
student_3 = Student.student_const(3, 'Jo', 'Hoyoung', 'ho@naver.com', '3', 100, 4.5)
student_4 = Student.student_const(4, 'Lee', 'Hyeonwook', 'wook@naver.com', '4', 200, 4.5)

print(student_3)
print(student_4)
print()

# 학비 변경 확인
print(student_3._tuition)
print(student_4._tuition)
print()

# 장학금 혜택 여부(스태틱 메소드 미사용 버전) -> 아래 메소드는 클래스 안에 있는 것이 자연스럽다!
def is_scholar(inst):
    if inst._gpa >= 3.5:
        return '{} is a scholarship recipient.'.format(inst._last_name)
    return 'Doosan is so happy'

print(is_scholar(student_1))
print(is_scholar(student_2))
print(is_scholar(student_3))
print(is_scholar(student_4))

# 장학금 혜택 여부(스태틱 메소드 사용)
print(Student.is_scholarship(student_1))
print(Student.is_scholarship(student_2))
print(Student.is_scholarship(student_3))
print(Student.is_scholarship(student_4))
print()
print(student_1.is_scholarship(student_1)) # 호출하는 형식도 자유로운 편

# Conclusion
# 스태틱 메소드 클래스 메소드 그냥 인스턴스 메소드 중 어떤 것도 다 같은 기능을 할 수 있다!
# 연관관계가 있다면 별도로 메소드를 만드는 것 보다는 클래스 안에 넣는 것이 권장된다!
# 클래스 부분만 따로 패키지화 혹은 모듈화하여 import하여 여러군데 공통으로 쓸 수 있다!
