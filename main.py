
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades_student = {}

    def add_grade(self, course_name, grade):
        if course_name in self.grades_student:
            self.grades_student[course_name].append(grade)
        else:
            self.grades_student[course_name] = [grade]

    def average_grade(self):
        total = sum(sum(grades) for grades in self.grades_student.values())
        count = sum(len(grades) for grades in self.grades_student.values())
        return total / count if count > 0 else 0

    def __str__(self):
        return f"Имя: {self.name} Фамилия: {self.surname} Среднее оценка за домашние задания: {self.average_grade()} Курсы в процессе изучения: {self.courses_in_progress} Завершенные курсы: {self.finished_courses}"


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_lecturer = {}

    def add_lecture_grade(self, course_name, grade):
        if course_name in self.grades_lecturer:
            self.grades_lecturer[course_name].append(grade)
        else:
            self.grades_lecturer[course_name] = [grade]

    def average_grade(self):
        total = sum(sum(grades) for grades in self.grades_lecturer.values())
        count = sum(len(grades) for grades in self.grades_lecturer.values())
        return total / count if count > 0 else 0

    def __str__(self):
        return f"Имя: {self.name} Фамилия: {self.surname} Средняя оценка за лекции: {self.average_grade()}"


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f"Имя: {self.name} Фамилия: {self.surname}"

    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades_student:
                student.grades_student[course] += [grade]
            else:
                student.grades_student[course] = [grade]
        else:
            return 'Ошибка'

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_attached and course in lecturer.courses_attached:
            if course in lecturer.grades_lecturer:
                lecturer.grades_lecturer[course] += [grade]
            else:
                lecturer.grades_lecturer[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('sam', 'nikitin', 'male')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']
cool_lecturer = Lecturer('John', 'Jhonson')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['Git']
cool_lecturer.grades_lecturer['Python'] = [10, 10, 10, 10, 10]
cool_lecturer.grades_lecturer['Git'] = [10, 10, 10, 10, 9]
cool_reviewer = Reviewer('Alex', 'Vibe')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Git']
cool_reviewer.rate_student(best_student, 'Python', 10)
cool_reviewer.rate_student(best_student, 'Python', 9)
cool_reviewer.rate_student(best_student, 'Git', 7)
cool_reviewer.rate_student(best_student, 'Git', 8)

print(cool_reviewer)
print(cool_lecturer)
print(best_student)

