def calculate_average(grades): #функция считает средний балл
    if not grades:
        return 0.0
    return round(sum(grades) / len(grades), 2)

def get_attendance_rate(attendance): #функция считает процент посещаемости
    if not attendance:
        return 0.0
    attended = sum(1 for x in attendance if x)
    return round((attended / len(attendance)) * 100, 1)
