from data import students, classes

def show_menu(): #функция выводит меню для взаимодействия
    print("─" * 80)
    print("ГЕНЕРАТОР ОТЧЕТОВ ОБ УСПЕВАЕМОСТИ СТУДЕНТОВ\n")
    print("1. Показать отчет")
    print("2. Показать тестовые данные")
    print("0. Выход")

def show_test_data(): #функция выводит тестовые данные
    print("─" * 80)
    print("Тестовые данные студентов:\n")
    for s in students:
        print(f"{s['name']}")
        print(f"  Оценки: {s['grades']}")
        print(f"  Посещаемость: {s['attendance']}")
    print(f"\nЗанятия ({len(classes)}):")
    for c in classes:
        print(f"   {c}")
