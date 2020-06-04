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
        self.name = name
        self.number = number
        self.grade = grade
        self.details = details
        self.email = email 
        
        Studen.student_cnt += 1

    def __str__(self):
        return 'str {}'.format(self._name)


    def __repr__(self):
        return 'str {}'.format(self._name)

    def detail_info(self):
        print('Current ID: {}'.format(id(self)))
        print('Student Detail Info: {} {} {}'.format(self._name, self._email, self._details))

    def __del__(self):
        Student.student_cnt -= 1



