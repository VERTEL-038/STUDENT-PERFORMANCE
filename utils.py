def calculate_average(grades):          # объявляем функцию, которая считает средний балл
    if not grades:                      # если список оценок пустой
        return 0.0                      # возвращаем 0.0
    return round(sum(grades) / len(grades), 2)   # считаем среднее и округляем до 2 знаков


def get_attendance_rate(attendance):    # функция считает процент посещаемости
    if not attendance:                  # если список посещаемости пустой
        return 0.0
    attended = sum(1 for x in attendance if x)   # считаем сколько True (был на занятии)
    return round((attended / len(attendance)) * 100, 1)  # считаем процент и округляем
