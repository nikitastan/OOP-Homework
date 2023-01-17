class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.gived_grades_to_lecturer = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in \
                set(self.courses_in_progress + self.finished_courses) and 0 <= grade <= 10:
            if course not in self.gived_grades_to_lecturer:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                return 'Оценка по данной дисциплине уже выставлена'
        else:
            return 'Ошибка'

    def mean_grades(self):
        if len(self.grades.values()) == 0:
            return 'Ошибка'
        else:
            all_grades = [item for values in self.grades.values() for item in values]
            return round(sum(all_grades)/len(all_grades), 2)

    def __str__(self):
        return (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за домашние задания: {self.mean_grades()}\n'
            f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
            f'Завершенные курсы: {", ".join(self.finished_courses)}\n'
        )

    def __lt__(self, other):
        if not isinstance(other, Student):
            return "Ошибка сравнения!"
        else:
            return self.mean_grades() < other.mean_grades()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за лекции: {self.mean_grades()}\n'
        )

    def mean_grades(self):
        if len(self.grades.values()) == 0:
            return 'Ошибка'
        else:
            all_grades = [item for values in self.grades.values() for item in values]
            return round(sum(all_grades)/len(all_grades), 2)

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return "Ошибка сравнения!"
        else:
            return self.mean_grades() < other.mean_grades()

class Reviewer(Mentor):
    def __str__(self):
        return (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
        )

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

# Функция расчета средней по курсу по всем студентам или лекторам
def group_mean(list_of_objects,course):
    means_list = []
    for member in list_of_objects:
        if course in member.grades:
            means_list += [sum(member.grades[course]) / len(member.grades[course])]
    if len(means_list) > 0:
        return round(sum(means_list)/len(means_list),2)
    else:
        return "Оценок по курсу еще нет"


# Создание примеров
students_list = []
lecturers_list = []

student1 = Student('Ruoy', 'Eman', 'male')
student1.courses_in_progress += ['Python', 'Git']
student1.finished_courses += ['Введение в программирование']
students_list.append(student1)

student2 = Student('Ivan', 'Ivanov', 'male')
student2.courses_in_progress += ['Python', 'Введение в программирование']
student2.finished_courses += ['Git']
students_list.append(student2)

lecturer1 = Lecturer('Petr', 'Petrov')
lecturers_list.append(lecturer1)
lecturer1.courses_attached += ['Git']

lecturer2 = Lecturer('Max', 'Maximov')
lecturers_list.append(lecturer2)
lecturer2.courses_attached += ['Введение в программирование', 'Python']

reviewer1 = Reviewer('Ann', 'Andreeva')
reviewer1.courses_attached += ['Введение в программирование', 'Python']

reviewer2 = Reviewer('Liza', 'Smith')
reviewer2.courses_attached += ['Git']

# Тестирование
reviewer2.rate_hw(student1, 'Git', 10)
reviewer1.rate_hw(student1, 'Python', 8)

reviewer1.rate_hw(student2, 'Введение в программирование', 9)
reviewer1.rate_hw(student2, 'Python', 7)

student1.rate_lecturer(lecturer1,'Git',5)
student1.rate_lecturer(lecturer2,'Введение в программирование',8)
student1.rate_lecturer(lecturer2,'Python',8)

student2.rate_lecturer(lecturer1,'Git',10)
student2.rate_lecturer(lecturer2,'Введение в программирование',10)
student2.rate_lecturer(lecturer2,'Python',10)

print(student2)
print(student1<student2)

print(lecturer1)
print(lecturer2)
print(lecturer1<lecturer2)

print(f'Средняя оценка по всем студентам по курсу Python: {group_mean(students_list, "Python")}')
print(f'Средняя оценка по всем лекторам по курсу Python: {group_mean(lecturers_list, "Python")}')




