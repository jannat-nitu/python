students_score = {
    "harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Naville": 62
}
student_grades = {}
for student in students_score:
    score = students_score[student]
    if score > 90:
        student_grades[student] = "outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectation"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"
print(student_grades)


