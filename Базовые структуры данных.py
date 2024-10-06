grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
def get_aver_grade(students: set, grades: list) -> dict:
    students_grades = {}

    students = sorted(students)

    for i in range(len(students)):
        students_grades [students[i]] = sum(grades[i]) / len(grades[i])

    return students_grades
a = get_aver_grade(students, grades)
print(a)
