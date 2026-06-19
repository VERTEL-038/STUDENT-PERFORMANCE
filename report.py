from data import students, classes
from utils import calculate_average, get_attendance_rate

def generate_report(): #создает список, куда будет сохраняться информация о каждом студенте
    student_stats = []

    for student in students:
        avg_grade = calculate_average(student["grades"])
        attendance_rate = get_attendance_rate(student["attendance"])

        student_stats.append({
            "name": student["name"],
            "avg_grade": avg_grade,
            "attendance_rate": attendance_rate
        })

    #начинаем вывод отчета  
    print("─" * 80)
    print("ОТЧЕТ ОБ УСПЕВАЕМОСТИ СТУДЕНТОВ\n")

    #выводим информацию по каждому студенту
    for student in students:
        avg_grade = calculate_average(student["grades"])
        attendance_rate = get_attendance_rate(student["attendance"])

        print(f"Студент: {student['name']}")
        print(f"   Средний балл: {avg_grade}")
        print(f"   Посещаемость: {attendance_rate}%")

    #успеваемость
    print("─" * 80)
    print("УСПЕВАЕМОСТЬ\n")

    best_student = student_stats[0]
    worst_student = student_stats[0]

    for s in student_stats:  #перебираем всех студентов
        if s["avg_grade"] > best_student["avg_grade"]:
            best_student = s
        if s["avg_grade"] < worst_student["avg_grade"]:
            worst_student = s

    print(f"Самый высокий балл: {best_student['name']} — {best_student['avg_grade']}")
    print(f"Самый низкий балл:  {worst_student['name']} — {worst_student['avg_grade']}")

    #посещаемость студентов
    print("─" * 80)
    print("ПОСЕЩАЕМОСТЬ\n")

    best_att = student_stats[0]
    worst_att = student_stats[0]

    for s in student_stats:
        if s["attendance_rate"] > best_att["attendance_rate"]:
            best_att = s
        if s["attendance_rate"] < worst_att["attendance_rate"]:
            worst_att = s

    print(f"Самая высокая посещаемость: {best_att['name']} — {best_att['attendance_rate']}%")
    print(f"Самая низкая посещаемость:  {worst_att['name']} — {worst_att['attendance_rate']}%")

    #посещаемость по занятиям
    print("─" * 80)
    print("ПОСЕЩАЕМОСТЬ ПО ЗАНЯТИЯМ\n")

    best_class = classes[0]
    worst_class = classes[0]
    best_pct = 0
    worst_pct = 100

    for i, class_name in enumerate(classes):
        attended = sum(1 for s in students if s["attendance"][i])
        percent = round((attended / len(students)) * 100, 1)

        if percent > best_pct:
            best_pct = percent
            best_class = class_name
        if percent < worst_pct:
            worst_pct = percent
            worst_class = class_name

    print(f"Наиболее посещаемое: {best_class} ({best_pct}%)")
    print(f"Наименее посещаемое: {worst_class} ({worst_pct}%)")
