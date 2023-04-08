class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grade = float()

    def get_average_grade(self):
        if not self.grades:
            return 0
        spisok = []
        for i in self.grades.values():
            spisok.extend(i)
        return float(sum(spisok) / max(len(spisok), 1))

    # сравнение студентов(по средним оценкам за ДЗ)
    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Not a Student'
        return self.average_grade < other.average_grade

    def __gt__(self, other):
        if not isinstance(other, Student):
            return 'Not a Student'
        return self.average_grade > other.average_grade

    def __eq__(self, other):
        if not isinstance(other, Student):
            return 'Not a Student'
        return self.average_grade == other.average_grade

    def __str__(self):
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        res = f'Имя:{self.name}\n' \
              f'Фамилия:{self.surname}\n' \
              f'Средняя оценка за домашнее задание: {self.average_grade}\n' \
              f'Курсы в процессе обучени: {courses_in_progress_string}\n' \
              f'Завершенные курсы: {finished_courses_string}'
        return res

    def rate_hw(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in lector.courses_attached and course in self.courses_in_progress:
            if course in lector.grades:
                lector.grades[course] += [grade]
                lector.average_grade = lector.get_average_grade()
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_grade = float()

    def get_average_grade(self):
        if not self.grades:
            return 0
        spisok = []
        for i in self.grades.values():
            spisok.extend(i)
        return float(sum(spisok) / len(spisok))

    # сравнение лекторов(по средним оценкам за ДЗ)
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Not a lector'
        if not isinstance(self, Lecturer):
            return 'Not a lector'
        return self.average_grade < other.average_grade

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Not a lector'
        if not isinstance(self, Lecturer):
            return 'Not a lector'
        return self.average_grade > other.average_grade

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return 'Not a lector'
        if not isinstance(self, Lecturer):
            return 'Not a lector'
        return self.average_grade == other.average_grade

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade}'
        return res


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
                student.average_grade = student.get_average_grade()
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


student_1 = Student('Ruoy', 'Eman')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Введение в программирование', 'Git']

student_2 = Student('Max', 'Larionov')
student_2.courses_in_progress += ['Java']
student_2.finished_courses += ['Основы програмирования', 'SQL']

lector_1 = Lecturer('Nat', 'Ivanova')
lector_1.courses_attached += ['Python']

lector_2 = Lecturer('Dima', 'Ognenko')
lector_2.courses_attached += ['Java']

reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Java']

reviewer_2 = Reviewer('Ostap', 'Smit')
reviewer_2.courses_attached += ['Python']
reviewer_2.courses_attached += ['Java']

student_1.rate_hw(lector_1, 'Python', 10)
student_1.rate_hw(lector_1, 'Python', 10)
student_1.rate_hw(lector_1, 'Python', 10)

student_1.rate_hw(lector_2, 'Python', 5)
student_1.rate_hw(lector_2, 'Python', 7)
student_1.rate_hw(lector_2, 'Python', 4)

student_2.rate_hw(lector_1, 'Java', 7)
student_2.rate_hw(lector_1, 'Java', 6)
student_2.rate_hw(lector_1, 'Java', 4)

student_2.rate_hw(lector_2, 'Java', 8)
student_2.rate_hw(lector_2, 'Java', 7)
student_2.rate_hw(lector_2, 'Java', 1)

reviewer_1.rate_hw(student_1, 'Python', 6)
reviewer_1.rate_hw(student_1, 'Python', 4)
reviewer_1.rate_hw(student_1, 'Python', 10)

reviewer_2.rate_hw(student_2, 'Java', 3)
reviewer_2.rate_hw(student_2, 'Java', 6)
reviewer_2.rate_hw(student_2, 'Java', 2)



print(student_1)
print()
print(student_2)
print()
print(lector_1)
print()
print(lector_2)
print()
print(f'Результат сравнения по средним оценкам за ДЗ: {student_1 > student_2} ')
print()

student_list = [student_1, student_2]
lecturer_list = [lector_1, lector_2]

def student_rating(student_list, course_name):
    sum_all = 0
    count_all = 0
    for stud in student_list:
       if stud.courses_in_progress == [course_name]:
            sum_all += stud.average_grade
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all

def lecturer_rating(lecturer_list, course_name):
    sum_all = 0
    count_all = 0
    for lect in lecturer_list:
        if lect.courses_attached == [course_name]:
            sum_all += lect.average_grade
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all

print(f"Средняя оценка для всех студентов по курсу {'Python'}: {student_rating(student_list, 'Python')}")
print(f"Средняя оценка для всех лекторов по курсу {'Python'}: {lecturer_rating(lecturer_list, 'Python')}")

